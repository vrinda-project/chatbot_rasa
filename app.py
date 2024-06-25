from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"  # Adjust this URL to your Rasa server's URL and port

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message = request.json.get("message")
    sender_id = request.json.get("sender", "default")

    response = requests.post(RASA_URL, json={"sender": sender_id, "message": user_message})

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000)
