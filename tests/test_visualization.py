
import numpy as np

from src.visualization import (
    create_overlay,
    create_segmentation_visualization,
)


def test_segmentation_visualization_returns_rgb_image():
    mask = np.zeros((64, 64), dtype=np.uint8)

    result = create_segmentation_visualization(mask)

    assert result.shape == (64, 64, 3)
    assert result.dtype == np.uint8


def test_create_overlay_preserves_image_dimensions():
    image = np.zeros((64, 64, 3), dtype=np.float32)
    mask = np.zeros((64, 64), dtype=np.uint8)

    result = create_overlay(image, mask)

    assert result.shape == (64, 64, 3)
    assert result.dtype == np.uint8


def test_visualization_handles_multiple_classes():
    mask = np.zeros((64, 64), dtype=np.uint8)
    mask[0:32, 0:32] = 1
    mask[32:64, 0:32] = 2
    mask[0:32, 32:64] = 3
    mask[32:64, 32:64] = 4

    result = create_segmentation_visualization(mask)

    assert result.shape == (64, 64, 3)
    assert len(np.unique(result.reshape(-1, 3), axis=0)) > 1
