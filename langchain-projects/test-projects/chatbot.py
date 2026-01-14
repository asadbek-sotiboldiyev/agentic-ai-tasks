from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
messages = [
    SystemMessage(
        content="You are a presentation assistant. You need to give me presentation slide datas about given TOPIC as a JSON object."
    )
]
message = HumanMessage(content="Introduction to LangChain")
response = model.invoke(messages + [message])
print(response.content)
with open("output.txt", "w") as f:
    f.write(response.content)
