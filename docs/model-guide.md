
# AI Model Guide

## 1. Model Overview

The AI Satellite Intelligence System uses a U-Net convolutional neural network for semantic segmentation of satellite imagery.

Semantic segmentation assigns a land-cover class to each pixel.

## 2. U-Net Architecture

U-Net contains two main paths:

- **Encoder:** Extracts spatial features using convolutional layers and downsampling.
- **Decoder:** Reconstructs spatial resolution using upsampling and skip connections.

Skip connections preserve spatial information that helps produce detailed segmentation masks.

## 3. Supported Classes

The current configuration defines five classes:

| ID | Class |
|---|---|
| 0 | Background |
| 1 | Water |
| 2 | Vegetation |
| 3 | Buildings |
| 4 | Bare land |

## 4. Training Pipeline

The training pipeline consists of:

1. Load satellite images and segmentation masks.
2. Resize and normalize the images.
3. Convert images into PyTorch tensors.
4. Train the U-Net model.
5. Calculate validation loss.
6. Save the best model checkpoint.

## 5. Loss Function and Optimizer

The current training implementation uses:

- Cross-Entropy Loss
- Adam optimizer

These are baseline choices. Class imbalance and alternative loss functions should be evaluated using the selected dataset.

## 6. Model Evaluation

Evaluate the trained model using:

- Pixel accuracy
- Mean Intersection over Union (mIoU)
- Dice coefficient
- Per-class performance

Do not rely on overall accuracy alone, because it can hide poor performance on less frequent classes.

## 7. Model Limitations

- Predictions depend on the quality and diversity of training data.
- The model may not generalize to different sensors or geographic regions.
- No trained weights are included by default.
- Real-world use requires independent validation against reliable ground truth.

## 8. Future Improvements

- Data augmentation
- Class-weighted loss
- Spatially separated validation
- Multi-spectral input support
- Model benchmarking against alternative architectures
