import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

# Correct paths
MODEL_PATH = "E:/dataset/models/skin_cancer_model.h5"
IMAGE_PATH = r"E:\dataset\data\HAM10000_images\ISIC_0024332.jpg"
print(f"Looking for model at: {MODEL_PATH}")
print(f"Looking for image at: {IMAGE_PATH}")

# Load the model
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")
model = load_model(MODEL_PATH)

# Define cancerous classes
CANCEROUS_CLASSES = {
    0: "akiec",  # Actinic keratoses and intraepithelial carcinoma (pre-cancerous or early cancer)
    1: "bcc",   # Basal cell carcinoma (a type of skin cancer)
    4: "mel"    # Melanoma (a serious type of skin cancer)
}

# Load the label encoder
label_encoder_classes = np.load('data/label_encoder.npy', allow_pickle=True)

def preprocess_image(image_path):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    image = Image.open(image_path).resize((224, 224))  # Resize to match model input
    image = np.array(image) / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Load and preprocess the image
preprocessed_image = preprocess_image(IMAGE_PATH)

# Make a prediction
prediction = model.predict(preprocessed_image)
predicted_class_index = np.argmax(prediction)
predicted_class_label = label_encoder_classes[predicted_class_index]
predicted_probability = np.max(prediction)

# Check if the predicted class is cancerous
if predicted_class_index in CANCEROUS_CLASSES:
    cancer_type = CANCEROUS_CLASSES[predicted_class_index]
    print(f"Prediction: Cancer ({cancer_type}) with probability {predicted_probability:.2%}")
else:
    print(f"Prediction: Not Cancer ({predicted_class_label}) with probability {predicted_probability:.2%}")