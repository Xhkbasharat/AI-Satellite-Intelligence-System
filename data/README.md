
# Satellite Dataset Guide

This directory stores the datasets used by the AI Satellite Intelligence System.

## Directory Structure

```text
data/
├── README.md
├── raw/
│   ├── images/
│   └── masks/
└── processed/
```

## Raw Images

Place original satellite images inside:

`data/raw/images/`

Supported formats include:
- PNG
- JPG
- JPEG
- TIFF
- TIF

## Segmentation Masks

Place corresponding segmentation masks inside:

`data/raw/masks/`

Each mask must have the same filename stem as its satellite image.

Example:

```text
images/
└── tile_001.png

masks/
└── tile_001.png
```

## Class Labels

The current configuration uses five segmentation classes:

| ID | Class |
|---|---|
| 0 | Background |
| 1 | Water |
| 2 | Vegetation |
| 3 | Buildings |
| 4 | Bare land |

## Processed Data

The `processed/` directory is reserved for resized, normalized, and prepared training data.

## Dataset Recommendations

Use a properly licensed satellite segmentation dataset. Before training, verify:
- Image and mask alignment.
- Correct class-label mapping.
- Image and mask dimensions.
- Dataset usage and redistribution permissions.

**Important:** Do not upload large datasets or private satellite imagery directly to GitHub. Use an appropriate storage location and keep the repository lightweight.
