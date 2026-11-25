
import numpy as np
import pytest

from src.change_detection import detect_changes, validate_images


def test_validate_images_accepts_matching_shapes():
    image_a = np.zeros((64, 64, 3), dtype=np.uint8)
    image_b = np.ones((64, 64, 3), dtype=np.uint8)

    assert validate_images(image_a, image_b) is True


def test_validate_images_rejects_different_shapes():
    image_a = np.zeros((64, 64, 3), dtype=np.uint8)
    image_b = np.zeros((32, 32, 3), dtype=np.uint8)

    with pytest.raises(ValueError):
        validate_images(image_a, image_b)


def test_detect_changes_returns_expected_keys():
    image_a = np.zeros((64, 64, 3), dtype=np.uint8)
    image_b = np.zeros((64, 64, 3), dtype=np.uint8)

    result = detect_changes(image_a, image_b)

    assert "change_mask" in result
    assert "change_percentage" in result
    assert result["change_mask"].shape == (64, 64)


def test_detect_changes_finds_obvious_change():
    image_a = np.zeros((64, 64, 3), dtype=np.uint8)
    image_b = image_a.copy()
    image_b[20:40, 20:40] = 255

    result = detect_changes(image_a, image_b, threshold=20)

    assert result["change_percentage"] > 0
