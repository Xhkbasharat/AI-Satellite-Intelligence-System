
import os


class Config:
    # Project information
    APP_NAME = "AI Satellite Intelligence System"
    APP_VERSION = "1.0.0"

    # Flask configuration
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "change-this-secret-key-before-deployment"
    )

    DEBUG = os.environ.get(
        "FLASK_DEBUG", "False"
    ).lower() == "true"

    # Project directories
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    DATA_DIR = os.path.join(BASE_DIR, "data")
    RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
    PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
    SAMPLE_DATA_DIR = os.path.join(DATA_DIR, "sample")

    MODEL_DIR = os.path.join(BASE_DIR, "models")
    CHECKPOINT_DIR = os.path.join(MODEL_DIR, "checkpoints")
    TRAINED_MODEL_DIR = os.path.join(MODEL_DIR, "trained")

    # Image processing configuration
    IMAGE_SIZE = 256
    IMAGE_CHANNELS = 3

    # Model configuration
    NUM_CLASSES = 5
    BATCH_SIZE = 8
    LEARNING_RATE = 0.001
    EPOCHS = 30

    # Supported satellite image formats
    ALLOWED_EXTENSIONS = {
        ".tif",
        ".tiff",
        ".png",
        ".jpg",
        ".jpeg"
    }

    # Maximum upload size: 50 MB
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024


# Create required directories
for directory in [
    Config.RAW_DATA_DIR,
    Config.PROCESSED_DATA_DIR,
    Config.SAMPLE_DATA_DIR,
    Config.CHECKPOINT_DIR,
    Config.TRAINED_MODEL_DIR
]:
    os.makedirs(directory, exist_ok=True)
