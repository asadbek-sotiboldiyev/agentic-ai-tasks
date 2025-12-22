from google.genai import types
from custom_functions import *


config = types.GenerateContentConfig(
    tools=[get_students_ciy, get_weater],
    system_instruction="Always answer with human readable format after tool calling."
)