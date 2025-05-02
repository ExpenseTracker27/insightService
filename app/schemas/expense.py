from typing import Optional

from pydantic import BaseModel, Field


class Expense(BaseModel):
    """
    Represents a financial expense extracted from a transaction message
    """
    amount: Optional[str] = Field(
        None,
        title="Expense Amount",
        description="The total amount of the expense incurred during the transaction. Use a numeric format, e.g., '100.50'."
    )

    merchant: Optional[str] = Field(
        None,
        title="Merchant Name",
        description="The name of the merchant or vendor where the transaction took place."
    )

    currency: Optional[str] = Field(
        None,
        title="Transaction Currency",
        description="The currency in which the transaction was conducted (e.g., 'INR', 'USD')."
    )
