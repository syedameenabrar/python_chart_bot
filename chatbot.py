import json
import random
from difflib import get_close_matches
from flask import Flask, request, jsonify
from flask_cors import CORS

# Load training data
with open("intents.json", "r") as file:
    intents = json.load(file)["intents"]

app = Flask(__name__)
CORS(app)  # Enables CORS for all routes

def get_response(user_input):
    user_input = user_input.lower()

    # Collect all patterns
    all_patterns = {pattern: intent["responses"] for intent in intents for pattern in intent["patterns"]}

    # Get the closest match (helps with partial inputs)
    matches = get_close_matches(user_input, all_patterns.keys(), n=1, cutoff=0.6)

    if matches:
        return random.choice(all_patterns[matches[0]])
    else:
        return "I'm not sure about that. Can you rephrase?"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extract the message from the JSON data
        user_message = data.get("message", "").strip()

        # Check if the message is empty
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        # Get a response from the chatbot
        bot_response = get_response(user_message)

        return jsonify({"response": bot_response})
    except Exception as e:
        return jsonify({"error": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
