# scripts/evaluate_model.py
import numpy as np
from backend.train_model import data_generator
from tensorflow.keras.models import load_model

# Load preprocessed data
X_test = np.load('data/X_test.npy', allow_pickle=True)
y_test = np.load('data/y_test.npy', allow_pickle=True)

# Load the trained model
# Load the trained model
model = load_model('models/skin_cancer_model.h5')  # Ensure the correct path is used

# Evaluate the model
batch_size = 32
test_generator = data_generator(X_test, y_test, batch_size)
test_loss, test_accuracy = model.evaluate(test_generator, steps=len(X_test) // batch_size)
print(f"Test Accuracy: {test_accuracy:.4f}")