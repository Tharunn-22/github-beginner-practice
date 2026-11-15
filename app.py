import streamlit as st
import joblib
import numpy as np

model = joblib.load('churn_model2.pkl')

st.title("Customer Churn Prediction")

tenure = st.number_input("Enter Tenure")

monthlycharges = st.number_input("Enter Monthly Charges")

totalcharges = st.number_input("Enter Total Charges")

if st.button("Predict"):

    input_data = np.array([
        tenure,
        monthlycharges,
        totalcharges
    ]).reshape(1,-1)

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.write("Customer Will Churn")

    else:
        st.write("Customer Will Stay")