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

    if not question:
        return jsonify({"error": "Please enter a question."}), 400

    try:
        answer = answer_question(question)
        return jsonify({"answer": answer})
    except Exception as e:
        print("Error:", e)
        return jsonify({"error": "Something went wrong on the server."}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
