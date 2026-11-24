
import numpy as np
import pytest

from affine import Affine
from rasterio.crs import CRS

from src.geospatial import (
    read_geotiff,
    get_pixel_area,
    calculate_affected_area,
    extract_change_polygons
)


def test_pixel_area_calculation():

    transform = Affine(
        10, 0, 500000,
        0, -10, 4500000
    )

    crs = CRS.from_epsg(32643)

    area = get_pixel_area(
        transform,
        crs
    )

    assert area == 100.0


def test_affected_area_calculation():

    change_mask = np.array(
        [
            [255, 0, 255],
            [0, 255, 0],
            [255, 255, 0]
        ],
        dtype=np.uint8
    )

    transform = Affine(
        10, 0, 500000,
        0, -10, 4500000
    )

    crs = CRS.from_epsg(32643)

    result = calculate_affected_area(
        change_mask,
        transform,
        crs
    )

    assert result["changed_pixels"] == 5

    assert result["area_square_metres"] == 500.0

    assert result["area_hectares"] == 0.05


def test_extract_change_polygons():

    change_mask = np.array(
        [
            [255, 255, 0],
            [255, 255, 0],
            [0, 0, 255]
        ],
        dtype=np.uint8
    )

    transform = Affine(
        10, 0, 500000,
        0, -10, 4500000
    )

    polygons = extract_change_polygons(
        change_mask,
        transform
    )

    assert len(polygons) == 2

    assert all(
        polygon.is_valid
        for polygon in polygons
    )


def test_geographic_coordinates_required():

    transform = Affine(
        10, 0, 500000,
        0, -10, 4500000
    )

    crs = CRS.from_epsg(4326)

    with pytest.raises(ValueError):

        get_pixel_area(
            transform,
            crs
        )


def test_invalid_change_mask():

    transform = Affine(
        10, 0, 500000,
        0, -10, 4500000
    )

    crs = CRS.from_epsg(32643)

    with pytest.raises(ValueError):

        calculate_affected_area(
            np.array([]),
            transform,
            crs
        )


def test_read_geotiff(tmp_path):

    import rasterio

    image_path = tmp_path / "sample.tif"

    image = np.ones(
        (3, 20, 20),
        dtype=np.uint8
    )

    transform = Affine(
        10, 0, 500000,
        0, -10, 4500000
    )

    with rasterio.open(
        image_path,
        "w",
        driver="GTiff",
        height=20,
        width=20,
        count=3,
        dtype="uint8",
        crs="EPSG:32643",
        transform=transform
    ) as dataset:

        dataset.write(image)

    loaded_image, metadata = read_geotiff(
        str(image_path)
    )

    assert loaded_image.shape == (3, 20, 20)

    assert metadata["crs"] == "EPSG:32643"

    assert metadata["width"] == 20

    assert metadata["height"] == 20
