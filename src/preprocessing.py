
import os
import cv2
import numpy as np

from config import Config


def load_satellite_image(image_path):
    """
    Load a satellite image from disk.
    Supports standard images and GeoTIFF files.
    """

    if not os.path.exists(image_path):
        raise FileNotFoundError(
            f"Image not found: {image_path}"
        )

    extension = os.path.splitext(image_path)[1].lower()

    if extension in [".tif", ".tiff"]:
        import rasterio

        with rasterio.open(image_path) as src:
            image = src.read(
                indexes=[1, 2, 3]
                if src.count >= 3
                else [1]
            )
            image = np.moveaxis(image, 0, -1)

            if image.shape[-1] == 1:
                image = np.repeat(image, 3, axis=-1)

            image = np.nan_to_num(image)

            return image.astype(np.float32)

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(
            "Unable to read the satellite image."
        )

    image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    return image


def resize_image(image, size=None):
    """
    Resize image to the configured dimensions.
    """

    if size is None:
        size = Config.IMAGE_SIZE

    if image is None or image.size == 0:
        raise ValueError("Invalid image.")

    resized = cv2.resize(
        image,
        (size, size),
        interpolation=cv2.INTER_AREA
    )

    return resized


def normalize_image(image):
    """
    Normalize image pixel values to the range 0 to 1.
    """

    image = image.astype(np.float32)

    if not np.isfinite(image).all():
        raise ValueError(
            "Image contains invalid pixel values."
        )

    minimum = float(np.min(image))
    maximum = float(np.max(image))

    if maximum == minimum:
        return np.zeros_like(image, dtype=np.float32)

    normalized = (
        (image - minimum) /
        (maximum - minimum)
    )

    return normalized.astype(np.float32)


def preprocess_satellite_image(image_path):
    """
    Complete preprocessing pipeline.
    """

    image = load_satellite_image(image_path)

    image = resize_image(image)

    image = normalize_image(image)

    return image


def prepare_model_input(image):
    """
    Convert image into PyTorch-compatible
    channel-first format.
    """

    if image.ndim != 3 or image.shape[-1] != 3:
        raise ValueError(
            "Expected an RGB image with 3 channels."
        )

    image = np.transpose(
        image,
        (2, 0, 1)
    )

    return image.astype(np.float32)
