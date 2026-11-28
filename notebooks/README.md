
# Research and Experiment Notebooks

This directory is reserved for Jupyter notebooks used during the development of the AI Satellite Intelligence System.

## Planned Notebooks

| Notebook | Purpose |
|---|---|
| `01_data_exploration.ipynb` | Explore satellite images and dataset statistics |
| `02_image_preprocessing.ipynb` | Test resizing and normalization |
| `03_segmentation_visualization.ipynb` | Visualize land-cover masks |
| `04_model_training.ipynb` | Experiment with U-Net training |
| `05_model_evaluation.ipynb` | Analyze segmentation metrics |
| `06_change_detection.ipynb` | Explore image comparison methods |
| `07_geospatial_analysis.ipynb` | Examine geographic metadata and area calculations |

## Install Jupyter

```bash
pip install jupyterlab
```

## Launch JupyterLab

From the repository root:

```bash
jupyter lab
```

## Notebook Guidelines

- Keep experiments reproducible.
- Document dataset sources and licenses.
- Set random seeds where appropriate.
- Avoid storing large datasets inside notebooks.
- Do not commit private satellite imagery or model checkpoints.
- Separate exploratory experiments from production code.

## Current Status

The directory currently contains documentation only. The experiment notebooks will be added as the project develops.
