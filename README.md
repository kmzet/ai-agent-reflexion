# AI Agentic Reflexion: GKE + vLLM

A decoupled AI orchestration pattern that separates intelligence logic from inference infrastructure. This project uses a **Reflexion** loop to improve code generation quality through automated self-critique.

### 🏗 Infrastructure Backend
The inference layer for this agent is hosted on a self-managed GPU cluster. 
**See the Infrastructure Repo here:** (https://github.com/kmzet/vllmGKE)

### 🛠 The Stack
* **Infra:** GKE (Google Kubernetes Engine) with **NVIDIA L4 GPUs**.
* **Inference:** **vLLM** (OpenAI-compatible API).
* **Orchestration:** **LangGraph** (Stateful Graph).
* **Model:** Llama-3-8B

### 🧠 Logic Flow
* **Designer Node:** Generates initial Python logic based on user requirements.
* **Critic Node:** Conducts a "harsh" review for bugs, security, and efficiency.
* **Stateful Loop:** If the critic identifies issues, the state loops back for a re-draft until criteria is met.


### 🚀 Getting Started
1. **Infra:** Ensure the vLLM cluster is running via the infra repo linked above.
2. **Tunneling:** `kubectl port-forward svc/llama-3-8b-vllm 8000:8000`
3. **Execution:**
```bash
pip install -r requirements.txt
python agent.py
