from google import genai
from dotenv import load_dotenv
from google.genai import types
import os
load_dotenv()

key = os.getenv("GEMINI_API_KEY")
model = os.getenv("GEMINI_MODEL")
ai = genai.Client(api_key=key)
ai_model = str(os.getenv("GEMINI_MODEL"))
context = ''
with open("history.txt", 'r') as f:
    context = f.read()
context = context.split(">>")
hist = []
for i in context:
    if i.startswith("user:"):
        hist.append(types.Content(role="user", parts=[types.Part(text=i)]))
        print("user")
    elif i.startswith:
        hist.append(types.Content(role="model", parts=[types.Part(text=i)]))
        print("ai")
chat = ai.chats.create(model=ai_model, history=hist)
while True:
    prompt = input("Ask me anything[q - quit]: ")
    if prompt == 'q':
        print("Good bye!")
        break
    print("\rThinking...")
    response = chat.send_message(prompt).text
    print(response)
    with open("history.txt", 'a') as f:
        f.write(">>user:" + prompt + "\n" + ">>AI:" + response + '\n')
