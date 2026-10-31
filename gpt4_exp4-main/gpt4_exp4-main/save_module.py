import os
from datetime import datetime


def save_recommendations(recommendations):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    file_path = os.path.join(
        "outputs",
        "recommendations.txt"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(
            "PERSONALIZED RECOMMENDATIONS\n"
        )

        file.write(
            "=" * 50 + "\n\n"
        )

        file.write(
            f"Saved On: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        for index, item in enumerate(
            recommendations,
            start=1
        ):

            file.write(
                f"{index}. {item['name']}\n"
            )

            file.write(
                f"Suitability Score: "
                f"{item['score']}%\n"
            )

            file.write(
                f"Reason: {item['reason']}\n\n"
            )

    print(
        f"\nRecommendations saved successfully!"
    )

    print(
        f"File: {file_path}"
    )