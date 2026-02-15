import streamlit as st
import pandas as pd
import joblib

st.title("Loan Prediction App")

# Load model and label encoders (PKL files)
model = joblib.load("Loan_prediction_Model.pkl")
label_encoders = joblib.load("label_encoder (4).pkl")

st.subheader("Enter Applicant Details")

gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
income = st.number_input("ApplicantIncome", min_value=0)

if st.button("Predict"):
    input_df = pd.DataFrame({
        "Gender": [gender],
        "Education": [education],
        "ApplicantIncome": [income]
    })

    # Apply encoding using saved encoders
    for col in input_df.columns:
        if col in label_encoders:
            input_df[col] = label_encoders[col].transform(input_df[col])

    prediction = model.predict(input_df)

    if prediction[0] == 1:
        st.write("Loan Approved")
    else:
        st.write("Loan Not Approved")
