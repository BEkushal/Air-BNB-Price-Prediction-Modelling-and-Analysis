# 🎛️ Streamlit Frontend: Airbnb Price Prediction

This folder contains the **Streamlit UI** for the Airbnb Price Prediction project.  
Users can interactively enter listing features and get instant rental price predictions via the deployed ML model (served by the FastAPI backend).

---

## 📦 Contents

- `application.py`: Main Streamlit app script.
- (Add more files if you customize further.)

---

## 🚀 How to Run

> **Requires:** backend server running (locally or remotely).

1. Clone the project and set up the environment as described in the main project [README](../README.md).
2. Ensure the FastAPI backend is running (locally or via Render).
3. In the project root, launch the Streamlit app with:

    ```bash
    streamlit run app/application.py
    ```

4. Go to [http://localhost:8501](http://localhost:8501) in your browser.

5. **Demo (web):** You can use the deployed app [here](https://airbnb-streamlit.onrender.com).

---

## 💡 Notes

- The Streamlit interface sends user inputs to the backend `/predict` endpoint and displays results.
- Update the API URL (`API_URL` in `application.py`) if running the backend on a remote host or a different port.
