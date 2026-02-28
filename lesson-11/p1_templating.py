import os

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field
from typing import List

OLLAMA_MODEL = "llama3.2:latest"

class Tank(BaseModel):
    name: str = Field(description="name")
    country: str = Field(description="country of tank")
    tier: int = Field(description="tier of tank")
class Tanks(BaseModel):
    list_of_tanks: List[Tank] = Field(name="list_of_tanks", description="List of Tank objects")

model = ChatOllama(
    model=OLLAMA_MODEL, base_url="http://localhost:11434", streaming=True
)
# parser = StrOutputParser()
parser = PydanticOutputParser(pydantic_object=Tanks)

user_input = "Hello, Im {name}. i play World of Tanks blitz. i have tier-6 tank -  KV-2. this is Soviet Union tank. My favorite tank is SU-100. SU-100 is Sovet Union tier-5 tank"
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are data extrctor. extract datas from plain text and return only list of JSON based on parser instructions. fields: name, country, tier. wrap list with list_of_tanks"),
        ("human", user_input),
    ]
).partial(format_instructions=parser.get_format_instructions())
print(parser.get_format_instructions())
# messages = chat_prompt.invoke({"name": "Alice"})

# response = model.invoke(messages)
chain = chat_prompt | model | parser
result = chain.invoke({"name": "Alice"})
print(result)
# for i in chain.stream({"name": "John Connor"}):
#     print(i, end="", flush=True)