
# AI Satellite Intelligence Experiment Plan

## 1. Objective

Evaluate the performance and reliability of the U-Net model for satellite image land-cover segmentation.

## 2. Research Questions

1. How accurately can the model classify different land-cover types?
2. Which classes are most difficult to segment?
3. How does image preprocessing affect model performance?
4. Does data augmentation improve generalization?
5. How well does the model perform on geographically separate imagery?

## 3. Experimental Dataset

The dataset must contain:
- Satellite images
- Corresponding segmentation masks
- Consistent class-label mapping
- Training and validation partitions

Record the dataset source, license, sensor, geographic coverage, and acquisition dates.

## 4. Baseline Experiment

Train the initial U-Net model using the existing configuration.

Record:
- Training loss
- Validation loss
- Pixel accuracy
- Mean Intersection over Union
- Dice coefficient
- Per-class IoU

## 5. Proposed Experiments

| Experiment | Investigation |
|---|---|
| EXP-01 | Baseline U-Net performance |
| EXP-02 | Effect of data augmentation |
| EXP-03 | Effect of learning rate |
| EXP-04 | Class imbalance handling |
| EXP-05 | Alternative loss functions |
| EXP-06 | Performance across geographic regions |

## 6. Evaluation Metrics

### Pixel Accuracy

Measures the proportion of correctly classified pixels.

### Intersection over Union

Measures overlap between predicted and ground-truth class regions.

### Dice Coefficient

Measures similarity between predicted and reference segmentation masks.

Report metrics per class as well as their averages.

## 7. Validation Strategy

- Keep training and validation data separate.
- Prefer geographic separation to reduce spatial leakage.
- Avoid evaluating only on training images.
- Inspect predictions visually.
- Document dataset limitations.

## 8. Results Recording

For every experiment, record:

- Experiment ID
- Dataset version
- Model configuration
- Hyperparameters
- Training duration
- Evaluation metrics
- Observations
- Limitations

## 9. Scientific Integrity

Do not report invented performance numbers. Publish only metrics obtained from actual experiments with clearly described evaluation procedures.

## 10. Current Status

Experiments are planned but have not yet been conducted on a verified dataset.
