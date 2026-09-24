import streamlit as st
import pandas as pd
import joblib

st.title("📉 Telecom Churn Predictor")
model = joblib.load("churn_model.pkl")

tenure = st.slider("Tenure", 0, 72, 12)
monthly = st.slider("Monthly Charges", 18, 120, 70)
total = st.number_input("Total Charges", value=500)
contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
internet = st.selectbox("Internet", ["DSL", "Fiber optic", "No"])

if st.button("Predict"):
    data = pd.DataFrame([{
        'gender': 'Male', 'SeniorCitizen': 0, 'Partner': 'No', 'Dependents': 'No',
        'tenure': tenure, 'PhoneService': 'Yes', 'MultipleLines': 'No',
        'InternetService': internet, 'OnlineSecurity': 'No', 'OnlineBackup': 'No',
        'DeviceProtection': 'No', 'TechSupport': 'No', 'StreamingTV': 'No',
        'StreamingMovies': 'No', 'Contract': contract, 'PaperlessBilling': 'Yes',
        'PaymentMethod': 'Electronic check', 'MonthlyCharges': monthly, 'TotalCharges': total
    }])
    prob = model.predict_proba(data)[0][1]
    if prob > 0.5:
        st.error(f"High Churn! Risk: {prob*100:.1f}%- Customer is likely to churn")
    else:
        st.success(f"Low Churn! Risk: {prob*100:.1f}%-Customer is likely to stay")