
# Frequently Asked Questions (FAQ)

## 1. What is the AI Satellite Intelligence System?

It is a Python-based project that uses computer vision, deep learning, and geospatial processing to analyze satellite imagery.

## 2. What can the system analyze?

The project is designed to support:
- Water bodies
- Vegetation
- Buildings
- Bare land
- Pixel-level image differences

## 3. Does the project include a trained AI model?

No. The repository includes a U-Net architecture and training pipeline, but a compatible trained checkpoint must be created separately.

## 4. Which programming language is used?

Python is the primary programming language. The dashboard uses HTML, CSS, and JavaScript.

## 5. Which image formats are supported?

The preprocessing module supports PNG, JPG, JPEG, and GeoTIFF formats.

Actual support depends on the installed image-processing libraries and the properties of each file.

## 6. Do I need a GPU?

No. Basic processing can run on a CPU, although GPU acceleration is recommended for model training.

## 7. Where should I place training images?

Place satellite images in:

`data/raw/images/`

Place corresponding segmentation masks in:

`data/raw/masks/`

## 8. How do I start the dashboard?

Install dependencies and run:

```bash
python app.py
```

Then open:

`http://127.0.0.1:5000`

## 9. Why are model predictions inaccurate?

Possible reasons include:
- Missing or untrained model weights
- Incorrect class-label mapping
- Insufficient training data
- Different satellite sensor characteristics
- Poor image quality

## 10. Is change detection scientifically validated?

Not yet. The current implementation uses pixel-level differences as a baseline. Reliable change analysis requires image co-registration, comparable acquisition conditions, and independent validation.

## 11. Can I use my own satellite dataset?

Yes, provided the imagery and labels are compatible with the project's preprocessing and class-label conventions.

## 12. Is this project production-ready?

No. It is a research and development project. Security improvements, dataset preparation, model training, and end-to-end validation are still required.

## 13. Who developed this project?

**Sheikh Basharat Akbar**
