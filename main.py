from langchain.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))
chat = ChatOpenAI(openai_api_key=os.environ.get("OPENAI_API_KEY"))
a = llm.predict("How many planets are there?")
b = chat.predict("How many planets are there?")
print(a, b)