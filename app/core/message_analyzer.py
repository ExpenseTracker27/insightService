import logging
import re
from typing import Dict, Any, Optional

from app.schemas.expense import Expense

logger = logging.getLogger(__name__)


class MessageAnalyzer:
    """
    Analyzes message content to determine if it's a bank SMS
    and extracts relevant information
    """
    
    def __init__(self):
        self.bank_keywords = ['spent', 'card', 'bank', 'account', 'transaction', 'purchase']
        
    def is_bank_sms(self, message: str) -> bool:
        """
        Determine if a message is likely a bank SMS by checking for keywords
        
        Args:
            message: The SMS content to analyze
            
        Returns:
            bool: True if message appears to be a bank SMS
        """
        pattern = r'\b(?:' + '|'.join(re.escape(word) for word in self.bank_keywords) + r')\b'
        match = bool(re.search(pattern, message, flags=re.IGNORECASE))
        
        logger.debug(f"Message analyzed as bank SMS: {match}")
        return match