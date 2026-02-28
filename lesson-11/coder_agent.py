from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List
from termcolor import colored
import sys
import time
OLLAMA_MODEL = "qwen2.5vl:3b"

chat = ChatOllama(model=OLLAMA_MODEL, base_url="http://localhost:11434", streaming=True)
parser = StrOutputParser()

user_input = "python function that return True if the number is prime else False"
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are coder. Only return RAW CODE. DO NOT EXPLAIN ANYTHING!"),
        ("human", "{user_input}"),
    ]
)
chain = chat_prompt | chat | parser

# result = chain.invoke(input=dict())
# print(result)

tokens = []
started = False
IS_STRING = False
COLOR = "white"
function_names = ['print', 'def', 'str', 'int', 'list', 'dict', 'range']
keywords = ['if', 'elif', 'else', 'in', 'for', 'return', 'import', 'from', 'not', '=', '==', '<=', '>=', '+', '-', '*', '/', '**', '%']
constants = ['True', 'False']
def syntax_highlight(token) -> str:
    global COLOR, IS_STRING
    if token.strip() in function_names:
        return colored(token, (166,226,46))
    if token.strip() in keywords:
        return colored(token, (249,38,114))
    if token.strip() in constants:
        return colored(token, (174,129,255))
    if "\"" in token:
        if token.startswith("\""):
            token = colored("\"", (231, 219, 116)) + colored(token[1:], "white")
        elif token.endswith("\""):
            token = colored(token[0:len(token) - 1], "white") + colored("\"", (231, 219, 116))
        index = token.index("\"")
        if IS_STRING:
            COLOR = 'white'
            token = colored(token[:index+1], (231, 219, 116)) + colored(token[index:], "white")
        else:
            COLOR = (231, 219, 116)
            token = colored(token[:index+1], 'white') + colored(token[index:], (231, 219, 116))
        IS_STRING = not IS_STRING
    return colored(token, COLOR)

example_tokens = ['```', 'python', '\n', 'def', ' is', '_prime', '(n', '):\n', '   ', ' if', ' n', ' <=', ' ', '1', ':\n', '       ', ' return', ' False', '\n', '   ', ' for', ' i', ' in', ' range', '(', '2', ',', ' int', '(n', '**', '0', '.', '5', ')', ' +', ' ', '1', '):\n', '       ', ' if', ' n', ' %', ' i', ' ==', ' ', '0', ':\n', '           ', ' return', ' False', '\n', '   ', ' return', ' True', '\n', '```', '', '']
# for token in example_tokens:
while True:
    user_input = input(colored("User: ", (2,122,255)))
    if user_input.lower() == '/bye':
        break
    print(colored("Thinking...", (251,70,76)))
    for token in chain.stream({"user_input": user_input}):
        if not started:
            print(colored("Agent:\n", (233,151,63)))
            started = True
        tokens.append(token)
        token = syntax_highlight(token)
        print(token, end="", flush=True)
    started = False
    print()

# print("\nTokens:")
# print(tokens)