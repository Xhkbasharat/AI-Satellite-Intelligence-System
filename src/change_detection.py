
import cv2
import numpy as np


def validate_images(image1, image2):
    """
    Validate that both images have compatible shapes.
    """

    if image1 is None or image2 is None:
        raise ValueError("Both images are required.")

    if image1.shape != image2.shape:
        raise ValueError(
            "Both images must have the same dimensions "
            "and number of channels."
        )


def detect_changes(image1, image2, threshold=30):
    """
    Detect changes between two satellite images
    using pixel intensity differences.

    Returns:
        change_mask: Binary mask of changed pixels.
        difference: Absolute difference image.
    """

    validate_images(image1, image2)

    if not 0 <= threshold <= 255:
        raise ValueError(
            "Threshold must be between 0 and 255."
        )

    # Convert images to grayscale
    gray1 = cv2.cvtColor(
        image1.astype(np.uint8),
        cv2.COLOR_RGB2GRAY
    )

    gray2 = cv2.cvtColor(
        image2.astype(np.uint8),
        cv2.COLOR_RGB2GRAY
    )

    # Calculate absolute difference
    difference = cv2.absdiff(
        gray1,
        gray2
    )

    # Apply binary threshold
    _, change_mask = cv2.threshold(
        difference,
        threshold,
        255,
        cv2.THRESH_BINARY
    )

    return change_mask, difference


def calculate_change_percentage(change_mask):
    """
    Calculate the percentage of changed pixels.
    """

    if change_mask is None or change_mask.size == 0:
        raise ValueError("Invalid change mask.")

    changed_pixels = np.count_nonzero(
        change_mask
    )

    total_pixels = change_mask.size

    percentage = (
        changed_pixels / total_pixels
    ) * 100

    return round(float(percentage), 2)


def create_change_visualization(
    image,
    change_mask,
    color=(255, 0, 0),
    alpha=0.5
):
    """
    Highlight detected changes on the original image.
    """

    if image is None or change_mask is None:
        raise ValueError("Image and mask are required.")

    if image.shape[:2] != change_mask.shape[:2]:
        raise ValueError(
            "Image and change mask dimensions must match."
        )

    if not 0 <= alpha <= 1:
        raise ValueError(
            "Alpha must be between 0 and 1."
        )

    result = image.copy().astype(np.uint8)

    overlay = result.copy()

    overlay[change_mask > 0] = color

    visualization = cv2.addWeighted(
        overlay,
        alpha,
        result,
        1 - alpha,
        0
    )

    return visualization


def compare_satellite_images(
    image1,
    image2,
    threshold=30
):
    """
    Complete satellite image change detection pipeline.
    """

    change_mask, difference = detect_changes(
        image1,
        image2,
        threshold
    )

    change_percentage = calculate_change_percentage(
        change_mask
    )

    visualization = create_change_visualization(
        image2,
        change_mask
    )

    return {
        "change_mask": change_mask,
        "difference": difference,
        "visualization": visualization,
        "change_percentage": change_percentage
    }
