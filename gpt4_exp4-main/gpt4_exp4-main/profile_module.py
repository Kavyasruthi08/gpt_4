def analyze_profile(profile):

    interests = [
        item.strip()
        for item in profile["interests"].split(",")
        if item.strip()
    ]

    if len(interests) >= 1:
        primary = interests[0]
    else:
        primary = "Not specified"

    if len(interests) >= 2:
        secondary = interests[1]
    else:
        secondary = "None"

    if len(interests) >= 3:
        other = ", ".join(interests[2:])
    else:
        other = "None"

    constraints = []

    if profile["skill_level"].lower() == "beginner":
        constraints.append(
            "Beginner-friendly recommendations"
        )

    if profile["preference"]:
        constraints.append(
            f"Prefer {profile['preference']} resources"
        )

    if constraints:
        constraint_text = "; ".join(constraints)
    else:
        constraint_text = "No specific constraints"

    return {
        "primary_interest": primary,
        "secondary_interest": secondary,
        "other_interests": other,
        "skill_level": profile["skill_level"],
        "goal": profile["goal"],
        "preference": profile["preference"],
        "constraints": constraint_text
    }


def display_analysis(analysis):

    print("\n" + "=" * 50)
    print("             PREFERENCE ANALYSIS")
    print("=" * 50)

    print(
        f"Primary Interest   : "
        f"{analysis['primary_interest']}"
    )

    print(
        f"Secondary Interest : "
        f"{analysis['secondary_interest']}"
    )

    print(
        f"Other Interests    : "
        f"{analysis['other_interests']}"
    )

    print(
        f"Skill Level        : "
        f"{analysis['skill_level']}"
    )

    print(
        f"Goal               : "
        f"{analysis['goal']}"
    )

    print(
        f"Preference         : "
        f"{analysis['preference']}"
    )

    print(
        f"Constraints        : "
        f"{analysis['constraints']}"
    )