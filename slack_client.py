import requests
import os
from dotenv import load_dotenv

load_dotenv()
SLACK_TOKEN = os.getenv("SLACK_TOKEN")

def get_channel_messages(channel_id, limit=20):
    response = requests.get(
        "https://slack.com/api/conversations.history",
        headers={"Authorization": f"Bearer {SLACK_TOKEN}"},
        params={"channel": channel_id, "limit": limit}
    )
    data = response.json()
    return data.get("messages", [])
