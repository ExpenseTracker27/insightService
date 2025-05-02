import pytest

from app.core.message_analyzer import MessageAnalyzer


class TestMessageAnalyzer:
    def setup_method(self):
        self.analyzer = MessageAnalyzer()
        
    def test_is_bank_sms_with_bank_keywords(self):
        # Test messages containing bank keywords
        test_messages = [
            "Your bank account was debited with $100 for purchase at COFFEE SHOP",
            "You spent $50 using your card at RESTAURANT",
            "Transaction of $75.99 at STORE using your card",
        ]
        
        for message in test_messages:
            assert self.analyzer.is_bank_sms(message) is True
            
    def test_is_bank_sms_without_bank_keywords(self):
        # Test messages without bank keywords
        test_messages = [
            "Your package has been delivered",
            "Meeting scheduled for tomorrow at 2pm",
            "Your subscription will expire soon",
        ]
        
        for message in test_messages:
            assert self.analyzer.is_bank_sms(message) is False