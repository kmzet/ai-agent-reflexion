import os
from typing import List, TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END

# 1. DEFINE THE STATE
class AgentState(TypedDict):
    task: str
    draft: str
    critique: str
    iterations: int

# 2. INITIALIZE YOUR ENDPOINT
# We use gemini-1.5-flash because it is extremely fast and free
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# 3. DEFINE THE NODES (THE BUILDER STEPS)
def designer_node(state: AgentState):
    """Generates the initial code based on the task."""
    prompt = f"Write a high-performance Python function for: {state['task']}. Provide only the code."
    res = llm.invoke(prompt)
    return {"draft": res.content, "iterations": state.get("iterations", 0) + 1}

def critic_node(state: AgentState):
    """Critiques the code and finds potential bugs."""
    prompt = f"Critique this Python code for bugs and efficiency. Be harsh:\n{state['draft']}"
    res = llm.invoke(prompt)
    return {"critique": res.content}

# 4. DEFINE THE LOGIC (THE EDGES)
def should_continue(state: AgentState):
    if state["iterations"] > 2: # Stop after 2 attempts to save API calls
        return END
    return "critic"

# 5. BUILD THE GRAPH
workflow = StateGraph(AgentState)
workflow.add_node("designer", designer_node)
workflow.add_node("critic", critic_node)

workflow.set_entry_point("designer")
workflow.add_conditional_edges("designer", should_continue)
workflow.add_edge("critic", "designer") # Loop back for a better draft

app = workflow.compile()

# ---------------------------------------------------------
# 6. THE EXECUTION GUARD (Only runs if executed directly)
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Running Agent in standalone mode...")
    test_inputs = {"task": "Write a Python script to calculate the Fibonacci sequence."}
    for output in app.stream(test_inputs):
        print(output)