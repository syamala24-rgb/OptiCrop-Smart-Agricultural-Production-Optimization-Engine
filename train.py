import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# 1. Load the dataset
df = pd.read_csv('dataset/crop_recommendation.csv')

# 2. Separate features and target
X = df[['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']]
y = df['label']

# 3. Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 5. Check accuracy
accuracy = model.score(X_test, y_test) * 100
print(f"Model Training Complete! Accuracy: {accuracy:.2f}%")

# 6. Save model brain
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)
print("Saved model as model.pkl successfully!")