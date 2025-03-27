import os
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.tree import DecisionTreeRegressor
import joblib

app = FastAPI()

# # Compute the path: move up one directory from 'serving', then into 'data'
# data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "melb_data.csv")
# #print("Computed data_path:", data_path)  # This will print the computed path

# # Now, load the data
# melbourne_data = pd.read_csv(data_path)

# melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
# melbourne_model = DecisionTreeRegressor(random_state=1)
# X = melbourne_data[melbourne_features]
# y = melbourne_data["Price"]
# melbourne_model.fit(X, y)

# class HouseFeatures(BaseModel):
#     Rooms: int
#     Bathroom: int
#     Landsize: float
#     Lattitude: float
#     Longtitude: float

@app.get("/")
async def home():
    return {"Message": "Hi, This is our first ML Model."}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# @app.post("/predict/")
# async def predict_price(features: HouseFeatures):
#     input_data = [[
#         features.Rooms,
#         features.Bathroom,
#         features.Landsize,
#         features.Lattitude,
#         features.Longtitude
#     ]]
#     prediction = melbourne_model.predict(input_data)
#     return {"predicted_price": f"{prediction[0]:,.2f} USD"}
