from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from agent1_research import research
from agent2_answer_drafter import draft_answer
from typing import TypedDict
from langchain_community.chat_models import ChatOpenAI  # ✅ updated

# STEP 1: Define a schema
class GraphState(TypedDict):
    query: str
    research: str
    answer: str

# STEP 2: Initialize the graph with schema
graph = StateGraph(state_schema=GraphState)  # ✅ fixed

# STEP 3: Add the nodes (functions)
graph.add_node("research", RunnableLambda(lambda state: {"research": research(state["query"])}))
graph.add_node("draft", RunnableLambda(lambda state: {"answer": draft_answer(state["research"])}))

# STEP 4: Set edges
graph.set_entry_point("research")
graph.add_edge("research", "draft")
graph.add_edge("draft", END)

# STEP 5: Run the graph
if __name__ == "__main__":
    query = input("Enter a research topic: ")
    workflow = graph.compile()
    result = workflow.invoke({"query": query})
    print("\n--- Final Answer ---\n")
    print(result["answer"])