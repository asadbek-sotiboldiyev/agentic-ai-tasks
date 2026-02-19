from pprint import pprint

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from termcolor import colored

model = ChatOpenAI(
    model="llama3.2:latest", api_key="key", base_url="http://localhost:11434/v1"
)
history = [SystemMessage(content="You are a helpful assistant.")]
while True:
    user_input = input("-------------\nUser: ")
    if user_input.lower() == "exit":
        print("-------------\nProgram finished")
        break
    history.append(HumanMessage(content=user_input))
    response = model.invoke(history)
    history.append(AIMessage(content=response.content))
    print("-------------")
    pprint(response)
    print(response.content)
