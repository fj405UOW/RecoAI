# training/train.py

import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib
import os

# Path to your training data (change "new_data.csv" if necessary)
data_path = os.path.join(os.path.dirname(__file__), "melb_data.csv")
data = pd.read_csv(data_path)

# Define features and target
features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = data[features]
y = data["Price"]

# Start an MLflow run
with mlflow.start_run():
    # Train the model
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X, y)
    
    # Evaluate model performance (R² score)
    score = model.score(X, y)
    
    # Log parameters and metrics
    mlflow.log_param("model_type", "DecisionTreeRegressor")
    mlflow.log_metric("r2_score", score)
    
    # Save the model locally
    model_save_path = os.path.join(os.path.dirname(__file__), "model.pkl")
    joblib.dump(model, model_save_path)
    
    # Log the model in MLflow
    mlflow.sklearn.log_model(model, "model")
    
    print(f"Model trained with R² score: {score:.4f}. Model saved at {model_save_path}.")
