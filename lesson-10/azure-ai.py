import os

from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

client = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
)


history = []
while True:
    user_input = input("-------\nuser: ")
    if user_input.lower() == "/bye":
        break
    history.append(HumanMessage(content=user_input))
    response = client.invoke(history)
    history.append(
        AIMessage(content=response.content)
    )
    print("-----Response")
    print(response)
    print("-----Agent:\n")
    print(response.content)
