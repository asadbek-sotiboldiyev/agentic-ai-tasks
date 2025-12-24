from google.genai import types

from custom_functions import get_students_ciy, get_weater

info_get_students_ciy = {
    "name": "get_students_city",
    "description": "returns home city of given student",
    "parameters": {
        "type": "object",
        "properties": {
            "student_name": {
                "type": "string",
                "description": "name of student",
            },
            "required": ["student_name"],
        },
    },
}
info_get_weather = {
    "name": "get_weather",
    "description": "returns current weather of given city",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "name of city",
            },
            "required": ["city"],
        },
    },
}
tools = types.Tool(function_declarations=[info_get_students_ciy, info_get_weather])
config = types.GenerateContentConfig(
    tools=[tools],
    system_instruction="""
    get_weater - get wheather info of given city
    get_students_ciy - returns city of student;
""",
)
