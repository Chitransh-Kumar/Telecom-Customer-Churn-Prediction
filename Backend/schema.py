from pydantic import BaseModel, Field
from typing import Annotated


class ChurnInput(BaseModel):
    """
    Schema for Telecom Customer Churn Prediction Input

    All fields are required and validated strictly.
    Categorical inputs are case-insensitive and flexible.
    """

    SeniorCitizen: Annotated[
        str,
        Field(
            ...,
            description="Whether the customer is a senior citizen",
            examples=["Yes", "No"]
        )
    ]

    Partner: Annotated[
        str,
        Field(
            ...,
            description="Whether the customer has a partner",
            examples=["Yes", "No"]
        )
    ]

    Dependents: Annotated[
        str,
        Field(
            ...,
            description="Whether the customer has dependents",
            examples=["Yes", "No"]
        )
    ]

    tenure: Annotated[
        int,
        Field(
            ...,
            ge=0,
            le=72,
            description="Number of months the customer has stayed with the company (0–72)"
        )
    ]

    OnlineSecurity: Annotated[
        str,
        Field(
            ...,
            description="Subscription to online security service",
            examples=["Yes", "No", "No internet service"]
        )
    ]

    OnlineBackup: Annotated[
        str,
        Field(
            ...,
            description="Subscription to online backup service",
            examples=["Yes", "No", "No internet service"]
        )
    ]

    DeviceProtection: Annotated[
        str,
        Field(
            ...,
            description="Subscription to device protection service",
            examples=["Yes", "No", "No internet service"]
        )
    ]

    TechSupport: Annotated[
        str,
        Field(
            ...,
            description="Subscription to tech support service",
            examples=["Yes", "No", "No internet service"]
        )
    ]

    Contract: Annotated[
        str,
        Field(
            ...,
            description="Customer contract type",
            examples=["Month-to-month", "One year", "Two year"]
        )
    ]

    PaperlessBilling: Annotated[
        str,
        Field(
            ...,
            description="Whether the customer uses paperless billing",
            examples=["Yes", "No"]
        )
    ]

    PaymentMethod: Annotated[
        str,
        Field(
            ...,
            description="Payment method used by the customer",
            examples=[
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )
    ]

    MonthlyCharges: Annotated[
        float,
        Field(
            ...,
            ge=0,
            description="Monthly charges billed to the customer"
        )
    ]

    TotalCharges: Annotated[
        float,
        Field(
            ...,
            ge=0,
            description="Total charges accumulated by the customer"
        )
    ]

    class Config:
        json_schema_extra = {
            "example": {
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
        }