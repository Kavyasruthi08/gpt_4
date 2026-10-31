def display_explanations(recommendations):

    print("\n" + "=" * 65)
    print("          RECOMMENDATION EXPLANATIONS")
    print("=" * 65)

    for index, item in enumerate(
        recommendations,
        start=1
    ):

        print(
            f"\n{index}. {item['name']}"
        )

        print(
            f"Suitability Score: "
            f"{item['score']}%"
        )

        print("Why this is suitable:")

        print(item["reason"])