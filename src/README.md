
# Core Source Modules

This directory contains the main processing components of the AI Satellite Intelligence System.

## Modules

| File | Responsibility |
|---|---|
| `preprocessing.py` | Load, resize, and normalize satellite images |
| `segmentation.py` | U-Net model and segmentation prediction |
| `change_detection.py` | Detect pixel-level differences between images |
| `geospatial.py` | Read GeoTIFF metadata and calculate geographic areas |
| `visualization.py` | Generate segmentation maps and image overlays |

## Processing Pipeline

1. Load satellite imagery.
2. Preprocess the image.
3. Run the segmentation model.
4. Generate a land-cover mask.
5. Compare images for potential changes.
6. Generate visualizations and geospatial summaries.

## Important Limitations

- Pixel-level change detection requires correctly aligned images.
- Accurate area calculations require suitable geospatial metadata and coordinate reference systems.
- Segmentation quality depends on the training dataset and model weights.
- Predictions from an untrained model are not reliable analytical results.

## Development

Run tests from the repository root:

```bash
pytest -q
```
