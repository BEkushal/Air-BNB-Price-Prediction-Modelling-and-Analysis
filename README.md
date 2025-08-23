# 🏡 Airbnb Price Prediction 🚀

> **End-to-end Machine Learning App: EDA • Modelling • FastAPI Backend • Streamlit Frontend • Cloud Deployment**

---

## 📸 **Project Demo**

![Web Application Demo](https://github.com/user-attachments/assets/bbda46be-9f78-45c1-b962-7d659464e608)

---

## 🏗️ **Project Architecture**


<img width="1047" height="792" alt="Project-Architecture drawio-img" src="https://github.com/user-attachments/assets/9946b643-eaa0-4e92-8bee-4ce46bdb1d7f" />

---


## 📝 **Project Overview**

This project demonstrates a real-world, production-ready approach to **predicting Airbnb rental prices** using data (locally available in this case), advanced preprocessing, robust linear modeling (including Ridge/Lasso), and deploying a fully functional web app using **FastAPI** and **Streamlit**.

**Key Features:**
- 📊 Data cleaning, EDA, and feature engineering
- 🔍 Outlier handling (capping/winsorization & trimming)
- 🤖 Multiple regression models with result comparison (exported as csv as well)
- 🗂️ Model export with `pickle`
- ⏩ FastAPI backend for predictions
- 🎛️ Streamlit user interface for interactive, live demo
- 🌐 Free cloud deployment (Render.com)
- 🧑‍💻 Modular, production-quality codebase structure
- 🧩 Project planning and task tracking managed using Notion workspace

---

## 📋 Project Management & Tracking (Notion)

Project phases, tasks, and progress for this work were planned and tracked in Notion, ensuring transparency, modularity, and agile project flow.

> **Access the full Notion board for this project here:**
> [View Airbnb ML Project Tracker in Notion](https://www.notion.so/Air-BNB-Price-Predictions-Modelling-Regression-2583e2a31005802a85ece9627a2d5b32?source=copy_link)

This Notion workspace includes:
- Phase breakdown (requirements, EDA, modeling, API/app, deployment, etc.)
- Task checklists
- Progress tracking (great for self-organization or team work!)

## ⚡ **Live Demo**

- **Try the app here:** [Web Application](https://airbnb-streamlit.onrender.com)  
- **API endpoint:** [https://airbnb-fastapi.onrender.com/predict](https://airbnb-fastapi.onrender.com/predict)
- *You can use the web interface or send POST requests for predictions!*

---

## 🎬 **Quick-Start (Local Demo)**

**1️⃣ Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/airbnb-price-prediction-ml.git
cd airbnb-price-prediction-ml
```

**2️⃣ Set Up Environment**

```
python -m venv venv
source venv/bin/activate           # or venv\Scripts\activate for Windows
pip install -r requirements.txt
```

**3️⃣ (Optional) Download Data**
  -  If sample data is not included, add the required file to ``/data``.

**4️⃣ Start the FastAPI Backend**

```
uvicorn server.backend:app --reload
# or, if you added if __name__ == "__main__": block:
python server/backend.py
# API docs: http://localhost:8000/docs
```

**5️⃣ Start the Streamlit Frontend**

```
streamlit run app/application.py
# App launches at http://localhost:8501
```

---

## **📂 Project Structure**

```

├── app/                # Streamlit frontend
│   └── application.py
├── server/             # FastAPI backend
│   └── backend.py
├── models/             # Trained and serialized models/scalers
├── data/               # (Optional) Input data for local demo
├── model_results/      # EDA/model results and exports
├── notebooks/          # Jupyter notebooks for EDA and experimentation
├── requirements.txt    # Clean, minimal environment file
├── .gitignore
└── README.md
```

---

## **🧠 Modelling Workflow Highlights**

1. **Exploratory Data Analysis**:
     -  Detailed investigation of distributions and relationships, highlighting outliers and missingness.
    
2. **Data Cleaning & Feature Engineering**:
     -  Median/mode and KNN-based imputation for missing data
     -  Outlier handling: both capping (percentile/quantile) and target trimming
     -  One-hot encoding for robust categorical handling (get_dummies)
      
3. **Modelling**:
     -  Compared Linear, Ridge, and Lasso Regression
     -  Cross-validated with multiple cleaned/imputed/outlier-handled datasets
     -  Model and results exported for reproducibility

4. **API & UI**:
     -  FastAPI serves predictions for any valid input feature vector
     -  Streamlit UI enables instant, user-friendly inputs and displays results
     -  Both deployable for public access via free Render hosting

---

## **🌟 The Importance of Enriched Data for Predictive Modeling**

The model’s accuracy is inherently limited by the available features.
*Real-world production models benefit significantly from richer, more descriptive data, such as:*

  -  Geographic location (neighborhood, coordinates, proximity to attractions)
  -  Seasonal & temporal trends (event proximity, booking window, date features)
  -  Listing & host details (amenities, superhost status, review volume/trends)
  -  Market signals (competitor pricing, occupancy rates)
  -  Text/image-derived insights (descriptions, photos)
    
With more diverse and targeted features, models capture deeper value and make far more accurate, business-relevant predictions! 

---

## **🚦 How to Use (Web Version)**

1.  **Visit the live app:**
    -  [Click Here](https://airbnb-streamlit.onrender.com)
3. **Enter listing features** (accommodates, room/bath count, etc.)
4. **View predicted price** for your Airbnb listing instantly!
    -  API endpoint available for programmatic access.
  
---

## **🧑‍💻 How to Use (Local Version)**

(see Quick-Start above)

---

## **✍️ Customization & Extensions**

-  Easily swap in other regression/classification models
-  Expand backend to handle more complex business logic
-  Add user authentication, multi-step forms, or charts via Streamlit widgets
-  Deploy to other platforms (Fly.io, Railway, Azure, etc.)
-  Add Docker and GitHub Actions for even smoother deployment

---

## **🖼️ Visualizations & Insights**

-  **Univariate Analysis**

 <img width="713" height="393" alt="image" src="https://github.com/user-attachments/assets/377d7402-ff7b-41a5-95f3-0cb18cb3f920" />
 
 <img width="713" height="393" alt="image" src="https://github.com/user-attachments/assets/5acddbe2-2aac-4693-9cf1-eda99329e24e" />
 
 <img width="713" height="393" alt="image" src="https://github.com/user-attachments/assets/06cfb360-ae85-4ef1-88fa-078dfacffc0e" />
 
 <img width="713" height="393" alt="image" src="https://github.com/user-attachments/assets/0370d536-aed3-451f-8e42-e069626da1c5" />
 
 <img width="713" height="393" alt="image" src="https://github.com/user-attachments/assets/3df1c4c3-1551-45e2-8174-6964504d47c0" />
 
 <img width="713" height="393" alt="image" src="https://github.com/user-attachments/assets/8c8c706f-d162-47fc-9d2b-f1213e37b0ab" />

 <img width="713" height="437" alt="image" src="https://github.com/user-attachments/assets/59b5cbac-4a26-4e44-805e-01abbee44b2a" />

 <img width="713" height="468" alt="image" src="https://github.com/user-attachments/assets/e03553b3-2a69-4c70-8525-968ade5bd70a" />

 <img width="713" height="393" alt="image" src="https://github.com/user-attachments/assets/812eae37-203a-4768-a0d0-bafbd4258588" />

 <img width="713" height="405" alt="image" src="https://github.com/user-attachments/assets/4df63d4c-5da6-4971-b220-d0e171536299" />

-  **Bivariate Analysis**

  <img width="678" height="393" alt="image" src="https://github.com/user-attachments/assets/b6e4d6c4-7856-411b-8b5d-787d8919e3fe" />

  <img width="678" height="393" alt="image" src="https://github.com/user-attachments/assets/bd73bf16-54ce-4744-87a6-826ebfa4d71a" />

  <img width="678" height="393" alt="image" src="https://github.com/user-attachments/assets/6d18a041-ec43-4299-8a05-be2e6d86910d" />

  <img width="678" height="393" alt="image" src="https://github.com/user-attachments/assets/eb6e972c-32ed-4dd9-bec9-e6048e036fb2" />

  <img width="678" height="393" alt="image" src="https://github.com/user-attachments/assets/908dbc2f-c656-4be0-8658-13dc132f8017" />

  <img width="678" height="468" alt="image" src="https://github.com/user-attachments/assets/7121aa13-94f2-4f69-b89e-a093b4f4a7bb" />

  <img width="678" height="437" alt="image" src="https://github.com/user-attachments/assets/cece40c5-4eca-481e-9790-3210ffd34f57" />

  <img width="678" height="393" alt="image" src="https://github.com/user-attachments/assets/0a728c46-90ec-40ea-81dc-7d06e639e1a0" />


-  **Multivariate Analysis**

  <img width="757" height="659" alt="image" src="https://github.com/user-attachments/assets/39fa6145-858f-49e3-8bee-fa79816cc852" />

-  **Ouliers Untreated**

  <img width="1337" height="838" alt="image" src="https://github.com/user-attachments/assets/b16dd724-cd45-4070-9cfc-7dacf1596f78" />

-  **Outliers Treteated via Capping(Winsorization)**

  <img width="1337" height="838" alt="image" src="https://github.com/user-attachments/assets/c9d7ea69-fa6e-4516-959f-1c5e78a4a22b" />

-  **Outliers Treated Based on Target (log_price)**

  <img width="1337" height="838" alt="image" src="https://github.com/user-attachments/assets/8c134213-09fb-44f0-872e-07e4457b5aeb" />

-  **Model Results Plot**

  <img width="982" height="490" alt="image" src="https://github.com/user-attachments/assets/f547c67d-cbb9-484f-83a6-200480221bcf" />


---

## **🛡️ Tech Stack**

-  **Python 3.x**
-  **pandas, numpy, matplotlib, seaborn, scikit-learn, joblib**
-  **Jupyter Notebooks (EDA)**
-  **FastAPI + Uvicorn, Streamlit**
-  **Github (Versioning)**
-  **Render (free hosting)**
-  **Notion (project planning & task management)**

---

## **📚 References**

-  [Data](data/)
-  [Fast API Documentation](https://fastapi.tiangolo.com/)
-  [Streamlit Documentation](https://docs.streamlit.io/)





