import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from app.entities.expense import Expense


class LLMService:
    def __init__(self):
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
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.llm = ChatOpenAI(api_key=self.api_key, model="gpt-3.5-turbo")
        self.runnable = self.prompt | self.llm.with_structured_output(schema=Expense)

    def run_llm(self, message):
        return self.runnable.invoke({"text": message})
