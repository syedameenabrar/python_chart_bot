import random
from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend access

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Connect to local MongoDB
db = client["chatbot_db"]  # Select database
collection = db["intents"]  # Select collection

def get_response(user_input):
    user_input = user_input.lower()

    # Find a matching pattern in MongoDB
    intent = collection.find_one({"patterns": {"$in": [user_input]}})

    if intent:
        return random.choice(intent["responses"])
    else:
        return "I'm not sure about that. Can you rephrase?"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    bot_response = get_response(user_message)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
