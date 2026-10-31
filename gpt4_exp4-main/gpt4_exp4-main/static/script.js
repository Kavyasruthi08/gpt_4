let currentProfile = {};
let currentRecommendations = [];


// ============================================================
// GENERATE RECOMMENDATIONS
// ============================================================

async function generateRecommendations() {

    const data = {

        name: document.getElementById("name").value,

        age: document.getElementById("age").value,

        background:
            document.getElementById("background").value,

        interests:
            document.getElementById("interests").value,

        skill_level:
            document.getElementById("skill_level").value,

        preference:
            document.getElementById("preference").value,

        goal:
            document.getElementById("goal").value,

        num_recommendations:
            document.getElementById("num_recommendations").value
    };


    if (!data.name || !data.age || !data.interests || !data.goal) {

        alert("Please fill in the required fields.");

        return;
    }


    showStatus("Generating personalized recommendations...");


    try {

        const response = await fetch(
            "/generate",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(data)
            }
        );


        const result = await response.json();


        if (!result.success) {

            showStatus(
                "Error: " + result.error
            );

            return;
        }


        currentProfile = result.profile;

        currentRecommendations =
            result.recommendations;


        displayProfile(
            result.profile
        );


        displayAnalysis(
            result.analysis
        );


        displayRecommendations(
            result.recommendations
        );


        displayRanking(
            result.recommendations
        );


        document
            .getElementById("profileSection")
            .classList.remove("hidden");


        document
            .getElementById("analysisSection")
            .classList.remove("hidden");


        document
            .getElementById("recommendationSection")
            .classList.remove("hidden");


        document
            .getElementById("rankingSection")
            .classList.remove("hidden");


        document
            .getElementById("feedbackSection")
            .classList.remove("hidden");


        document
            .getElementById("actionsSection")
            .classList.remove("hidden");


        showStatus(
            "Recommendations generated successfully!"
        );

    }

    catch (error) {

        showStatus(
            "Error connecting to server: " +
            error
        );
    }
}


// ============================================================
// DISPLAY PROFILE
// ============================================================

function displayProfile(profile) {

    const output =
        document.getElementById(
            "profileOutput"
        );


    output.innerHTML = `

        <div class="profile-item">
            <strong>Name:</strong>
            ${profile.name}
        </div>

        <div class="profile-item">
            <strong>Age:</strong>
            ${profile.age}
        </div>

        <div class="profile-item">
            <strong>Background:</strong>
            ${profile.background}
        </div>

        <div class="profile-item">
            <strong>Interests:</strong>
            ${profile.interests}
        </div>

        <div class="profile-item">
            <strong>Skill Level:</strong>
            ${profile.skill_level}
        </div>

        <div class="profile-item">
            <strong>Preference:</strong>
            ${profile.preference}
        </div>

        <div class="profile-item">
            <strong>Goal:</strong>
            ${profile.goal}
        </div>

        <div class="profile-item">
            <strong>No. of Recommendations:</strong>
            ${profile.num_recommendations}
        </div>
    `;
}


// ============================================================
// DISPLAY ANALYSIS
// ============================================================

function displayAnalysis(analysis) {

    const output =
        document.getElementById(
            "analysisOutput"
        );


    let html = "";


    for (const key in analysis) {

        html += `

            <div class="analysis-item">

                <strong>
                    ${formatKey(key)}:
                </strong>

                ${analysis[key]}

            </div>
        `;
    }


    output.innerHTML = html;
}


// ============================================================
// DISPLAY RECOMMENDATIONS
// ============================================================

function displayRecommendations(
    recommendations
) {

    const output =
        document.getElementById(
            "recommendationOutput"
        );


    output.innerHTML = "";


    recommendations.forEach(
        (item, index) => {

            const div =
                document.createElement(
                    "div"
                );


            div.className =
                "recommendation";


            div.innerHTML = `

                <h3>
                    ${index + 1}.
                    ${item.name}
                </h3>

                <div class="score">
                    Suitability Score:
                    ${item.score}%
                </div>

                <div class="reason">

                    <strong>
                        Why this is suitable:
                    </strong>

                    ${item.reason}

                </div>
            `;


            output.appendChild(div);
        }
    );
}


