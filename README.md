# Telecom-Customer-Churn-Prediction

---

## Project Overview

Customer churn is a critical business problem in the telecom industry. Retaining existing customers is significantly more cost-effective than acquiring new ones. This project focuses on predicting whether a customer is likely to churn using machine learning techniques.

The goal is to help stakeholders proactively identify high-risk customers and take appropriate retention actions.

---

## Problem Statement

Predict whether a telecom customer will churn based on demographic information, subscribed services, contract details, and billing data.

**Type of Problem:** Binary Classification  
**Target Variable:** Churn (Yes / No)

---

## Dataset

The dataset contains customer information including:

- Customer demographics
- Account details
- Service subscriptions
- Contract & billing information

Typical features:

- Tenure
- Monthly Charges
- Total Charges
- Contract Type
- Payment Method
- Online Security / Backup / Support etc.

---

## Project Workflow

### 1. Data Preprocessing

- Removed irrelevant identifier (`customerID`)
- Converted `TotalCharges` to numeric
- Handled missing values
- Applied **Label Encoding** to categorical variables
- Performed **MinMax Scaling** on continuous features

---

### 2. Models Implemented

The following machine learning models were trained and evaluated:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree
- Random Forest
- XGBoost

---

### 3. Model Evaluation Strategy

Given the class imbalance in churn data, evaluation focused on:

- ROC-AUC Score (Primary Metric)
- Accuracy
- Classification Report
- Confusion Matrix
- ROC Curve

**Why ROC-AUC?**

Accuracy can be misleading in imbalanced datasets. ROC-AUC better measures the model’s ability to distinguish churn vs non-churn customers.

---

### 4. Hyperparameter Tuning

Used **RandomizedSearchCV** for efficient parameter optimization:

- KNN tuning
- Decision Tree tuning
- Random Forest tuning
- XGBoost tuning

---

### 5. Best Model Selection

After comparing all models:

**Best Performing Model:** XGBoost  
**ROC-AUC Score:** ~86%

This indicates strong predictive capability for churn classification.

---

## Final Features Used

The final XGBoost model was trained on:

- SeniorCitizen
- Partner
- Dependents
- tenure
- OnlineSecurity
- OnlineBackup
- DeviceProtection
- TechSupport
- Contract
- PaperlessBilling
- PaymentMethod
- MonthlyCharges
- TotalCharges

---

## Model Deployment

The trained model was deployed using **Streamlit** to create an interactive web application for stakeholders.

### Application Capabilities:

- Input customer details
- Predict churn probability
- Visualize risk via gauge meter
- Categorize customer risk level

---

## API Development (Backend)

A backend service was developed using **FastAPI** to serve the trained model through a REST API.

### API Capabilities

- Accept structured customer input  
- Validate input using **Pydantic schemas**  
- Handle flexible categorical inputs (case-insensitive normalization)  
- Apply preprocessing (encoding + scaling)  
- Return churn probability and risk classification  

### Endpoint

POST /predict

### Sample Request

```json
{
  "SeniorCitizen": "Yes",
  "Partner": "No",
  "Dependents": "No",
  "tenure": 12,
  "OnlineSecurity": "No internet service",
  "OnlineBackup": "Yes",
  "DeviceProtection": "No",
  "TechSupport": "No",
  "Contract": "Month-to-month",
  "PaperlessBilling": "Yes",
  "PaymentMethod": "Credit card (automatic)",
  "MonthlyCharges": 70.5,
  "TotalCharges": 1500.2
}
```

### Sample Response

```
{
  "churn_probability": 0.73,
  "risk_level": "High Risk"
}
```

## How to Run the Project

```bash
git clone https://github.com/yourusername/Telecom-Customer-Churn-Prediction.git

cd Telecom-Customer-Churn-Prediction

pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

# Run FastAPI backend (optional)
cd Backend
uvicorn app:app --reload

```

---

## Technologies Used

- Python

- Pandas

- NumPy

- Scikit-learn

- XGBoost

- Matplotlib / Seaborn

- Plotly

- Streamlit

---

## Business Impact

This solution enables:

- Early identification of churn-risk customers

- Data-driven retention strategies

- Reduced revenue loss

- Improved customer lifetime value


---

## Future Improvements

Potential enhancements:

- One-Hot Encoding comparison

- Feature importance explainability

- SHAP analysis

- Advanced threshold tuning

- Cloud deployment (AWS / GCP / Azure)


---

