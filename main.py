from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import joblib

app = FastAPI()

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
melbourne_model = DecisionTreeRegressor(random_state=1)

melbourne_data = pd.read_csv('data/melb_data.csv')
X = melbourne_data[melbourne_features]
y = melbourne_data.Price
melbourne_model.fit(X, y)

class HouseFeatures(BaseModel):
    Rooms: int
    Bathroom: int
    Landsize: float
    Lattitude: float
    Longtitude: float


@app.get('/')
async def home():
    return {
        "Message":"Hi,This is our first ML Model."
    }

@app.post("/predict/")
async def predict_price(features: HouseFeatures):
    # Convert the input data to the format required by the model
    input_data = [[
        features.Rooms,
        features.Bathroom,
        features.Landsize,
        features.Lattitude,
        features.Longtitude
    ]]

    # Make a prediction
    prediction = melbourne_model.predict(input_data)

    # Return the prediction as a JSON response
    return f"predicted_price: {prediction[0]:,.2f} USD"

# You can run the app using the command below
# uvicorn filename:app --reload
