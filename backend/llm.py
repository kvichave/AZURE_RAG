from langchain_openai import ChatOpenAI

from config import *


llm = ChatOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    base_url=AZURE_OPENAI_ENDPOINT,
    model=AZURE_OPENAI_DEPLOYMENT,
    temperature=0,
)