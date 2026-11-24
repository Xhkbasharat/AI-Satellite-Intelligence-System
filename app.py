
import os
import uuid

import numpy as np

from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash
)
from werkzeug.utils import secure_filename

from config import Config

from src.preprocessing import (
    preprocess_satellite_image
)

from src.segmentation import (
    load_segmentation_model,
    predict_segmentation
)

from src.change_detection import (
    compare_satellite_images
)

from src.visualization import (
    create_segmentation_visualization,
    create_overlay,
    save_visualization,
    create_class_distribution
)

from src.geospatial import (
    get_geographic_summary
)


app = Flask(__name__)
app.config.from_object(Config)

UPLOAD_DIR = os.path.join(
    app.static_folder,
    "uploads"
)

RESULT_DIR = os.path.join(
    app.static_folder,
    "results"
)

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULT_DIR, exist_ok=True)


# --------------------------------------------------
# Helper functions
# --------------------------------------------------

def allowed_file(filename):
    extension = os.path.splitext(filename)[1].lower()

    return extension in Config.ALLOWED_EXTENSIONS


def save_uploaded_file(file):
    """
    Validate and save an uploaded satellite image.
    """

    if not file or not file.filename:
        raise ValueError("Please select an image.")

    if not allowed_file(file.filename):
        raise ValueError(
            "Unsupported file format."
        )

    original_name = secure_filename(
        file.filename
    )

    extension = os.path.splitext(
        original_name
    )[1].lower()

    filename = f"{uuid.uuid4().hex}{extension}"

    filepath = os.path.join(
        UPLOAD_DIR,
        filename
    )

    file.save(filepath)

    return filename, filepath


def get_model_path():
    return os.path.join(
        Config.CHECKPOINT_DIR,
        "best_unet.pth"
    )


def get_model():
    """
    Load the trained model only when weights exist.
    """

    model_path = get_model_path()

    if not os.path.isfile(model_path):
        return None

    return load_segmentation_model(
        model_path=model_path
    )


# --------------------------------------------------
# Home page
# --------------------------------------------------

@app.route("/")
def home():

    return render_template(
        "index.html",
        app_name=Config.APP_NAME,
        app_version=Config.APP_VERSION
    )


# --------------------------------------------------
# Satellite image upload and segmentation
# --------------------------------------------------

@app.route(
    "/analyze",
    methods=["POST"]
)
def analyze():

    filepath = None

    try:

        uploaded_file = request.files.get(
            "satellite_image"
        )

        filename, filepath = save_uploaded_file(
            uploaded_file
        )

        image = preprocess_satellite_image(
            filepath
        )

        model = get_model()

        if model is None:

            flash(
                "Image uploaded successfully, "
                "but the trained AI model is not "
                "available yet. Train the model first.",
                "warning"
            )

            return redirect(url_for("home"))

        # Prepare model input
        model_input = np.transpose(
            image,
            (2, 0, 1)
        )

        mask = predict_segmentation(
            model,
            model_input
        )

        # Generate visualization
        original_image = np.clip(
            image * 255,
            0,
            255
        ).astype(np.uint8)

        overlay = create_overlay(
            original_image,
            mask
        )

        result_name = (
            f"{uuid.uuid4().hex}.png"
        )

        result_path = os.path.join(
            RESULT_DIR,
            result_name
        )

        save_visualization(
            overlay,
            result_path,
            title="Satellite Land Cover Analysis"
        )

        distribution = create_class_distribution(
            mask
        )

        return render_template(
            "index.html",
            app_name=Config.APP_NAME,
            app_version=Config.APP_VERSION,
            original_image=url_for(
                "static",
                filename=f"uploads/{filename}"
            ),
            result_image=url_for(
                "static",
                filename=f"results/{result_name}"
            ),
            distribution=distribution
        )

    except Exception as error:

        app.logger.exception(
            "Satellite image analysis failed."
        )

        flash(
            f"Analysis failed: {error}",
            "danger"
        )

        return redirect(url_for("home"))


# --------------------------------------------------
# Satellite image change detection
# --------------------------------------------------

@app.route(
    "/change-detection",
    methods=["POST"]
)
def change_detection():

    try:

        first_file = request.files.get(
            "first_image"
        )

        second_file = request.files.get(
            "second_image"
        )

        _, first_path = save_uploaded_file(
            first_file
        )

        _, second_path = save_uploaded_file(
            second_file
        )

        first_image = preprocess_satellite_image(
            first_path
        )

        second_image = preprocess_satellite_image(
            second_path
        )

        results = compare_satellite_images(
            first_image,
            second_image
        )

        visualization_name = (
            f"{uuid.uuid4().hex}.png"
        )

        visualization_path = os.path.join(
            RESULT_DIR,
            visualization_name
        )

        save_visualization(
            results["visualization"],
            visualization_path,
            title="Satellite Change Detection"
        )

        return render_template(
            "index.html",
            app_name=Config.APP_NAME,
            app_version=Config.APP_VERSION,
            change_image=url_for(
                "static",
                filename=f"results/{visualization_name}"
            ),
            change_percentage=results[
                "change_percentage"
            ]
        )

    except Exception as error:

        app.logger.exception(
            "Change detection failed."
        )

        flash(
            f"Change detection failed: {error}",
            "danger"
        )

        return redirect(url_for("home"))


# --------------------------------------------------
# Application startup
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=Config.DEBUG
    )
