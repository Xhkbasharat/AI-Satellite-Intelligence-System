
import numpy as np
import rasterio

from rasterio.features import shapes
from shapely.geometry import shape


def read_geotiff(image_path):
    """
    Read a GeoTIFF image and return its metadata.
    """

    with rasterio.open(image_path) as src:
        image = src.read()

        metadata = {
            "crs": str(src.crs) if src.crs else None,
            "transform": src.transform,
            "width": src.width,
            "height": src.height,
            "count": src.count,
            "bounds": src.bounds,
            "resolution": src.res
        }

    return image, metadata


def get_pixel_area(transform, crs):
    """
    Calculate pixel area in square metres.

    Requires a projected CRS with metre units.
    """

    if crs is None:
        raise ValueError(
            "Image must have a defined CRS."
        )

    if not crs.is_projected:
        raise ValueError(
            "Pixel area calculation requires a "
            "projected CRS in metres. Reproject the "
            "image before calculating area."
        )

    units = [
        axis.unit_name.lower()
        for axis in crs.axis_info[:2]
    ]

    if not all(
        "metre" in unit or "meter" in unit
        for unit in units
    ):
        raise ValueError(
            "Projected CRS must use metre units."
        )

    pixel_area = abs(
        transform.a * transform.e -
        transform.b * transform.d
    )

    return float(pixel_area)


def calculate_affected_area(change_mask, transform, crs):
    """
    Calculate the total affected area.

    Args:
        change_mask: Binary change mask.
        transform: Rasterio affine transform.
        crs: Raster coordinate reference system.

    Returns:
        Area in square metres, hectares,
        and square kilometres.
    """

    if change_mask is None or change_mask.size == 0:
        raise ValueError("Invalid change mask.")

    pixel_area = get_pixel_area(
        transform,
        crs
    )

    changed_pixels = np.count_nonzero(
        change_mask
    )

    area_m2 = changed_pixels * pixel_area

    area_hectares = area_m2 / 10000

    area_km2 = area_m2 / 1000000

    return {
        "changed_pixels": int(changed_pixels),
        "area_square_metres": round(
            float(area_m2), 2
        ),
        "area_hectares": round(
            float(area_hectares), 4
        ),
        "area_square_kilometres": round(
            float(area_km2), 6
        )
    }


def extract_change_polygons(change_mask, transform):
    """
    Convert detected change regions into polygons.
    """

    if change_mask is None or change_mask.size == 0:
        raise ValueError("Invalid change mask.")

    binary_mask = (
        change_mask > 0
    ).astype(np.uint8)

    polygons = []

    for geometry, value in shapes(
        binary_mask,
        mask=binary_mask.astype(bool),
        transform=transform
    ):
        if value == 1:
            polygons.append(
                shape(geometry)
            )

    return polygons


def get_geographic_summary(image_path, change_mask):
    """
    Generate a geographic summary for a
    detected change mask.
    """

    with rasterio.open(image_path) as src:
        if change_mask.shape != (
            src.height,
            src.width
        ):
            raise ValueError(
                "Change mask dimensions must match "
                "the original GeoTIFF dimensions."
            )

        area = calculate_affected_area(
            change_mask,
            src.transform,
            src.crs
        )

        polygons = extract_change_polygons(
            change_mask,
            src.transform
        )

        return {
            "crs": str(src.crs),
            "bounds": {
                "left": src.bounds.left,
                "bottom": src.bounds.bottom,
                "right": src.bounds.right,
                "top": src.bounds.top
            },
            "affected_area": area,
            "change_regions": len(polygons)
        }
