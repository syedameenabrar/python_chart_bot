from flask import Flask, request, jsonify
import random
from difflib import get_close_matches

app = Flask(__name__)

# Predefined chatbot responses
responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "I'm here to assist you."],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "default": ["Sorry, I don't understand. Can you rephrase?"]
}

# Function to find the best matching response
def get_best_response(user_input):
    matches = get_close_matches(user_input, responses.keys(), n=1, cutoff=0.4)  # 40% similarity threshold
    if matches:
        return random.choice(responses[matches[0]])  # Return a response from the closest match
    return random.choice(responses["default"])

# Chatbot API
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    response = get_best_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
