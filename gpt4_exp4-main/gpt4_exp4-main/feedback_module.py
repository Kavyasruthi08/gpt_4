def collect_feedback():

    print("\n" + "=" * 65)
    print("              USER FEEDBACK")
    print("=" * 65)

    feedback = input(
        "Enter your feedback: "
    ).strip()

    return feedback


def create_refinement_prompt(
    profile,
    recommendations,
    feedback
):

    current_recommendations = ""

    for index, item in enumerate(
        recommendations,
        start=1
    ):

        current_recommendations += (
            f"{index}. {item['name']} - "
            f"Score: {item['score']} - "
            f"Reason: {item['reason']}\n"
        )

    prompt = f"""
You are a personalized recommendation assistant.

USER PROFILE
Name: {profile['name']}
Age: {profile['age']}
Background: {profile['background']}
Interests: {profile['interests']}
Skill Level: {profile['skill_level']}
Preferred Category: {profile['preference']}
Goal: {profile['goal']}

CURRENT RECOMMENDATIONS
{current_recommendations}

USER FEEDBACK
{feedback}

TASK
Refine the recommendations according to the user's feedback.

Keep recommendations relevant to the user's goal.
Remove resources that conflict with the feedback.
Prioritize beginner-friendly and practical resources.

Return exactly {profile['num_recommendations']} recommendations.

Use this format:

1. Recommendation Name: <name>
Suitability Score: <number>
Reason: <reason>

2. Recommendation Name: <name>
Suitability Score: <number>
Reason: <reason>
"""

    return prompt