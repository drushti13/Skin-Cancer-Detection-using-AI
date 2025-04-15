import numpy as np
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from PIL import Image

# Load preprocessed data
X_train = np.load('data/X_train.npy', allow_pickle=True)
y_train = np.load('data/y_train.npy', allow_pickle=True)

# Debug: Check data shapes and samples
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)
print("Sample X_train:", X_train[:5])
print("Sample y_train:", y_train[:5])

# Load the label encoder
label_encoder_classes = np.load('data/label_encoder.npy', allow_pickle=True)
num_classes = len(label_encoder_classes)

# Data generator
def data_generator(image_ids, labels, batch_size=32, target_size=(224, 224)):
    image_folder = 'E:/dataset/data/HAM10000_images/'
    num_samples = len(image_ids)
    while True:
        for offset in range(0, num_samples, batch_size):
            batch_ids = image_ids[offset:offset + batch_size]
            batch_labels = labels[offset:offset + batch_size]

            images = []
            valid_labels = []
            for image_id, label in zip(batch_ids, batch_labels):
                image_path = os.path.join(image_folder, image_id + '.jpg')
                if os.path.exists(image_path):
                    image = Image.open(image_path)
                    image = image.resize(target_size)
                    image = np.array(image) / 255.0  # Normalize pixel values
                    if image.shape == (224, 224, 3):  # Ensure correct shape
                        images.append(image)
                        valid_labels.append(label)
                else:
                    print(f"Warning: Image {image_id}.jpg not found. Skipping.")

            if len(images) > 0:  # Only yield non-empty batches
                yield np.array(images), np.array(valid_labels)

# Build the model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

# Train the model
batch_size = 32
epochs = 10

train_generator = data_generator(X_train, y_train, batch_size)
steps_per_epoch = len(X_train) // batch_size

history = model.fit(
    train_generator,
    steps_per_epoch=steps_per_epoch,
    epochs=epochs
)

# Save the trained model
os.makedirs('models', exist_ok=True)
model.save('models/skin_cancer_model.h5')