import json
import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import AzureChatOpenAI

load_dotenv()

categories = ["Math", "Music", "Programming"]
# category_name
# score

# English to French translator
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant"),
        (
            "human",
            """Which category best describes this message '{message}' based on following categories: \n {categories}.
        You must give me only JSON formatted response like this: {{"category": "Programming", "score": 0.8}}.
     """,
        ),
    ]
).partial(categories=categories)


llm = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
)
parser = StrOutputParser()

chain = prompt | llm | parser

# out = chain.invoke({"message": "Python is a programming language"})
out = chain.invoke({"message": "Python is a programming language"})
json_data = json.loads(out)

print(json_data)
print(json_data["category"])
print(json_data["score"])
# print(category_name)
# print(score)
