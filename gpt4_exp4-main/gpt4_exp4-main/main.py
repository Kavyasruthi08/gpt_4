from input_module import (
    collect_user_profile,
    display_profile
)

from profile_module import (
    analyze_profile,
    display_analysis
)

from prompt_module import (
    construct_prompt,
    display_prompt
)

from recommendation_module import (
    generate_recommendations
)

from ranking_module import (
    extract_recommendations,
    rank_recommendations,
    display_ranking
)

from explanation_module import (
    display_explanations
)

from feedback_module import (
    collect_feedback,
    create_refinement_prompt
)

from intent_module import (
    detect_intent
)

from save_module import (
    save_recommendations
)


def generate_initial_recommendations(
    profile,
    analysis
):

    prompt = construct_prompt(
        profile,
        analysis
    )

    display_prompt(prompt)

    print("\n" + "=" * 65)
    print(
        "          GENERATING RECOMMENDATIONS..."
    )
    print("=" * 65)

    response = generate_recommendations(
        prompt
    )

    if not response:

        print(
            "\nCould not generate recommendations."
        )

        return []

    print("\nGPT RESPONSE")
    print("-" * 65)
    print(response)

    recommendations = extract_recommendations(
        response
    )

    if not recommendations:

        print(
            "\nCould not process the GPT response."
        )

        return []

    recommendations = rank_recommendations(
        recommendations
    )

    display_ranking(
        recommendations
    )

    display_explanations(
        recommendations
    )

    return recommendations


def refine_recommendations(
    profile,
    recommendations,
    feedback
):

    prompt = create_refinement_prompt(
        profile,
        recommendations,
        feedback
    )

    print("\n" + "=" * 65)
    print(
        "             REFINING RECOMMENDATIONS"
    )
    print("=" * 65)

    response = generate_recommendations(
        prompt
    )

    if not response:

        print(
            "\nCould not generate refined recommendations."
        )

        return recommendations

    print("\nREFINED GPT RESPONSE")
    print("-" * 65)
    print(response)

    refined = extract_recommendations(
        response
    )

    if not refined:

        print(
            "\nCould not process refined recommendations."
        )

        return recommendations

    refined = rank_recommendations(
        refined
    )

    display_ranking(
        refined
    )

    display_explanations(
        refined
    )

    return refined


def main():

    # ==========================================
    # PART A - USER PROFILE COLLECTION
    # ==========================================

    profile = collect_user_profile()

    # ==========================================
    # DISPLAY PROFILE
    # ==========================================

    display_profile(profile)

    # ==========================================
    # PART B - PREFERENCE ANALYSIS
    # ==========================================

    analysis = analyze_profile(
        profile
    )

    display_analysis(
        analysis
    )

    # ==========================================
    # PART C, D, E, F
    # INITIAL RECOMMENDATIONS
    # ==========================================

    recommendations = (
        generate_initial_recommendations(
            profile,
            analysis
        )
    )

    if not recommendations:

        print(
            "\nNo recommendations generated."
        )

        return

    # ==========================================
    # PART G, H, I
    # CONTINUOUS INTERACTION
    # ==========================================

    while True:

        print("\n" + "=" * 65)
        print(
            "             ASSISTANT MENU"
        )
        print("=" * 65)

        print(
            "1. Generate Recommendation"
        )

        print(
            "2. Refine Recommendation"
        )

        print(
            "3. Show Profile"
        )

        print(
            "4. Explain Recommendation"
        )

        print(
            "5. Save Recommendation"
        )

        print(
            "6. Exit"
        )

        user_input = input(
            "\nEnter your request or command: "
        ).strip()

        if not user_input:

            print(
                "\nPlease enter a command."
            )

            continue

        # ==========================================
        # INTENT DETECTION
        # ==========================================

        intent = detect_intent(
            user_input
        )

        print(
            f"\nDetected Intent: {intent}"
        )

        # ==========================================
        # GENERATE
        # ==========================================

        if intent == "GENERATE_RECOMMENDATION":

            new_recommendations = (
                generate_initial_recommendations(
                    profile,
                    analysis
                )
            )

            if new_recommendations:

                recommendations = (
                    new_recommendations
                )

        # ==========================================
        # REFINE
        # ==========================================

        elif intent == "REFINE_RECOMMENDATION":

            feedback = user_input

            # If user entered menu option "2",
            # ask for actual feedback.
            if feedback == "2":

                feedback = collect_feedback()

            recommendations = (
                refine_recommendations(
                    profile,
                    recommendations,
                    feedback
                )
            )

        # ==========================================
        # SHOW PROFILE
        # ==========================================

        elif intent == "SHOW_PROFILE":

            display_profile(
                profile
            )

            display_analysis(
                analysis
            )

        # ==========================================
        # EXPLAIN
        # ==========================================

        elif intent == "EXPLAIN_RECOMMENDATION":

            display_explanations(
                recommendations
            )

        # ==========================================
        # SAVE
        # ==========================================

        elif intent == "SAVE_RECOMMENDATION":

            save_recommendations(
                recommendations
            )

        # ==========================================
        # EXIT
        # ==========================================

        elif intent == "EXIT":

            print("\n" + "=" * 65)

            print(
                "Thank you for using the "
                "Personalized Recommendation System!"
            )

            print("=" * 65)

            break

        # ==========================================
        # UNKNOWN
        # ==========================================

        else:

            print(
                "\nUnable to determine the requested action."
            )


if __name__ == "__main__":
    main()