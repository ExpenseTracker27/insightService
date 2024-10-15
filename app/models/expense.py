from typing import Optional
from pydantic import BaseModel, Field


class Expense(BaseModel):
    """
        Represents a financial expense associated with a transaction.
    """

    amount: Optional[str] = Field(
        title="Expense Amount",
        description="The total amount of the expense incurred during the transaction. Use a numeric format, e.g., '100.50'."
    )

    merchant: Optional[str] = Field(
        title="Merchant Name",
        description="The name of the merchant or vendor where the transaction took place."
    )

    currency: Optional[str] = Field(
        title="Transaction Currency",
        description="The currency in which the transaction was conducted (e.g., 'INR', 'USD')."
    )