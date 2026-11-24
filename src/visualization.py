
import os

import numpy as np
import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import plotly.express as px


# Land-cover class colors
CLASS_COLORS = {
    0: [0, 0, 0],          # Background
    1: [0, 100, 255],      # Water
    2: [0, 180, 0],        # Vegetation
    3: [220, 50, 50],      # Buildings
    4: [190, 160, 100]     # Bare land
}

CLASS_NAMES = {
    0: "Background",
    1: "Water",
    2: "Vegetation",
    3: "Buildings",
    4: "Bare Land"
}


def create_segmentation_visualization(mask):
    """
    Convert a segmentation mask into an RGB image.
    """

    if mask is None or mask.size == 0:
        raise ValueError("Invalid segmentation mask.")

    if not np.issubdtype(mask.dtype, np.integer):
        raise ValueError(
            "Segmentation mask must contain integer class IDs."
        )

    if np.any(mask < 0) or np.any(mask >= len(CLASS_COLORS)):
        raise ValueError(
            "Segmentation mask contains unknown class IDs."
        )

    height, width = mask.shape

    output = np.zeros(
        (height, width, 3),
        dtype=np.uint8
    )

    for class_id, color in CLASS_COLORS.items():
        output[mask == class_id] = color

    return output


def create_overlay(
    original_image,
    segmentation_mask,
    alpha=0.5
):
    """
    Overlay segmentation results on the original image.
    """

    if original_image is None or segmentation_mask is None:
        raise ValueError("Image and mask are required.")

    if original_image.shape[:2] != segmentation_mask.shape:
        raise ValueError(
            "Image and mask dimensions must match."
        )

    if not 0 <= alpha <= 1:
        raise ValueError("Alpha must be between 0 and 1.")

    original = np.asarray(original_image)

    if not np.issubdtype(original.dtype, np.number):
        raise ValueError("Image must contain numeric pixels.")

    if not np.isfinite(original).all():
        raise ValueError("Image contains invalid pixel values.")

    if original.max() <= 1:
        original = original * 255

    original = np.clip(original, 0, 255).astype(np.uint8)

    colored_mask = create_segmentation_visualization(
        segmentation_mask
    )

    overlay = (
        original.astype(np.float32) * (1 - alpha)
        + colored_mask.astype(np.float32) * alpha
    )

    return np.clip(overlay, 0, 255).astype(np.uint8)


def save_visualization(
    image,
    output_path,
    title="Satellite Analysis"
):
    """
    Save an image visualization to disk.
    """

    if image is None or image.size == 0:
        raise ValueError("Invalid visualization image.")

    output_dir = os.path.dirname(output_path)

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    plt.figure(figsize=(10, 8))

    plt.imshow(image)

    plt.title(title)

    plt.axis("off")

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight"
    )

    plt.close()


def create_class_distribution(mask):
    """
    Calculate the percentage of each land-cover class.
    """

    if mask is None or mask.size == 0:
        raise ValueError("Invalid segmentation mask.")

    total_pixels = mask.size

    distribution = {}

    for class_id, class_name in CLASS_NAMES.items():

        count = np.count_nonzero(
            mask == class_id
        )

        percentage = (
            count / total_pixels
        ) * 100

        distribution[class_name] = round(
            float(percentage), 2
        )

    return distribution


def create_interactive_chart(distribution):
    """
    Create an interactive land-cover distribution chart.
    """

    labels = list(distribution.keys())

    values = list(distribution.values())

    figure = px.pie(
        names=labels,
        values=values,
        title="Satellite Land Cover Distribution",
        hole=0.4
    )

    figure.update_traces(
        textposition="inside",
        textinfo="label+percent"
    )

    return figure
