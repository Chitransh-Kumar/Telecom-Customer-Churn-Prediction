def normalize_text(value: str) -> str:
    return value.lower().replace(" ", "").replace("-", "").replace("_", "")


def map_value(value: str, mapping: dict):
    norm_val = normalize_text(value)

    for key in mapping:
        if normalize_text(key) == norm_val:
            return mapping[key]

    raise ValueError(f"Invalid value: {value}")


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


def preprocess_input(data):
    import pandas as pd

    SeniorCitizen = 1 if normalize_text(data.SeniorCitizen) == "yes" else 0

    input_dict = {
        'SeniorCitizen': SeniorCitizen,
        'Partner': map_value(data.Partner, encoding_maps['Partner']),
        'Dependents': map_value(data.Dependents, encoding_maps['Dependents']),
        'tenure': data.tenure,

        'OnlineSecurity': map_value(data.OnlineSecurity, encoding_maps['OnlineSecurity']),
        'OnlineBackup': map_value(data.OnlineBackup, encoding_maps['OnlineBackup']),
        'DeviceProtection': map_value(data.DeviceProtection, encoding_maps['DeviceProtection']),
        'TechSupport': map_value(data.TechSupport, encoding_maps['TechSupport']),

        'Contract': map_value(data.Contract, encoding_maps['Contract']),
        'PaperlessBilling': map_value(data.PaperlessBilling, encoding_maps['PaperlessBilling']),
        'PaymentMethod': map_value(data.PaymentMethod, encoding_maps['PaymentMethod']),

        'MonthlyCharges': data.MonthlyCharges,
        'TotalCharges': data.TotalCharges
    }

    return pd.DataFrame([input_dict])