from pydantic import BaseModel
from typing import List, Optional
import json
from pprint import pprint

class FunctionCall(BaseModel):
    name: str
    arguments: str

class ToolCall(BaseModel):
    id: str
    type: str
    reason: Optional[str]
    function: FunctionCall

class Resposne(BaseModel):
    role: str
    content: Optional[str]
    tool_calls: List[ToolCall]

with open("example-response.json", "r") as f:
    example_call_from_ai = f.read()

# result = json.loads(example_call_from_ai)
result = Resposne.model_validate_json(example_call_from_ai)
# type_info = 
pprint(result)

