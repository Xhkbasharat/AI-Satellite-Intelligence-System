
# Testing Guide

This directory contains automated tests for the AI Satellite Intelligence System.

## Test Files

| File | What It Tests |
|---|---|
| `test_preprocessing.py` | Image loading, resizing, and normalization |
| `test_geospatial.py` | GeoTIFF metadata and geographic calculations |
| `test_change_detection.py` | Image comparison and change detection |
| `test_visualization.py` | Segmentation maps and image overlays |

## Install Testing Dependencies

From the repository root, run:

```bash
pip install -r requirements-dev.txt
```

## Run All Tests

```bash
pytest -v
```

## Run a Specific Test

```bash
pytest tests/test_preprocessing.py -v
```

## Generate a Coverage Report

```bash
pytest --cov=src --cov-report=term-missing
```

## Testing Notes

- Tests use small synthetic images where possible.
- Geospatial tests may create temporary GeoTIFF files.
- A passing test suite does not establish the accuracy of a trained segmentation model.
- Real-world validation requires representative satellite imagery and correctly labeled ground-truth masks.
