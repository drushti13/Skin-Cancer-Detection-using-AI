from flask import Flask, request, jsonify
import os
import numpy as np
from tensorflow.keras.models import load_model
from PIL import Image
from flask_cors import CORS
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Constants
MODEL_PATH = "./models/skin_cancer_model.h5"
LABEL_ENCODER_PATH = "data/label_encoder.npy"

# Load model and label encoder
try:
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
    model = load_model(MODEL_PATH)
    logger.info("Model loaded successfully")

    label_encoder_classes = np.load(LABEL_ENCODER_PATH, allow_pickle=True)
    if isinstance(label_encoder_classes, np.ndarray):
        label_encoder_classes = {i: label for i, label in enumerate(label_encoder_classes)}
    logger.info(f"Label encoder loaded: {label_encoder_classes}")
except Exception as e:
    logger.error(f"Initialization error: {str(e)}")
    raise

# Cancerous classes mapping
CANCEROUS_CLASSES = {
    0: "akiec",  # Actinic keratoses
    1: "bcc",    # Basal cell carcinoma
    4: "mel"     # Melanoma
}

def preprocess_image(image):
    """Preprocess image for model prediction"""
    try:
        # Convert to RGB if not already
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Resize and normalize
        image = image.resize((224, 224))
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)
        return image
    except Exception as e:
        logger.error(f"Image preprocessing failed: {str(e)}")
        raise

@app.route("/predict", methods=["POST"])
def predict():
    """Handle image prediction requests"""
    try:
        # Validate request
        if "file" not in request.files:
            logger.warning("No file in request")
            return jsonify({
                "success": False,
                "error": "No file uploaded",
                "status": "error"
            }), 400

        file = request.files["file"]
        if file.filename == "":
            logger.warning("Empty filename")
            return jsonify({
                "success": False,
                "error": "No file selected",
                "status": "error"
            }), 400

        # Validate file extension
        allowed_extensions = {'jpg', 'jpeg', 'png'}
        if '.' not in file.filename or file.filename.split('.')[-1].lower() not in allowed_extensions:
            logger.warning(f"Invalid file type: {file.filename}")
            return jsonify({
                "success": False,
                "error": "Invalid file type. Only JPG, JPEG, PNG are allowed",
                "status": "error"
            }), 400

        # Process image
        logger.info(f"Processing file: {file.filename}")
        image = Image.open(file)
        preprocessed_image = preprocess_image(image)

        # Make prediction
        prediction = model.predict(preprocessed_image)
        predicted_class_index = int(np.argmax(prediction))  # Convert to native int
        predicted_class_label = str(label_encoder_classes[predicted_class_index])
        predicted_probability = float(np.max(prediction))  # Convert to native float

        # Prepare response
        is_cancerous = predicted_class_index in CANCEROUS_CLASSES
        response = {
            "success": True,
            "status": "Cancer Detected" if is_cancerous else "No Cancer",
            "type": CANCEROUS_CLASSES.get(predicted_class_index, predicted_class_label),
            "probability": predicted_probability,
            "confidence": f"{predicted_probability:.2%}",
            "class_index": predicted_class_index,
            "class_label": predicted_class_label
        }
        logger.info(f"Prediction result: {response}")

        return jsonify(response)

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({
            "success": False,
            "error": str(e),
            "status": "error"
        }), 500

@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "success": True,
        "status": "healthy",
        "message": "Skin cancer detection API is running"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)