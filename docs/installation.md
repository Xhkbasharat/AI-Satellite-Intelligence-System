
# Installation Guide

## Requirements

- Python 3.10 or newer
- Git
- pip
- Internet connection for dependency installation

## Step 1 — Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Satellite-Intelligence-System.git
cd AI-Satellite-Intelligence-System
```

Replace `YOUR_USERNAME` with your GitHub username.

## Step 2 — Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## Step 3 — Upgrade pip

```bash
python -m pip install --upgrade pip
```

## Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

For development:

```bash
pip install -r requirements-dev.txt
```

## Step 5 — Configure Environment

Copy `.env.example` to `.env` and configure your local settings.

Do not commit `.env` to GitHub.

Note: Environment-variable integration must be completed in the application configuration before all template settings take effect.

## Step 6 — Prepare Dataset

Create or populate the following directories:

```text
data/raw/images/
data/raw/masks/
```

Add matching satellite images and segmentation masks.

Follow `dataset-guide.md` for the required class mapping.

## Step 7 — Run Tests

```bash
pytest -v
```

## Step 8 — Start the Application

```bash
python app.py
```

Open:

http://127.0.0.1:5000

## Troubleshooting

### Dependency Installation Errors

Rasterio and GeoPandas may require compatible system libraries. Consult their official installation instructions.

### Missing Model Checkpoint

The segmentation workflow requires a compatible trained checkpoint. Train the model before relying on segmentation predictions.

### Dataset Errors

Check that every image has a corresponding mask and that mask values match the configured class IDs.

---

**Project Author:** Sheikh Basharat Akbar
