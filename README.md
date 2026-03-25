# Agentic Reflexion Loop with Automated Evaluation

## 🚀 Overview
This repository demonstrates a **Compound AI System** designed to solve complex coding tasks through a self-correcting **Reflexion Architecture**. Built using **LangGraph**, the agent doesn't just generate code; it critiques its own work and iterates until the output is functionally sound.

To ensure production reliability, the system includes an **Immutable Evaluator** harness that validates generated Python code in an isolated execution environment, integrated directly with **LangSmith** for full-trace observability.

---

## 🏗️ Architecture

### 1. Stateful Orchestration (LangGraph)
The agent follows a directed cyclic graph (DCG) pattern:
*   **Designer Node:** Generates initial Python logic using `Gemini 2.5 Flash`.
*   **Critic Node:** Performs a "harsh" review of the code, identifying logic gaps or inefficiencies.
*   **Conditional Edges:** Logic that determines if the code requires a rewrite or is ready for delivery based on iteration count and critique quality.

### 2. Automated Evaluation (LangSmith)
Every agent run is automatically tracked and scored.
*   **Execution Sandbox:** Uses a Python `exec()` wrapper to verify the code runs without runtime errors.
*   **Binary Scoring:** Maps execution success to a `1.0` or `0.0` score in the LangSmith dashboard.
*   **Trace Visibility:** Provides deep-dive metrics into latency per node and total token consumption (OpEx).

---

## 🛠️ Tech Stack
*   **Framework:** LangGraph (Stateful Agents)
*   **LLM:** Google Gemini 2.5 Flash
*   **Observability:** LangSmith
*   **Inference Strategy:** Designed for vLLM / OpenAI-compatible API compatibility.

---

## 🚦 Getting Started

### Prerequisites
1. Get a free API Key from [Google AI Studio](https://aistudio.google.com/).
2. Get a [LangSmith API Key](https://smith.langchain.com/).

### Installation
```bash
git clone [https://github.com/kmzet/ai-agent-reflexion.git](https://github.com/kmzet/ai-agent-reflexion.git)
cd ai-agent-reflexion
pip install -r requirements.txt
