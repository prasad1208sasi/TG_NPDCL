import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ===============================
# Load Model
# ===============================

model = joblib.load("rf_units_model.pkl")

st.set_page_config(page_title="Units Prediction App")
st.title("🔮 Units Prediction App")

st.write("Enter details below:")

# ===============================
# User Inputs
# ===============================

circle = st.text_input("Circle")
division = st.text_input("Division")
subdivision = st.text_input("SubDivision")
section = st.text_input("Section")

load = st.number_input("Load", min_value=0.0)
tot_services = st.number_input("Total Services", min_value=0.0)
billed_services = st.number_input("Billed Services", min_value=0.0)

# ===============================
# Prediction
# ===============================

if st.button("Predict Units"):

    load_per_service = load / (tot_services + 1e-6)
    billing_ratio = billed_services / (tot_services + 1e-6)
    log_load = np.log1p(load)

    input_df = pd.DataFrame({
        "Circle": [circle],
        "Division": [division],
        "SubDivision": [subdivision],
        "Section": [section],
        "Load": [load],
        "TotServices": [tot_services],
        "BilledServices": [billed_services],
        "Load_per_Service": [load_per_service],
        "Billing_Ratio": [billing_ratio],
        "Log_Load": [log_load]
    })

    prediction = model.predict(input_df)

    st.success(f"Predicted Units: {prediction[0]:,.2f}")
