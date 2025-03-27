# serving/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib
import os
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Configure CORS (adjust the allowed origins as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use a list of allowed origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define model features
melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']

# For this example, we are training the model at startup.
# In a production scenario, you would load a pre-trained model (e.g., from MLflow or a file).
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "melb_data.csv")
print(data_path)
melbourne_data = pd.read_csv(data_path)
X = melbourne_data[melbourne_features]
y = melbourne_data["Price"]
melbourne_model = DecisionTreeRegressor(random_state=1)
melbourne_model.fit(X, y)

class HouseFeatures(BaseModel):
    Rooms: int
    Bathroom: int
    Landsize: float
    Lattitude: float
    Longtitude: float

@app.get("/")
async def home():
    return {"Message": "Hi, This is our first ML Model."}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/predict/")
async def predict_price(features: HouseFeatures):
    input_data = [[
        features.Rooms,
        features.Bathroom,
        features.Landsize,
        features.Lattitude,
        features.Longtitude
    ]]
    prediction = melbourne_model.predict(input_data)
    return {"predicted_price": f"{prediction[0]:,.2f} USD"}
