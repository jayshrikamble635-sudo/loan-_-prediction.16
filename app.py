import streamlit as st
import pandas as pd
import joblib

st.title("Loan Prediction App")

# Load trained model and label encoders
model = joblib.load("Loan_prediction_Model.pkl")
label_encoders = joblib.load("label_encoder (4).pkl")

st.subheader("Enter Applicant Details")

gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
income = st
