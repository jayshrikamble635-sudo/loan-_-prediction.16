import streamlit as st
import pandas as pd
import joblib

st.title("Loan Prediction App")

model = joblib.load("Loan_prediction_Model.pkl")
encoders = joblib.load("label_encoder (4).pkl")

gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
income = st.number_input("ApplicantIncome", min_value=0)

if st.button("Predict"):
    df = pd.DataFrame({
        "Gender": [gender],
        "Education": [education],
        "ApplicantIncome": [income]
    })

    for col in df.columns:
        if col in encoders:
            df[col] = encoders[col].transform(df[col])

    result = model.predict(df)

    st.success("Loan Approved" if result[0] == 1 else "Loan Not Approved")
