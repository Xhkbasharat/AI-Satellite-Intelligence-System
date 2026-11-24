
import numpy as np
import pytest
import cv2

from src.preprocessing import (
    resize_image,
    normalize_image,
    prepare_model_input
)


def test_resize_image():

    image = np.random.randint(
        0,
        256,
        (512, 512, 3),
        dtype=np.uint8
    )

    resized = resize_image(
        image,
        size=256
    )

    assert resized.shape == (256, 256, 3)


def test_normalize_image():

    image = np.array(
        [
            [0, 50],
            [100, 200]
        ],
        dtype=np.float32
    )

    normalized = normalize_image(image)

    assert normalized.min() == 0.0
    assert normalized.max() == 1.0

    assert np.isfinite(normalized).all()


def test_normalize_constant_image():

    image = np.full(
        (10, 10, 3),
        50,
        dtype=np.float32
    )

    normalized = normalize_image(image)

    assert np.all(normalized == 0)


def test_prepare_model_input():

    image = np.random.random(
        (256, 256, 3)
    ).astype(np.float32)

    prepared = prepare_model_input(image)

    assert prepared.shape == (3, 256, 256)

    assert prepared.dtype == np.float32


def test_invalid_model_input():

    image = np.random.random(
        (256, 256)
    ).astype(np.float32)

    with pytest.raises(ValueError):

        prepare_model_input(image)


def test_invalid_resize_image():

    image = np.array([])

    with pytest.raises(ValueError):

        resize_image(image)


def test_normalize_invalid_values():

    image = np.array(
        [[np.nan, 10]],
        dtype=np.float32
    )

    with pytest.raises(ValueError):

        normalize_image(image)
