import os
from openai import OpenAI

SMART_CALENDAR_API_KEY = os.getenv("SMART_CALENDAR_API_KEY")
SMART_CALENDAR_ENDPOINT = "https://api.microsoft.com/v1/smart_calendar"

client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY")
)

def get_smart_calendar_response(data):
    headers = {
        "Authorization": f"Bearer {SMART_CALENDAR_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(SMART_CALENDAR_ENDPOINT, json=data, headers=headers)
    return response.json()

response = client.chat.completions.create(
    model="microsoft/Phi-3.5-mini-instruct",
    max_tokens=1024,
    temperature=0.7,
    top_p=1,
    extra_body={
        "top_k": 50
    },
    messages=[]
)

print(response.to_json())