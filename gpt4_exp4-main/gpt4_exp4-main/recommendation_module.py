import ollama


MODEL_NAME = "qwen2.5:latest"


def generate_recommendations(prompt):
    """
    Generate recommendations using Ollama.
    """

    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as error:
        print("\nOllama Error:")
        print(error)
        return ""