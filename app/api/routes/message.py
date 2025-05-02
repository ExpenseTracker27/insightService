import logging
from typing import Optional

from fastapi import APIRouter, Depends, Header, HTTPException

from app.api.deps import get_llm_service, get_message_analyzer, get_kafka_client
from app.core.llm_service import LLMService
from app.core.message_analyzer import MessageAnalyzer
from app.schemas.message import MessageRequest, MessageResponse
from app.config.settings import settings

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/message", response_model=MessageResponse)
async def process_message(
    request_data: MessageRequest,
    x_user_id: Optional[str] = Header(None),
    message_analyzer: MessageAnalyzer = Depends(get_message_analyzer),
    llm_service: LLMService = Depends(get_llm_service),
    kafka_client = Depends(get_kafka_client),
):
    """
    Process a message to extract expense information and publish to Kafka
    """
    if not x_user_id:
        logger.warning("Request received without user_id header")
        
    logger.info(f"Processing message for user: {x_user_id}")
    
    # Check if the message is a bank SMS
    if not message_analyzer.is_bank_sms(request_data.message):
        logger.info("Message is not a bank SMS, skipping processing")
        return MessageResponse(user_id=x_user_id)
        
    try:
        # Extract expense data from the message
        result = llm_service.extract_expense_data(request_data.message)
        
        # Add user_id to the result
        result_dict = result.model_dump()
        result_dict['user_id'] = x_user_id
        
        # Send the result to Kafka
        kafka_client.send_message(result_dict, settings.KAFKA_TOPIC)
        
        # Return the response
        return MessageResponse(**result_dict)
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        raise HTTPException(status_code=500, detail="Error processing message")