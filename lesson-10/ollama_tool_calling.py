import json
import os
from typing import Any, List

from dotenv import load_dotenv
from langchain.tools import tool
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    ToolCall,
    ToolMessage,
)
from langchain_core.messages.tool import tool_call
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

load_dotenv()


class ToolCallCLass:
    def __init__(self, data):
        self.data = data


model = ChatGoogleGenerativeAI(model=str(os.getenv("GEMINI_MODEL_NAME")))

# model = ChatOllama(
#     model=str(os.getenv("OLLAMA_MODEL")), base_url="http://localhost:11434"
# )

data = {
    "john": "Doe",
    "John": "Connor",
    "Sarah": "Connor",
    "Peter": "Parker",
    "Robert": "Dovney",
    "Harry": "Smith",
}
universities = {
    "john-Doe": "TUIT",
    "John-Connor": "TUIT",
    "Sarah-Connor": "TUIT",
    "Peter-Parker": "TSTU",
    "Robert-Dovney": "TSTU",
    "Harry-Smith": "UWED",
}


@tool("get_lastname", description="returns lastname of given name")
def get_lastname(name: str) -> str:
    """
    params: name:str|required
    return: str
    """
    lastname = data.get(name, "Unknown")
    return lastname


@tool(
    "get_university",
    description="This tool gives universityname of student. Use this ONLY AFTER you have both the firstname and the lastname.",
)
def get_university(name: str, lastname: str) -> str:
    """
    Params: name:str|required, lastname:str|required
    return: str
    """
    university = universities.get(
        name.capitalize() + "-" + lastname.capitalize(), "Unknown"
    )
    return university


tools = [get_lastname, get_university]
tool_executor = {tool.name: tool for tool in tools}
model = model.bind_tools(tools)

user_input = "first get lastname and give me universityname of John"
actions = [HumanMessage(content=user_input)]

messages: Any = [
    SystemMessage(
        content="You are an agent. You can call tools. Only return result based on tools, not based on your old knowledges"
    ),
]
while len(actions) > 0:
    action = actions.pop(0)

    if isinstance(action, HumanMessage):
        messages.append(action)
    elif isinstance(action, list) and isinstance(action[0], ToolCallCLass):
        for current_action in action:
            current_action = current_action.data
            tool_name = current_action["name"]
            uid = current_action["id"]
            print(">> Executing tool: ", tool_name, "args:", current_action["args"])
            tool_result = tool_executor[tool_name].invoke(current_action["args"])
            print(">> Tool result: ", tool_result)
            messages.append(ToolMessage(content=tool_result, tool_call_id=uid))

    print("** Requesting Agent:", messages)
    print("Thinking...")
    ai_response = model.invoke(messages)
    if len(ai_response.tool_calls) > 0:
        actions.append(
            [ToolCallCLass(tool_for_call) for tool_for_call in ai_response.tool_calls]
        )
    elif isinstance(ai_response, AIMessage):
        print(ai_response)
        print("> Agent:", ai_response.content)
    # print(actions)
print("-- Program finished")
