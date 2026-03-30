import streamlit as st
import pickle
import pandas as pd
import plotly.graph_objects as go
import time

model = pickle.load(open('../Model/model.pkl', 'rb'))
scaler = pickle.load(open('../Model/scaler.pkl', 'rb'))

st.set_page_config(page_title="Churn Prediction", layout="wide")

st.title("Telecom Customer Churn Prediction")
st.markdown("Provide customer details to estimate churn risk")

st.divider()

# ---------------- CUSTOMER PROFILE ---------------- #

st.subheader("Customer Profile")

col1, col2, col3 = st.columns(3)

with col1:
    SeniorCitizen_ui = st.selectbox("Senior Citizen", ["No", "Yes"])

with col2:
    Partner = st.selectbox("Partner", ["Yes", "No"])

with col3:
    Dependents = st.selectbox("Dependents", ["Yes", "No"])

tenure = st.slider("Tenure (Months)", min_value=0, max_value=72, step=1)

st.divider()

# ---------------- SERVICES ---------------- #

st.subheader("Subscribed Services")

col1, col2, col3, col4 = st.columns(4)

with col1:
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])

with col2:
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])

with col3:
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])

with col4:
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])

st.divider()

# ---------------- CONTRACT & BILLING ---------------- #

st.subheader("Contract & Billing")

col1, col2, col3 = st.columns(3)

with col1:
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])

with col2:
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])

with col3:
    PaymentMethod = st.selectbox(
        "Payment Method",
        ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
    )

st.divider()

# ---------------- CHARGES ---------------- #

st.subheader("Charges")

col1, col2 = st.columns(2)

with col1:
    MonthlyCharges = st.number_input("Monthly Charges")

with col2:
    TotalCharges = st.number_input("Total Charges")

# ---------------- ENCODING ---------------- #

encoding_maps = {
    'Partner': {'Yes': 1, 'No': 0},
    'Dependents': {'Yes': 1, 'No': 0},
    'OnlineSecurity': {'No': 0, 'Yes': 2, 'No internet service': 1},
    'OnlineBackup': {'Yes': 2, 'No': 0, 'No internet service': 1},
    'DeviceProtection': {'No': 0, 'Yes': 2, 'No internet service': 1},
    'TechSupport': {'No': 0, 'Yes': 2, 'No internet service': 1},
    'Contract': {'Month-to-month': 0, 'One year': 1, 'Two year': 2},
    'PaperlessBilling': {'Yes': 1, 'No': 0},
    'PaymentMethod': {
        'Electronic check': 2,
        'Mailed check': 3,
        'Bank transfer (automatic)': 0,
        'Credit card (automatic)': 1
    }
}

SeniorCitizen = 1 if SeniorCitizen_ui == "Yes" else 0

# ---------------- PREDICTION ---------------- #

if st.button("Predict Churn"):

    input_df = pd.DataFrame({

        'SeniorCitizen': [SeniorCitizen],
        'Partner': [encoding_maps['Partner'][Partner]],
        'Dependents': [encoding_maps['Dependents'][Dependents]],
        'tenure': [tenure],

        'OnlineSecurity': [encoding_maps['OnlineSecurity'][OnlineSecurity]],
        'OnlineBackup': [encoding_maps['OnlineBackup'][OnlineBackup]],
        'DeviceProtection': [encoding_maps['DeviceProtection'][DeviceProtection]],
        'TechSupport': [encoding_maps['TechSupport'][TechSupport]],

        'Contract': [encoding_maps['Contract'][Contract]],
        'PaperlessBilling': [encoding_maps['PaperlessBilling'][PaperlessBilling]],
        'PaymentMethod': [encoding_maps['PaymentMethod'][PaymentMethod]],

        'MonthlyCharges': [MonthlyCharges],
        'TotalCharges': [TotalCharges]
    })

    # ---------------- SCALING ---------------- #

    scale_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
    input_df[scale_cols] = scaler.transform(input_df[scale_cols])

    churn_prob = model.predict_proba(input_df)[0][1]

    st.subheader("Prediction Result")

    col1, col2 = st.columns(2)

    # ---------------- ANIMATED GAUGE ---------------- #

    with col1:

        gauge_placeholder = st.empty()

        for i in range(0, int(churn_prob * 100) + 1, 2):

            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=i,
                title={'text': "Churn Risk Score"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'steps': [
                        {'range': [0, 40], 'color': "green"},
                        {'range': [40, 70], 'color': "orange"},
                        {'range': [70, 100], 'color': "red"}
                    ],
                }
            ))

            gauge_placeholder.plotly_chart(fig, width= 'stretch')

            time.sleep(0.02)   # Animation speed

    # ---------------- RISK OUTPUT ---------------- #

    with col2:

        st.metric("Churn Probability", f"{churn_prob:.2%}")

        if churn_prob < 0.4:
            st.success("Low Risk Customer")
            st.info("Recommendation: Maintain engagement")

        elif churn_prob < 0.7:
            st.warning("Moderate Risk Customer")
            st.info("Recommendation: Offer loyalty incentives")

        else:
            st.error("High Risk Customer")
            st.info("Recommendation: Immediate retention action")