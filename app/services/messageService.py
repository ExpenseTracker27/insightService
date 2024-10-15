from app.services.llmService import LlmService
from app.utils.messageUtil import MessageUtil


class MessageService:
    def __init__(self):
        self.messageUtil = MessageUtil()
        self.llmService = LlmService()