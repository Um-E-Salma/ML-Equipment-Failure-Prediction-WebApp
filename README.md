---
# ML-Equipment-Failure-Prediction-WebApp

This project is a Machine Learning (ML) model deployment that predicts whether a piece of equipment is likely to fail based on historical data related to its usage and maintenance. The model has been trained using Random Forest and is deployed in a web-based application, which allows users to input relevant details of the equipment and get a failure prediction.

## Project Overview

The prediction system is built using three datasets:
1. **Equipment List Dataset:** Contains details about the equipment, including its unique ID, specifications, type, added date, and manufacture year.
2. **Equipment Utilization Dataset:** Tracks the usage of equipment through columns such as equipment ID, job number (JONO), out date, out time, in date, and in time.
3. **Equipment Maintenance Dataset:** Contains information about equipment maintenance events, including maintenance ID, equipment ID, maintenance category, current odometer reading, valid months, valid mileage, maintenance comments, and the date of maintenance.

### Data Preprocessing

- The three datasets were merged on the basis of `equipment_ID` to create a unified view of equipment data.
- The `maintenance_category` column contains three unique values:
  - **Production:** This category was removed from the dataset.
  - **Preventive Maintenance:** Rows with this value were labeled as "Not_Failure" in a new `Failure` column.
  - **Maintenance:** Rows with this value were labeled as "Failure".
  
### Machine Learning Model

- A Random Forest model was trained on the processed data to predict whether equipment will fail or not.
- The trained model, along with the preprocessor and dimensionality reduction steps, were saved as `.pkl` files for later use.
  
### Web Application

A web-based UI was developed to allow users to input the following equipment information:
- **Equipment ID**
- **In Date**
- **Out Date**
- **In Time**
- **Out Time**
- **Equipment Type**
- **Manufacture Year**

Upon entering the details and clicking the "Predict" button, the system provides a prediction on whether the equipment is likely to fail.

## Installation and Setup

To run this project locally, follow these steps:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Um-E-Salma/ML-Equipment-Failure-Prediction-WebApp.git
   cd ML-Equipment-Failure-Prediction-WebApp

   ```

2. **Install Dependencies:**

   Install the required Python libraries by running:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the App:**

   Once dependencies are installed, start the application by running:

   ```bash
   python app.py
   ```

4. **Access the App:**

   Open your browser and go to `http://localhost:5000`. You should see a form where you can input the equipment data and get failure predictions.

## Files in the Repository

- `app.py`: The main application script that serves the web interface and handles predictions.
- `index.html`: The front-end form for user input.
- `random_forest_model.pkl`: The serialized Random Forest model.
- `preprocessor.pkl`: The data preprocessing steps for transforming input data.
- `dim_reduction.pkl`: Pickle file containing dimensionality reduction (if applied).
- `requirements.txt`: List of Python dependencies required to run the project.

## Further Improvements

This project has been designed based on client requirements, which limited the use of certain data features. However, there are several ways the prediction accuracy could be improved:

1. **Feature Expansion:** Additional features such as more detailed equipment specifications, operational environment data, and sensor readings could be incorporated to improve the model's understanding of equipment failure.
  
2. **Time-Series Analysis:** Since equipment usage involves temporal data (in and out times), time-series techniques such as LSTM (Long Short-Term Memory) or other recurrent neural networks could help capture the patterns in equipment usage more effectively.

3. **Maintenance History Analysis:** A more detailed analysis of past maintenance history could be included to better model how prior maintenance impacts future failures.

4. **Predictive Maintenance Strategy:** By combining the current prediction model with advanced predictive maintenance strategies, the system could offer optimized scheduling recommendations to minimize downtime and prevent future failures.

5. **Hyperparameter Tuning:** Further optimization of the Random Forest model could be done using grid search or random search to find the best combination of hyperparameters (e.g., tree depth, number of trees, etc.).

## Client Requirements

Please note that the prediction model was developed using the columns provided by the client. The model focuses on the essential features needed for equipment failure prediction according to the client's specifications. There may be opportunities to incorporate more advanced techniques and data features to enhance the prediction performance in future iterations.

---
