import os
import pickle
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Make sure there are TWO underscores before and after file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'templates', 'model.pkl')

# Load the trained ML model brain
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            features = [
                float(request.form['N']),
                float(request.form['P']),
                float(request.form['K']),
                float(request.form['temperature']),
                float(request.form['humidity']),
                float(request.form['ph']),
                float(request.form['rainfall'])
            ]
            final_features = [np.array(features)]
            prediction_output = model.predict(final_features)
            return render_template('index.html', prediction=prediction_output[0])
        except Exception as e:
            return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)