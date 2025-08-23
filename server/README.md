# ⏩ FastAPI Backend: Airbnb Price Prediction API

This folder contains the **FastAPI app** (`backend.py`) serving the trained Airbnb price prediction model.

---

## 📦 Contents

- `backend.py`: Main backend script. Handles loading the model, data scaling, and exposes a `/predict` POST endpoint for inference.

---

## 🚀 How to Run

1. Clone the project and create the environment as per the main [README](../README.md).
2. Make sure the serialized model and scaler (`ridge_model_and_scaler.pkl`) are available in `models/`.
3. Start the API server from the project root:

    ```bash
    uvicorn server.backend:app --reload
    # OR, if enabled:
    python server/backend.py
    ```

4. Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger UI.

5. **Demo (web):** The deployed backend is available at [https://airbnb-fastapi.onrender.com
](https://airbnb-fastapi.onrender.com)

---

## 💡 Notes

- The `/predict` endpoint expects a JSON payload matching the required input fields.
- The backend must be running for the Streamlit frontend to connect and provide predictions.
- Update the model/scaler if you retrain or improve the pipeline.
