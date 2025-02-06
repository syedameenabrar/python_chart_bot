from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Predefined chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm here to assist you."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["Sorry, I don't understand. Can you rephrase?"]
}

# Chatbot endpoint
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()

    # Find response based on user input
    for key in responses:
        if key in user_input:
            return jsonify({"response": random.choice(responses[key])})
    
    return jsonify({"response": random.choice(responses["default"])})

if __name__ == "__main__":
    app.run(debug=True)
