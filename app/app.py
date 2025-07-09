import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('rf_model.pkl')
scaler = joblib.load('scaler.pkl')

# Recommendation mapping
recommendation_map = {
    0: "No action needed",
    1: "Regular check-up / Lifestyle guidance"
}

# App title
st.title("🩺 Personalized Healthcare Recommendation")

# Input form
st.sidebar.header("Patient Information")

recency = st.sidebar.slider("Months Since Last Donation (Recency)", 0, 50, 10)
frequency = st.sidebar.slider("Total Donations (Frequency)", 0, 50, 2)
monetary = st.sidebar.number_input("Total Volume Donated (in cc)", 250, 12500, 1000)
time = st.sidebar.slider("Months Since First Donation (Time)", 0, 100, 30)

if st.sidebar.button("Get Recommendation"):
    # Preprocess input
    input_data = pd.DataFrame([{
        'Recency': recency,
        'Frequency': frequency,
        'Monetary': np.log1p(monetary),
        'Time': time
    }])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)[0]
    
    # Output
    st.subheader("🧠 Recommendation")
    st.success(recommendation_map.get(prediction, "Unknown"))
