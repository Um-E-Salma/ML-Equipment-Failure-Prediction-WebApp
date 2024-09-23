from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA, TruncatedSVD
from joblib import load

app = Flask(__name__)

# Load the pre-trained model and PCA/SVD transformer
model = load('best_rf_model.pkl')  # Assuming the best model is saved
dim_reduction = load('dim_reduction.pkl')  # Load PCA or SVD
preprocessor = load('preprocessor.pkl')  # Load preprocessing pipeline

# Input column names
numerical_features = ['Utilization_Duration', 'Manufacture_Year']
categorical_features = ['EquiID', 'Specification', 'Equipment Type']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input from form
    input_data = request.form
    
    # Extract and format the data
    input_values = {
        'EquiID': request.form['EquiID'],
        'OutDate': request.form['OutDate'],
        'OutTime': request.form['OutTime'],
        'InDate': request.form['InDate'],
        'InTime': request.form['InTime'],
        'Equipment Type': request.form['Equipment_Type'],
        'Manufacture_Year': request.form['Manufacture_Year']
    }
    
    # Create a dataframe from the input data
    input_df = pd.DataFrame([input_values])

    # Preprocess input data
    preprocessed_input = preprocessor.transform(input_df)
    
    # Apply dimensionality reduction
    input_reduced = dim_reduction.transform(preprocessed_input)
    
    # Make prediction
    prediction = model.predict(input_reduced)

    # Map the prediction result to 'Failure' or 'Not Failure'
    prediction_label = 'Failure' if int(prediction[0]) == 1 else 'Not Failure'

    # Return the result as JSON
    return jsonify({'prediction': prediction_label})

if __name__ == "__main__":
    app.run(debug=True)
