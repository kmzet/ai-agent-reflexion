import os
from langsmith import Client
from langsmith.evaluation import evaluate
from agent import app

# Initialize the LangSmith client
client = Client()

# ---------------------------------------------------------
# 1. The Dataset (The Ground Truth)
# ---------------------------------------------------------
# We define a strict coding challenge that the agent MUST solve.
dataset_name = "Python_Reflexion_Test"

# (Run this once to create the dataset in LangSmith)
if not client.has_dataset(dataset_name=dataset_name):
    dataset = client.create_dataset(dataset_name, description="Test suite for AutoResearch")
    client.create_example(
        inputs={"coding_prompt": "Write a Python function to calculate the Fibonacci sequence up to N."},
        outputs={"expected_behavior": "Must return a valid list of integers without syntax errors."},
        dataset_id=dataset.id,
    )

# ---------------------------------------------------------
# 2. The Target Function (Your Agent)
# ---------------------------------------------------------
def run_reflexion_agent(inputs: dict) -> dict:
    """Takes the LangSmith prompt, runs it through LangGraph, and extracts the code."""
    prompt = inputs["coding_prompt"]
    
    # MATCH THE AGENT STATE: Use "task"
    initial_state = {"task": prompt}
    
    # Invoke the graph
    final_state = app.invoke(initial_state)
    
    # MATCH THE AGENT STATE: Extract "draft"
    # We also strip out Markdown formatting (like ```python) so exec() doesn't choke
    final_code_string = final_state.get("draft", "").replace("```python", "").replace("```", "")
    
    return {"final_code": final_code_string}

# ---------------------------------------------------------
# 3. The Evaluator (The Judge)
# ---------------------------------------------------------
def execution_evaluator(run, example) -> dict:
    """Checks if the agent's generated code executes without runtime errors."""
    
    # ADD THIS SAFETY CHECK: Did the agent crash before outputting anything?
    if not run.outputs or "final_code" not in run.outputs:
        return {"key": "execution_valid", "score": 0, "comment": "Agent crashed before generating code."}
    
    agent_output = run.outputs["final_code"]
    
    try:
        exec(agent_output, {})
        score = 1
        reason = "Code executed without throwing an exception."
    except Exception as e:
        score = 0
        reason = f"Execution failed with error: {type(e).__name__} - {str(e)}"
        
    return {"key": "execution_valid", "score": score, "comment": reason}

# ---------------------------------------------------------
# 4. The Auto-Run
# ---------------------------------------------------------
if __name__ == "__main__":
    print("Running Automated Evaluation Loop...")
    experiment_results = evaluate(
        run_reflexion_agent, # The AI
        data=dataset_name,   # The Test
        evaluators=[execution_evaluator], # The Judge
        experiment_prefix="reflexion-test-run"
    )
    print("Evaluation complete. Check your LangSmith Dashboard!")
