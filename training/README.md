
# Model Training Guide

This directory contains the training and evaluation pipeline for the
AI Satellite Intelligence System.

## Directory Structure

```text
training/
├── __init__.py
├── dataset.py
├── train.py
├── evaluate.py
└── README.md
```

## Dataset Requirements

Place satellite images in:

`data/raw/images/`

Place their corresponding segmentation masks in:

`data/raw/masks/`

Each image must have a matching mask with the same filename stem.

Example:

```text
data/raw/
├── images/
│   ├── tile_001.png
│   └── tile_002.png
└── masks/
    ├── tile_001.png
    └── tile_002.png
```

## Mask Format

Masks must contain integer class IDs from `0` to `4`.

| Class ID | Class |
|---|---|
| 0 | Background |
| 1 | Water |
| 2 | Vegetation |
| 3 | Buildings |
| 4 | Bare land |

The mask must be a single-channel image, not a colored visualization.

## Install Development Dependencies

```bash
pip install -r requirements-dev.txt
```

## Train the Model

From the repository root, run:

```bash
python -m training.train
```

The best checkpoint is saved in:

`models/checkpoints/`

## Evaluate the Model

Evaluation utilities are available in `evaluate.py`.

A standalone evaluation command will be added after the evaluation interface is finalized.

## Important Notes

- Use correctly aligned images and masks.
- Keep image and mask dimensions consistent.
- Ensure mask values match the configured class IDs.
- Use a separate validation dataset when possible.
- Do not treat untrained model predictions as reliable satellite intelligence.
