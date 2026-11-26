
# Satellite Dataset Preparation Guide

## 1. Dataset Overview

The AI Satellite Intelligence System requires satellite images and corresponding segmentation masks for supervised land-cover training.

## 2. Directory Structure

```text
data/
├── raw/
│   ├── images/
│   │   ├── tile_001.png
│   │   └── tile_002.png
│   └── masks/
│       ├── tile_001.png
│       └── tile_002.png
└── processed/
```

## 3. Image Requirements

Supported formats:
- PNG
- JPG
- JPEG
- TIFF
- TIF

Images should:
- Represent genuine satellite or aerial imagery.
- Have sufficient spatial resolution.
- Use consistent band ordering.
- Be correctly paired with their segmentation masks.

## 4. Segmentation Class Mapping

The current configuration defines five classes:

| Class ID | Class Name |
|---|---|
| 0 | Background |
| 1 | Water |
| 2 | Vegetation |
| 3 | Buildings |
| 4 | Bare land |

All masks must use these integer IDs.

**Important:** This is the project's current label convention, not a universal satellite dataset standard. Dataset labels must be mapped to these IDs before training.

## 5. Data Quality Checks

Before training, verify:

1. Every image has a matching mask.
2. Image and mask dimensions match.
3. Masks contain only valid class IDs.
4. Images and masks are spatially aligned.
5. Training and validation samples are separated appropriately.

## 6. Dataset Licensing

Use datasets whose licenses permit your intended research and distribution. Record the dataset name, source, license, and preprocessing steps.

## 7. Recommended Validation

Inspect several image-mask pairs visually before starting training. Incorrect label mappings or misaligned masks can seriously reduce model performance.
