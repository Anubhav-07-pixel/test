from flask import Flask, request, make_response

app = Flask(__name__)

# Verify Token wahi jo Meta Dashboard me hai
VERIFY_TOKEN = "money_honey_secret_123"

@app.route('/webhook', methods=['GET'])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    # Check agar token match karta hai
    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("✅ WEBHOOK_VERIFIED")
        
        # --- FIX: Force response to be Plain Text ---
        challenge_text = str(challenge).strip()
        response = make_response(challenge_text, 200)
        response.headers["Content-Type"] = "text/plain"
        return response
    
    # Agar match nahi kiya
    return "Forbidden", 403

@app.route('/webhook', methods=['POST'])
def handle_messages():
    return "EVENT_RECEIVED", 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
