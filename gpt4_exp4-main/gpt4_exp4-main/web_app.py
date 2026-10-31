from flask import Flask, render_template, request, jsonify
from input_module import collect_user_profile
from profile_module import analyze_profile
from prompt_module import construct_prompt
from recommendation_module import generate_recommendations
from ranking_module import extract_recommendations, rank_recommendations
from feedback_module import create_refinement_prompt
from intent_module import detect_intent
from save_module import save_recommendations


app = Flask(__name__)


# ============================================================
# HOME PAGE
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# GENERATE RECOMMENDATIONS
# ============================================================

@app.route("/generate", methods=["POST"])
def generate():

    try:

        data = request.get_json()

        profile = {
            "name": data.get("name", ""),
            "age": data.get("age", ""),
            "background": data.get("background", ""),
            "interests": data.get("interests", ""),
            "skill_level": data.get("skill_level", ""),
            "preference": data.get("preference", ""),
            "goal": data.get("goal", ""),
            "num_recommendations": int(
                data.get("num_recommendations", 4)
            )
        }

        # Analyze profile
        analysis = analyze_profile(profile)

        # Construct GPT/Ollama prompt
        prompt = construct_prompt(
            profile,
            analysis
        )

        # Generate recommendation
        response = generate_recommendations(prompt)

        # Extract recommendations
        recommendations = extract_recommendations(
            response
        )

        # Rank recommendations
        recommendations = rank_recommendations(
            recommendations
        )

        return jsonify({
            "success": True,
            "profile": profile,
            "analysis": analysis,
            "prompt": prompt,
            "recommendations": recommendations
        })

    except Exception as error:

        return jsonify({
            "success": False,
            "error": str(error)
        })


# ============================================================
# REFINE RECOMMENDATIONS
# ============================================================

@app.route("/refine", methods=["POST"])
def refine():

    try:

        data = request.get_json()

        profile = data.get("profile", {})
        recommendations = data.get(
            "recommendations",
            []
        )
        feedback = data.get(
            "feedback",
            ""
        )

        # Create refinement prompt
        prompt = create_refinement_prompt(
            profile,
            recommendations,
            feedback
        )

        # Generate refined recommendations
        response = generate_recommendations(
            prompt
        )

        # Extract recommendations
        refined = extract_recommendations(
            response
        )

        # Rank recommendations
        refined = rank_recommendations(
            refined
        )

        return jsonify({
            "success": True,
            "recommendations": refined,
            "response": response
        })

    except Exception as error:

        return jsonify({
            "success": False,
            "error": str(error)
        })


# ============================================================
# INTENT DETECTION
# ============================================================

@app.route("/intent", methods=["POST"])
def intent():

    try:

        data = request.get_json()

        user_input = data.get(
            "input",
            ""
        )

        detected_intent = detect_intent(
            user_input
        )

        return jsonify({
            "success": True,
            "intent": detected_intent
        })

    except Exception as error:

        return jsonify({
            "success": False,
            "error": str(error)
        })


# ============================================================
# SAVE RECOMMENDATIONS
# ============================================================

@app.route("/save", methods=["POST"])
def save():

    try:

        data = request.get_json()

        recommendations = data.get(
            "recommendations",
            []
        )

        save_recommendations(
            recommendations
        )

        return jsonify({
            "success": True,
            "message": "Recommendations saved successfully."
        })

    except Exception as error:

        return jsonify({
            "success": False,
            "error": str(error)
        })


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    print("\n" + "=" * 60)
    print("     PERSONALIZED RECOMMENDATION WEB APPLICATION")
    print("=" * 60)

    print("\nServer starting...")
    print("Open your browser and visit:")
    print("http://127.0.0.1:5000")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )