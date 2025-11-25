from flask import Flask, request, Response
import os

app = Flask(__name__)
VERIFY_TOKEN = "money_honey_secret_123"


# --------------- VERIFY WEBHOOK (META HANDSHAKE) ---------------
@app.get("/webhook")
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        print("✅ WEBHOOK_VERIFIED")
        # Return challenge EXACTLY as Meta sent it
        return Response(challenge, status=200, mimetype="text/plain")

    return Response("Forbidden", status=403)


# --------------- HANDLE INCOMING MESSAGES ---------------
@app.post("/webhook")
def handle_messages():
    return Response("EVENT_RECEIVED", status=200)


# --------------- RENDER PORT CONFIG ---------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
