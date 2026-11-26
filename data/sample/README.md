
# Sample Satellite Data

This directory is reserved for small sample satellite images and segmentation masks.

## Purpose

Sample data can be used to:

- Test image preprocessing.
- Check segmentation visualization.
- Test image upload functionality.
- Verify change-detection workflows.

## Recommended Structure

```text
data/sample/
├── README.md
├── images/
└── masks/
```

## Data Guidelines

- Use small images to keep the repository lightweight.
- Ensure every sample image has a corresponding mask when testing segmentation.
- Use mask class IDs from `0` to `4`.
- Confirm that sample data is licensed for redistribution.

## Important

No real satellite dataset is included yet. Add suitable sample imagery before attempting end-to-end analysis.
