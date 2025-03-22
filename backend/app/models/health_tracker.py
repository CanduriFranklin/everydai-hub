import os
import requests
from openai import OpenAI

HEALTH_TRACKER_API_KEY = os.getenv("HEALTH_TRACKER_API_KEY")
HEALTH_TRACKER_ENDPOINT = "https://api.aaditya.com/v1/health_tracker"

client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY")
)

def get_health_tracker_response(data):
    headers = {
        "Authorization": f"Bearer {HEALTH_TRACKER_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(HEALTH_TRACKER_ENDPOINT, json=data, headers=headers)
    return response.json()

response = client.chat.completions.create(
    model="aaditya/Llama3-OpenBioLLM-8B",
    temperature=0,
    messages=[]
)

print(response.to_json())