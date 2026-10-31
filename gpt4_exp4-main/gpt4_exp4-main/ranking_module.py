import re


def extract_recommendations(response):
    """
    Extract recommendation name, score and reason
    from the Ollama response.
    """

    recommendations = []

    # Split response into recommendation blocks
    blocks = re.split(
        r'(?=\d+\.\s*(?:\*\*)?Recommendation\s+Name)',
        response,
        flags=re.IGNORECASE
    )

    for block in blocks:

        # Ignore empty blocks
        if not block.strip():
            continue

        # ------------------------------------------
        # Extract Recommendation Name
        # ------------------------------------------

        name_match = re.search(
            r'Recommendation\s+Name\s*:\s*(.+?)(?=\n)',
            block,
            re.IGNORECASE
        )

        # ------------------------------------------
        # Extract Suitability Score
        # ------------------------------------------

        score_match = re.search(
            r'Suitability\s+Score\s*:\s*(\d+)',
            block,
            re.IGNORECASE
        )

        # ------------------------------------------
        # Extract Reason
        # ------------------------------------------

        reason_match = re.search(
            r'Reason\s*:\s*(.*)',
            block,
            re.IGNORECASE | re.DOTALL
        )

        # Make sure all three fields exist
        if name_match and score_match and reason_match:

            name = clean_text(
                name_match.group(1)
            )

            reason = clean_text(
                reason_match.group(1)
            )

            try:
                score = int(
                    score_match.group(1)
                )
            except ValueError:
                score = 0

            recommendations.append({
                "name": name,
                "score": score,
                "reason": reason
            })

    return recommendations


def clean_text(text):
    """
    Remove unnecessary formatting characters.
    """

    text = text.strip()

    # Remove Markdown bold
    text = text.replace("**", "")

    # Remove quotation marks
    text = text.replace('"', '')

    # Remove leading bullet characters
    text = re.sub(
        r'^\s*[-*]\s*',
        '',
        text
    )

    # Remove extra spaces/newlines
    text = re.sub(
        r'\s+',
        ' ',
        text
    )

    return text.strip()


def rank_recommendations(recommendations):
    """
    Sort recommendations from highest
    suitability score to lowest.
    """

    recommendations.sort(
        key=lambda item: item["score"],
        reverse=True
    )

    return recommendations


def display_ranking(recommendations):
    """
    Display recommendations in ranked order.
    """

    print("\n" + "=" * 65)
    print("              RECOMMENDATION RANKING")
    print("=" * 65)

    print(
        f"{'Rank':<8}"
        f"{'Recommendation':<40}"
        f"{'Score':<10}"
    )

    print("-" * 65)

    for index, item in enumerate(
        recommendations,
        start=1
    ):

        name = item["name"]

        # Shorten long names for table display
        if len(name) > 38:
            name = name[:35] + "..."

        print(
            f"{index:<8}"
            f"{name:<40}"
            f"{item['score']}%"
        )