
# Deployment Guide

## 1. Prerequisites

Install the following:

- Python 3.10 or newer
- Git
- pip
- A computer with sufficient RAM and storage

A compatible NVIDIA GPU is recommended for faster model training but is not required for basic CPU inference.

## 2. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-Satellite-Intelligence-System.git
cd AI-Satellite-Intelligence-System
```

Replace `YOUR_USERNAME` with your GitHub username.

## 3. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux and macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

For development and testing tools:

```bash
pip install -r requirements-dev.txt
```

Note: Rasterio and GeoPandas may require compatible system libraries or platform-specific installation instructions.

## 5. Configure the Project

Review `config.py`.

Set any required environment variables, including a secure Flask secret key.

Do not commit private credentials or production secrets to GitHub.

## 6. Prepare the Dataset

Place satellite images in:

`data/raw/images/`

Place matching segmentation masks in:

`data/raw/masks/`

Follow the instructions in `dataset-guide.md`.

## 7. Train the Model

From the repository root:

```bash
python -m training.train
```

Training requires a suitable labeled dataset.

## 8. Start the Web Application

```bash
python app.py
```

Open this address in your browser:

`http://127.0.0.1:5000`

## 9. Run Tests

```bash
pytest -v
```

## 10. Production Deployment

Before exposing the application publicly:

- Disable Flask debug mode.
- Use a production WSGI server.
- Configure HTTPS.
- Add authentication and upload controls.
- Restrict upload file sizes and types.
- Protect uploaded imagery and generated results.
- Validate model predictions before operational use.

## Important

This project is currently under development. Verify dependencies, model weights, and application behavior before deploying it for real-world use.
