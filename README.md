# 📊 Customer Churn Prediction App

A Streamlit web app that predicts whether a telecom customer is likely to churn, based on their service and account details.

## 🚀 Demo

Try the live app: [Customer Churn App](https://vishwavannala-customer-churn-app.streamlit.app)

## 🔍 Features

- Upload customer information manually or via form inputs
- Predict customer churn using a trained XGBoost model
- View probability of churn
- Clean and interactive Streamlit UI

## 🧠 Model

- Trained on the [Telco Customer Churn Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)
- Features include tenure, services subscribed, contract type, monthly charges, and more
- Preprocessing with LabelEncoding, OneHotEncoding
- Model used: XGBoostClassifier

## 📁 Project Structure
customer-churn-app/
├── churn_streamlit_app/
│ ├── app.py # Streamlit app
│ ├── best_churn_model.pkl # Trained XGBoost model
│ ├── encoders.pkl # Pre-fitted encoders for categorical variables
│ └── requirements.txt # Python dependencies
├── WA_Fn-UseC_-Telco-Customer-Churn.csv # Dataset
└── README.md