// ============================================================
// DISPLAY RANKING
// ============================================================

function displayRanking(
    recommendations
) {

    const output =
        document.getElementById(
            "rankingOutput"
        );


    output.innerHTML = "";


    recommendations.forEach(
        (item, index) => {

            const row =
                document.createElement(
                    "tr"
                );


            row.innerHTML = `

                <td>
                    ${index + 1}
                </td>

                <td>
                    ${item.name}
                </td>

                <td>
                    ${item.score}%
                </td>
            `;


            output.appendChild(row);
        }
    );
}


// ============================================================
// REFINE RECOMMENDATIONS
// ============================================================

async function refineRecommendations() {

    const feedback =
        document.getElementById(
            "feedback"
        ).value;


    if (!feedback.trim()) {

        alert(
            "Please enter your feedback."
        );

        return;
    }


    showStatus(
        "Refining recommendations..."
    );


    try {

        const response =
            await fetch(
                "/refine",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        profile:
                            currentProfile,

                        recommendations:
                            currentRecommendations,

                        feedback:
                            feedback
                    })
                }
            );


        const result =
            await response.json();


        if (!result.success) {

            showStatus(
                "Error: " +
                result.error
            );

            return;
        }


        currentRecommendations =
            result.recommendations;


        displayRecommendations(
            result.recommendations
        );


        displayRanking(
            result.recommendations
        );


        showStatus(
            "Recommendations refined successfully!"
        );
    }

    catch (error) {

        showStatus(
            "Error: " + error
        );
    }
}


// ============================================================
// INTENT DETECTION
// ============================================================

async function detectIntent() {

    const input =
        document.getElementById(
            "intentInput"
        ).value;


    if (!input.trim()) {

        alert(
            "Enter a request first."
        );

        return;
    }


    try {

        const response =
            await fetch(
                "/intent",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        input: input
                    })
                }
            );


        const result =
            await response.json();


        if (!result.success) {

            document.getElementById(
                "intentOutput"
            ).innerText =
                "Error: " +
                result.error;

            return;
        }


        document.getElementById(
            "intentOutput"
        ).innerHTML = `

            Detected Intent:
            <strong>
                ${result.intent}
            </strong>
        `;
    }

    catch (error) {

        document.getElementById(
            "intentOutput"
        ).innerText =
            "Error: " + error;
    }
}


// ============================================================
// SHOW PROFILE
// ============================================================

function showProfile() {

    document
        .getElementById(
            "profileSection"
        )
        .classList.remove("hidden");


    document
        .getElementById(
            "profileSection"
        )
        .scrollIntoView({
            behavior: "smooth"
        });
}


// ============================================================
// SHOW EXPLANATIONS
// ============================================================

function showExplanations() {

    const section =
        document.getElementById(
            "recommendationSection"
        );


    section.classList.remove(
        "hidden"
    );


    section.scrollIntoView({
        behavior: "smooth"
    });
}


// ============================================================
// SAVE RECOMMENDATIONS
// ============================================================

async function saveRecommendations() {

    if (
        currentRecommendations.length === 0
    ) {

        alert(
            "Generate recommendations first."
        );

        return;
    }


    try {

        const response =
            await fetch(
                "/save",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        recommendations:
                            currentRecommendations
                    })
                }
            );


        const result =
            await response.json();


        if (result.success) {

            showStatus(
                "Recommendations saved successfully!"
            );

        }

        else {

            showStatus(
                "Error: " +
                result.error
            );
        }

    }

    catch (error) {

        showStatus(
            "Error: " + error
        );
    }
}


// ============================================================
// FORMAT KEY
// ============================================================

function formatKey(key) {

    return key
        .replace(/_/g, " ")
        .replace(/\b\w/g, letter =>
            letter.toUpperCase()
        );
}


// ============================================================
// STATUS
// ============================================================

function showStatus(message) {

    document.getElementById(
        "status"
    ).innerText = message;
}