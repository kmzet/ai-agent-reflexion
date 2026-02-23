from openai import OpenAI

# POINTING TO INTERNAL INFRASTRUCTURE
client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="EMPTY",
)

print("--- Connecting to GKE Inference Server (Raw Completion) ---")

try:
    # FIX: We use 'completions' (Legacy), not 'chat.completions'
    # Because OPT-1.3B is a Base Model, not a Chat Model.
    response = client.completions.create(
        model="facebook/opt-1.3b",
        prompt="The capital of France is", # We provide the start of the sentence
        max_tokens=20,
        temperature=0.7
    )

    print("\nModel Response:")
    # The output format is also slightly different (text vs message)
    print(response.choices[0].text.strip())

    print("\n\n--- Success! ---")

except Exception as e:
    print(f"\n[ERROR] {e}")
