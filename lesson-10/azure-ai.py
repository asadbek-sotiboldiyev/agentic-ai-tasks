from openai import AzureOpenAI
import os

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

history = [
    {
        "role":"user",
        "content":"Hi"
    }
]
while True:
    user_input = input("user: ")
    if user_input.lower() == "/bye":
        break
    history.append()