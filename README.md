🔮 Units Prediction App

An end-to-end Machine Learning + Streamlit web application that predicts electricity Units consumption based on infrastructure, load, and service-related features.

🚀 Project Overview

This project uses a Random Forest Regressor to predict electricity usage (Units) using features like:

Location hierarchy (Circle, Division, SubDivision, Section)
Load data
Service metrics
Engineered features

The model is deployed using Streamlit for an interactive user interface.

📊 Features
📥 User input via Streamlit UI
🧠 ML model prediction (Random Forest)
⚙️ Feature engineering included
🔄 Real-time prediction
💾 Model saved using Joblib
🧠 Machine Learning Pipeline
🔹 Feature Engineering
Load_per_Service = Load / TotServices
Billing_Ratio = BilledServices / TotServices
Log_Load = log(1 + Load)
🔹 Preprocessing
Categorical features → OneHotEncoder
Numerical features → Pass-through
Combined using ColumnTransformer
🔹 Model Used
RandomForestRegressor
n_estimators = 334
max_depth = 21
min_samples_split = 7
max_features = sqrt
📁 Project Structure
📦 Units-Prediction-App
│
├── app.py                 # Streamlit application
├── model_training.py      # Model training script
├── rf_units_model.pkl     # Saved trained model
├── cleaned_data.xls       # Dataset
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
⚙️ Installation
1️⃣ Clone the repository
---
git clone https://github.com/your-username/units-prediction-app.git
---
cd units-prediction-app
2️⃣ Install dependencies
---
pip install -r requirements.txt
---
▶️ Run the Application
---
streamlit run app.py
---
🧪 Model Training

To retrain the model:
----

python model_training.py
---

This will:

Train the pipeline
Save model as rf_units_model.pkl


🖥️ App Inputs

Users need to provide:
Circle
Division
SubDivision
Section
Load
Total Services
Billed Services
📈 Output
✅ Predicted Units (Electricity consumption)
🛠️ Tech Stack
Python 🐍
Pandas & NumPy
Scikit-learn
Streamlit
Joblib
📌 Future Improvements
📊 Add model evaluation metrics (R², RMSE)
🌐 Deploy on cloud (Streamlit Cloud / AWS)
📉 Add visualization dashboard
🤖 Try advanced models (XGBoost, LightGBM)
