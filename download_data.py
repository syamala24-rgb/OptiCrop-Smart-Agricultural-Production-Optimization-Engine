import os
import pandas as pd

# Define the dataset path and URL
folder_path = "dataset"
file_path = os.path.join(folder_path, "crop_recommendation.csv")
data_url = "https://raw.githubusercontent.com/Gladiator07/Harvestify/master/Data-processed/crop_recommendation.csv"

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

print("Downloading dataset...")
try:
    # Read directly from raw github link and save locally
    df = pd.read_csv(data_url)
    df.to_csv(file_path, index=False)
    print(f"Success! File saved precisely to: {file_path}")
    print(df.head())  # Preview data columns
except Exception as e:
    print(f"An error occurred during download: {e}")