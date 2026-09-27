from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

from bot import answer_question

app = Flask(__name__)
CORS(app)  # allow browser requests


# Serve the chat page at the root URL
@app.route("/")
def home():
    return send_from_directory(".", "index.html")


# The API endpoint the frontend calls
@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    question = (data or {}).get("question", "").strip()
    history = (data or {}).get("history", [])

    if not question:
        return jsonify({"error": "Please enter a question."}), 400

    try:
        answer = answer_question(question, history)

        chart = None

        if "CHART_DATA:" in answer:
            chart_text = answer.split("CHART_DATA:", 1)[1].strip()

            chart = {
                "type": "bar",
                "labels": [],
                "values": []
            }

            for line in chart_text.splitlines():

                if line.startswith("type:"):
                    chart["type"] = line.replace("type:", "", 1).strip()

                elif line.startswith("labels:"):
                    chart["labels"] = [
                        x.strip()
                        for x in line.replace("labels:", "", 1).split(",")
                    ]

                elif line.startswith("values:"):
                    chart["values"] = [
                        int(x.strip())
                        for x in line.replace("values:", "", 1).split(",")
                    ]

            answer = answer.split("CHART_DATA:", 1)[0].strip()

        return jsonify({
            "answer": answer,
            "chart": chart
        })

    except Exception as e:
        print("Error:", e)
        return jsonify({
            "error": "Something went wrong on the server."
        }), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)