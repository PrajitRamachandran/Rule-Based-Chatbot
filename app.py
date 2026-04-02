from flask import Flask, render_template, request, jsonify
from chatbot.logic import get_response
from chatbot.memory import get_history

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

@app.route("/history", methods=["GET"])
def history():
    return jsonify(get_history())

if __name__ == "__main__":
    app.run(debug=True)