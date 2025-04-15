# scripts/load_and_explore.py
import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
metadata_path = 'data/HAM10000_metadata.csv'
metadata = pd.read_csv(metadata_path)

# Display the first few rows
print(metadata.head())

# Check the distribution of diagnoses
print(metadata['dx'].value_counts())

# Plot the distribution of diagnoses
metadata['dx'].value_counts().plot(kind='bar')
plt.title('Distribution of Diagnoses')
plt.xlabel('Diagnosis')
plt.ylabel('Count')
plt.show()