# scripts/preprocess.py
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load the CSV file
metadata_path = 'data/HAM10000_metadata.csv'
metadata = pd.read_csv(metadata_path)

# Encode the diagnosis labels into numerical values
label_encoder = LabelEncoder()
metadata['label'] = label_encoder.fit_transform(metadata['dx'])

# Split the data into training and testing sets
X = metadata['image_id']  # Image IDs
y = metadata['label']     # Encoded labels
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Save the splits for later use
np.save('data/X_train.npy', X_train)
np.save('data/X_test.npy', X_test)
np.save('data/y_train.npy', y_train)
np.save('data/y_test.npy', y_test)

# Save the label encoder for later use
np.save('data/label_encoder.npy', label_encoder.classes_)