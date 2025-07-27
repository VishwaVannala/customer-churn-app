import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("best_churn_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Telco Churn Predictor", layout="centered")
st.title("📉 Telco Customer Churn Prediction")
st.write("Fill in the customer details to predict churn probability:")

# Input form
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Has Partner?", ["Yes", "No"])
dependents = st.selectbox("Has Dependents?", ["Yes", "No"])
tenure = st.slider("Tenure (in months)", 0, 72, 12)

phone_service = st.selectbox("Phone Service", ["Yes", "No"])
multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
online_backup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])
device_protection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
tech_support = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
streaming_tv = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["Yes", "No"])
payment_method = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])

monthly = st.number_input("Monthly Charges", min_value=0.0, max_value=200.0, value=70.0)
total = st.number_input("Total Charges", min_value=0.0, max_value=10000.0, value=2000.0)

# Predict button
if st.button("Predict Churn"):
    # Prepare input
    input_data = pd.DataFrame({
        'gender': [1 if gender == "Male" else 0],
        'SeniorCitizen': [1 if senior == "Yes" else 0],
        'Partner': [1 if partner == "Yes" else 0],
        'Dependents': [1 if dependents == "Yes" else 0],
        'tenure': [tenure],
        'PhoneService': [1 if phone_service == "Yes" else 0],
        'MultipleLines': [0 if multiple_lines == "No" else 1 if multiple_lines == "Yes" else 2],
        'InternetService': [0 if internet_service == "DSL" else 1 if internet_service == "Fiber optic" else 2],
        'OnlineSecurity': [0 if online_security == "No" else 1 if online_security == "Yes" else 2],
        'OnlineBackup': [0 if online_backup == "No" else 1 if online_backup == "Yes" else 2],
        'DeviceProtection': [0 if device_protection == "No" else 1 if device_protection == "Yes" else 2],
        'TechSupport': [0 if tech_support == "No" else 1 if tech_support == "Yes" else 2],
        'StreamingTV': [0 if streaming_tv == "No" else 1 if streaming_tv == "Yes" else 2],
        'StreamingMovies': [0 if streaming_movies == "No" else 1 if streaming_movies == "Yes" else 2],
        'Contract': [0 if contract == "Month-to-month" else 1 if contract == "One year" else 2],
        'PaperlessBilling': [1 if paperless_billing == "Yes" else 0],
        'PaymentMethod': [
            0 if payment_method == "Electronic check" else
            1 if payment_method == "Mailed check" else
            2 if payment_method == "Bank transfer (automatic)" else
            3
        ],
        'MonthlyCharges': [monthly],
        'TotalCharges': [total]
    })

    # Prediction
    churn_prob = model.predict_proba(input_data)[:, 1][0]
    st.success(f"Churn Probability: {churn_prob:.2%}")

    if churn_prob > 0.5:
        st.warning("⚠️ High risk of churn!")
    else:
        st.info("✅ Customer likely to stay.")
