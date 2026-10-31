def construct_prompt(profile, analysis):
    """
    Construct a personalized recommendation prompt.
    """

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

PREFERENCE ANALYSIS
Primary Interest: {analysis['primary_interest']}
Secondary Interest: {analysis['secondary_interest']}
Other Interests: {analysis.get('other_interests', 'None')}
Skill Level: {analysis['skill_level']}
Learning Goal: {analysis['goal']}
Preferred Type: {analysis['preference']}
Constraints: {analysis['constraints']}

TASK
Recommend exactly {profile['num_recommendations']} suitable learning
resources for this user.

IMPORTANT:
- Give realistic learning resources.
- Prioritize the user's goal and interests.
- Consider beginner skill level.
- Prefer practical and hands-on resources.
- Do not recommend unrelated resources.

For each recommendation provide:

1. Recommendation Name
2. Suitability Score from 0 to 100
3. Short Reason explaining why it is suitable

Use this exact format:

1. Recommendation Name: <name>
Suitability Score: <number>
Reason: <reason>

2. Recommendation Name: <name>
Suitability Score: <number>
Reason: <reason>

Return exactly {profile['num_recommendations']} recommendations.
"""

    return prompt


def display_prompt(prompt):
    print("\n" + "=" * 60)
    print("                 GPT PROMPT")
    print("=" * 60)
    print(prompt)