from langchain_core import messages
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import MessagesState
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_ollama import ChatOllama
import random

llm = ChatOllama(model="llama3.2:latest")
NUM = random.randint(1, 50)
print("NUM: ", NUM)
system_prompt = SystemMessage("""You can only return ONE NUMBER. you can't write any word. i have though number between 1 and 50.
	Find number that i thought. if you give me number, i will tell you [less, greater, correct].
	use optimal algorithm for finding number.
	for example, my number is 5: 
		you: 10; me: less; you 4; me: greater.
	You should return only one number like this: 34 """)

def agent(state: MessagesState):
	response = llm.invoke([system_prompt] + state["messages"])
	print("===== Agent =====")
	print(response.content)
	return {"messages": [response]}

def checker(state: MessagesState):
	message = state["messages"][-1].content
	try:
		num = int(message)
		if num == NUM:
			state['messages'].append(HumanMessage(content="correct"))
		elif num > NUM:
			state['messages'].append(HumanMessage(content="less"))
		else:
			state['messages'].append(HumanMessage(content="greater"))
		print("===== Checker =====")
		print(state['messages'][-1].content)
		return state
	except Exception as e:
		print(">> ERROR: ", e)
		state['messages'].append(HumanMessage(content="there is an error your output format. you have given wrong format result"))
		return state

def correct(state: MessagesState):
	state['messages'].append(HumanMessage(content="you have found it and won!"))
	return state

def router(state: MessagesState):
	last = state["messages"][-1].content
	if last == "correct":
		return "correct"
	return "agent"

graph = StateGraph(MessagesState)

graph.add_node("agent", agent)
graph.add_node("agent_correct", agent)
graph.add_node("checker", checker)
graph.add_node("correct", correct)

graph.add_edge(START, "agent")
graph.add_edge("agent", "checker")
graph.add_conditional_edges("checker", router, {"correct": "correct", "agent": "agent"})
graph.add_edge("correct", "agent_correct")
graph.add_edge("agent_correct", END)

workflow = graph.compile()
workflow.get_graph().draw_mermaid_png(output_file_path="flow.png")

message_state = workflow.invoke({"messages": [
			system_prompt,
			HumanMessage(content="I thought of a number, find it. Between 1 and 50")
		]
	}
)
for message in message_state['messages']:
	message.pretty_print()









