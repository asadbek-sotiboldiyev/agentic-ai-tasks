from langgraph.graph import StateGraph, START, END
from typing import TypedDict

class State(TypedDict):
	"""Custom state for learning"""
	state_obj: str

def node_1(state: State) -> State:
	print("===== node_1 =====")
	print("state: ", state["state_obj"])
	state["state_obj"] += "node_1"
	return state
def node_2(state: State) -> State:
	print("===== node_2 =====")
	print("state: ", state["state_obj"])
	state["state_obj"] += "-> node_2"
	return state
def node_3(state: State) -> State:
	print("===== node_3 =====")
	print("state: ", state["state_obj"])
	state["state_obj"] += "-> node_3"
	return state

def continue_or_end(state: State) -> str:
	print("===== cond =====")
	print(state["state_obj"])
	if state["state_obj"] == "":
		return "node_1"
	return END

if __name__ == "__main__":
	graph = StateGraph(State)
	graph.add_node(node_1)
	graph.add_node(node_2)
	graph.add_node(node_3)

	graph.add_conditional_edges(START, continue_or_end, {"node_1": "node_1", END: END})
	graph.add_edge("node_1", 'node_2')
	graph.add_edge("node_2", 'node_3')
	graph.add_edge("node_3", END)

	workflow = graph.compile()
	workflow.get_graph().draw_mermaid_png(output_file_path="flow.png")

	result = workflow.invoke({"state_obj": "Hello"})
	print(result)


