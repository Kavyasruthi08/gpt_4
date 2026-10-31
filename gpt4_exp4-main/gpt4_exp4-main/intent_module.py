import ollama


MODEL_NAME = "qwen2.5:latest"


def detect_intent(user_input):

    text = user_input.strip()

    # Direct menu number support
    menu_intents = {
        "1": "GENERATE_RECOMMENDATION",
        "2": "REFINE_RECOMMENDATION",
        "3": "SHOW_PROFILE",
        "4": "EXPLAIN_RECOMMENDATION",
        "5": "SAVE_RECOMMENDATION",
        "6": "EXIT"
    }

    if text in menu_intents:
        return menu_intents[text]

    prompt = f"""
Classify the user's request into exactly ONE of these intents:

GENERATE_RECOMMENDATION
REFINE_RECOMMENDATION
SHOW_PROFILE
EXPLAIN_RECOMMENDATION
SAVE_RECOMMENDATION
EXIT

User request:
{text}

Return ONLY the intent name.
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

        intent = response["message"]["content"].strip()

        valid_intents = [
            "GENERATE_RECOMMENDATION",
            "REFINE_RECOMMENDATION",
            "SHOW_PROFILE",
            "EXPLAIN_RECOMMENDATION",
            "SAVE_RECOMMENDATION",
            "EXIT"
        ]

        for valid in valid_intents:

            if valid in intent.upper():
                return valid

        return "UNKNOWN"

    except Exception as error:

        print(
            f"\nIntent detection error: {error}"
        )

        return "UNKNOWN"