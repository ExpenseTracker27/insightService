from pydantic import BaseModel, Field


class MessageRequest(BaseModel):
    """
    Request schema for message processing
    """
    message: str = Field(..., description="The message content to analyze")


class MessageResponse(BaseModel):
    """
    Response schema for message processing
    """
    amount: str = Field(None, description="Extracted amount from the message")
    merchant: str = Field(None, description="Extracted merchant from the message")
    currency: str = Field(None, description="Extracted currency from the message")
    user_id: str = Field(None, description="User ID from the request header")