def collect_user_profile():

    print("\n" + "=" * 50)
    print("       PERSONALIZED RECOMMENDATION SYSTEM")
    print("=" * 50)

    print("\nEnter User Profile\n")

    name = input("Name: ").strip()
    age = input("Age: ").strip()
    background = input(
        "Educational/Professional Background: "
    ).strip()

    interests = input("Interests: ").strip()

    skill_level = input("Skill Level: ").strip()

    preference = input(
        "Preferred Category/Type: "
    ).strip()

    goal = input("Goal: ").strip()

    while True:
        try:
            num_recommendations = int(
                input("Number of Recommendations: ").strip()
            )

            if num_recommendations > 0:
                break

            print("Please enter a number greater than 0.")

        except ValueError:
            print("Please enter a valid number.")

    return {
        "name": name,
        "age": age,
        "background": background,
        "interests": interests,
        "skill_level": skill_level,
        "preference": preference,
        "goal": goal,
        "num_recommendations": num_recommendations
    }


def display_profile(profile):

    print("\n" + "=" * 50)
    print("              USER PROFILE")
    print("=" * 50)

    print(f"Name                   : {profile['name']}")
    print(f"Age                    : {profile['age']}")
    print(f"Background             : {profile['background']}")
    print(f"Interests              : {profile['interests']}")
    print(f"Skill Level            : {profile['skill_level']}")
    print(f"Preference             : {profile['preference']}")
    print(f"Goal                   : {profile['goal']}")
    print(
        f"No. of Recommendations : "
        f"{profile['num_recommendations']}"
    )