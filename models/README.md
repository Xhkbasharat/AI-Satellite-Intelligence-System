
# Model Storage

This directory stores model checkpoints and trained weights for the AI Satellite Intelligence System.

## Directory Structure

```text
models/
├── README.md
├── checkpoints/
└── trained/
```

## Checkpoints

The `checkpoints/` directory stores intermediate training states.

These may include:
- Model parameters
- Optimizer state
- Training epoch
- Validation loss

## Trained Models

The `trained/` directory stores final model weights used for inference.

## Model Requirements

Before using a model:

1. Confirm it was trained with the expected number of classes.
2. Confirm its architecture matches `src/segmentation.py`.
3. Verify that the checkpoint loads successfully.
4. Evaluate it on held-out satellite imagery.

## Important

No trained model weights are included yet. The application should not be considered reliable for real-world satellite analysis until a suitable model has been trained and evaluated.
