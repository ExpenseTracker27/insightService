import logging
from typing import Optional

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from app.config.settings import settings
from app.schemas.expense import Expense

logger = logging.getLogger(__name__)


class LLMService:
    """
    Service for interacting with LLM to extract structured data from text
    """
    
    def __init__(self):
        """Initialize the LLM service with the appropriate prompt and model"""
        self.prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                "You are an expert extraction algorithm. "
                "Only extract relevant information from the text. "
                "If you do not know the value of an attribute asked to extract, "
                "return null for the attribute's value.",
            ),
            (
                "human",
                "{text}"
            )
        ])
        
        self.model = settings.OPENAI_MODEL
        self.api_key = settings.OPENAI_API_KEY
        
        if not self.api_key:
            logger.warning("OPENAI_API_KEY environment variable not set")
            
        self.llm = ChatOpenAI(api_key=self.api_key, model=self.model)
        self.runnable = self.prompt | self.llm.with_structured_output(schema=Expense)
    
    def extract_expense_data(self, message: str) -> Expense:
        """
        Extract expense data from a message using the LLM
        
        Args:
            message: The message text to analyze
            
        Returns:
            Expense: The extracted expense information
        """
        try:
            logger.debug(f"Sending message to LLM: {message[:50]}...")
            result = self.runnable.invoke({"text": message})
            logger.info(f"Successfully extracted expense data: {result}")
            return result
        except Exception as e:
            logger.error(f"Error extracting expense data: {str(e)}")
            # Return a default expense object with None values
            return Expense()