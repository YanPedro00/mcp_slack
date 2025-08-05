from flask import Flask, jsonify, request
from slack_client import get_channel_messages

app = Flask(__name__)

@app.route("/slack/messages", methods=["GET"])
def slack_messages():
    channel_id = request.args.get("channel_id")
    if not channel_id:
        return jsonify({"error": "channel_id is required"}), 400

    messages = get_channel_messages(channel_id)
    return jsonify(messages)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
