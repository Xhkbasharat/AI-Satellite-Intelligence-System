
import torch
import numpy as np

from sklearn.metrics import confusion_matrix

from config import Config
from src.segmentation import load_segmentation_model


def calculate_metrics(
    predictions,
    targets,
    num_classes=None
):
    """
    Calculate segmentation evaluation metrics.

    Args:
        predictions: Predicted class IDs.
        targets: Actual class IDs.
        num_classes: Number of segmentation classes.
    """

    if num_classes is None:
        num_classes = Config.NUM_CLASSES

    predictions = np.asarray(predictions).reshape(-1)
    targets = np.asarray(targets).reshape(-1)

    if predictions.size == 0 or targets.size == 0:
        raise ValueError("Predictions and targets cannot be empty.")

    if predictions.shape != targets.shape:
        raise ValueError(
            "Predictions and targets must have equal sizes."
        )

    if (
        predictions.min() < 0
        or targets.min() < 0
        or predictions.max() >= num_classes
        or targets.max() >= num_classes
    ):
        raise ValueError("Invalid class IDs detected.")

    matrix = confusion_matrix(
        targets,
        predictions,
        labels=list(range(num_classes))
    )

    accuracy = (
        np.trace(matrix) / matrix.sum()
        if matrix.sum() > 0 else 0.0
    )

    intersection = np.diag(matrix).astype(float)

    actual_pixels = matrix.sum(axis=1).astype(float)
    predicted_pixels = matrix.sum(axis=0).astype(float)

    union = (
        actual_pixels
        + predicted_pixels
        - intersection
    )

    iou = np.divide(
        intersection,
        union,
        out=np.full(num_classes, np.nan),
        where=union != 0
    )

    dice_denominator = (
        actual_pixels + predicted_pixels
    )

    dice = np.divide(
        2 * intersection,
        dice_denominator,
        out=np.full(num_classes, np.nan),
        where=dice_denominator != 0
    )

    mean_iou = (
        float(np.nanmean(iou))
        if np.any(~np.isnan(iou)) else 0.0
    )

    mean_dice = (
        float(np.nanmean(dice))
        if np.any(~np.isnan(dice)) else 0.0
    )

    return {
        "accuracy": round(float(accuracy), 4),
        "mean_iou": round(mean_iou, 4),
        "mean_dice": round(mean_dice, 4),
        "class_iou": [
            None if np.isnan(value)
            else round(float(value), 4)
            for value in iou
        ],
        "class_dice": [
            None if np.isnan(value)
            else round(float(value), 4)
            for value in dice
        ],
        "confusion_matrix": matrix.tolist()
    }


def evaluate_model(
    model,
    data_loader,
    device=None
):
    """
    Evaluate a trained segmentation model.
    """

    if device is None:
        device = next(model.parameters()).device

    model.eval()

    all_predictions = []
    all_targets = []

    with torch.no_grad():

        for images, masks in data_loader:

            images = images.to(device)

            outputs = model(images)

            predictions = torch.argmax(
                outputs,
                dim=1
            )

            all_predictions.append(
                predictions.cpu().numpy()
            )

            all_targets.append(
                masks.numpy()
            )

    predictions = np.concatenate(
        all_predictions,
        axis=0
    )

    targets = np.concatenate(
        all_targets,
        axis=0
    )

    return calculate_metrics(
        predictions,
        targets
    )


def load_and_evaluate(
    model_path,
    data_loader
):
    """
    Load trained U-Net weights and evaluate them.
    """

    device = torch.device(
        "cuda" if torch.cuda.is_available()
        else "cpu"
    )

    model = load_segmentation_model(
        model_path=model_path,
        device=device
    )

    results = evaluate_model(
        model,
        data_loader,
        device
    )

    print("\nMODEL EVALUATION RESULTS")
    print("------------------------")

    print(
        f"Accuracy: {results['accuracy']}"
    )

    print(
        f"Mean IoU: {results['mean_iou']}"
    )

    print(
        f"Mean Dice: {results['mean_dice']}"
    )

    return results
