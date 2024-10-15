from app.services.llmService import LLMService
from app.utils.messageUtil import MessageUtil


class MessageService:
    def __init__(self):
        self.messageUtil = MessageUtil()
        self.llmService = LLMService()

    def process_message(self, message):
        if self.messageUtil.is_bank_sms(message):
            return self.llmService.run_llm(message)

        return None