from typing import Optional
import os
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_mistralai import ChatMistralAI
from langchain_core.utils.function_calling import convert_to_openai_tool
from dotenv import load_dotenv, dotenv_values


class LlmService:
    def __init__(self):
        load_dotenv()
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
        self.apikey = os.getenv("API_KEY")
