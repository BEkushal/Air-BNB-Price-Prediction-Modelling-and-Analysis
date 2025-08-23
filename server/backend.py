from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import numpy as np

# Load the model and scaler
with open('models/ridge_model_and_scaler.pkl', 'rb') as f:
    best_model, scaler = pickle.load(f)
    

# app bio
app = FastAPI(
    title="Airbnb Price Prediction API",
    description="API for predicting Airbnb rental prices from structured features",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or specify your Streamlit app domain for more security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the expected input features (customize fields as per your encoded model's features)
class PredictRequest(BaseModel):
    accommodates: float
    bathrooms: float
    cleaning_fee: float
    instant_bookable: int
    review_scores_rating: float
    bedrooms: float
    beds: float
    room_type_Private_room: int = 0
    room_type_Shared_room: int = 0
    cancellation_policy_moderate: int = 0
    cancellation_policy_strict: int = 0
    
@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>Airbnb Price Prediction API</title>
            <style>
                body { font-family: Arial, sans-serif; background-color: #f9fafb; color: #233; padding: 2em; }
                .notice { color: #0a8f08; font-weight: bold; }
                a { color: #0a8f08; text-decoration: none; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>🏡 Airbnb Price Prediction API</h1>
            <p class="notice">
                <strong>👤 Are you a user or recruiter?</strong><br>
                Please visit <a href='/docs'>/docs</a> <b>instead of /predict</b> for a full interactive demo and instructions.<br>
                <br>
                <strong>🌐 Or, use the web user interface here:</strong>
                <a href='https://airbnb-streamlit.onrender.com' target='_blank'>[Launch Airbnb Price Prediction App]</a>
                <br><br>
                <span style="color: #FF5733;">
                If you see a browser security warning, it's only because this is a newly deployed API.<br>
                It is safe to proceed if you came here from my portfolio or resume.
                </span>
                <br><br>
                (For more help, see the readme of <a href="https://github.com/BEkushal/Air-BNB-Price-Prediction-Modelling-and-Analysis.git" target="_blank">project README</a>)
            </p>
        </body>
    </html>
    """

@app.post("/predict")
def predict_price(req: PredictRequest):
    # Convert the input data to a DataFrame row or array
    data = np.array([[
        req.accommodates,
        req.bathrooms,
        req.cleaning_fee,
        req.instant_bookable,
        req.review_scores_rating,
        req.bedrooms,
        req.beds,
        req.room_type_Private_room,
        req.room_type_Shared_room,
        req.cancellation_policy_moderate,
        req.cancellation_policy_strict
    ]])

    data_scaled = scaler.transform(data)
    log_price_pred = best_model.predict(data_scaled)[0]
    price_pred = np.exp(log_price_pred)  # Inverse of log if you want actual price

    return {
        "log_price_prediction": round(float(log_price_pred), 2),
        "predicted_price": round(float(price_pred), 2)  
    }

# To run:
if __name__ == "__main__":
    import uvicorn
     # Adjust module path as needed for your project structure
    uvicorn.run("server.backend:app", host="127.0.0.1", port=8000, reload=True)