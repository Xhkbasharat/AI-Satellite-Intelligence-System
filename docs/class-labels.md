
# Satellite Image Segmentation Class Labels

## Overview

The AI Satellite Intelligence System currently defines five semantic segmentation classes.

Each pixel in a segmentation mask must contain one of the configured class IDs.

## Class Mapping

| Class ID | Class Name | Description |
|---|---|---|
| 0 | Background | Unclassified or background pixels |
| 1 | Water | Rivers, lakes, reservoirs, and other water bodies |
| 2 | Vegetation | Forests, trees, grassland, and vegetation |
| 3 | Buildings | Buildings and built-up structures |
| 4 | Bare Land | Exposed soil, barren land, and non-vegetated ground |

## Mask Requirements

- Masks must be single-channel label images.
- Valid pixel values are integers from 0 through 4.
- Each mask must correspond to its satellite image.
- Image and mask dimensions must match before training.
- Do not use RGB visualization masks as training labels without converting them to class IDs.

## Example

A small segmentation mask could contain:

```python
import numpy as np

mask = np.array([
    [0, 0, 1, 1],
    [0, 2, 2, 1],
    [3, 3, 2, 4],
    [3, 3, 4, 4]
], dtype=np.uint8)
```

## Important Dataset Consideration

Different satellite datasets use different class definitions.

Before training:
1. Review the original dataset labels.
2. Create an explicit mapping to these five classes.
3. Convert original masks into the configured class IDs.
4. Verify the converted masks visually and programmatically.

Do not assume that class IDs from an external dataset already match this project.

## Future Extensions

The class system may later be expanded to include roads, agriculture, wetlands, snow, and other land-cover categories. Such changes require updating the model configuration, training data, and visualization logic together.
