import os
import requests
from openai import OpenAI

MEAL_PLANNER_API_KEY = os.getenv("MEAL_PLANNER_API_KEY")
MEAL_PLANNER_ENDPOINT = "https://api.meta-llama.com/v1/meal_planner"

client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY")
)

def get_meal_planner_response(data):
    headers = {
        "Authorization": f"Bearer {MEAL_PLANNER_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(MEAL_PLANNER_ENDPOINT, json=data, headers=headers)
    return response.json()

response = client.chat.completions.create(
    model="meta-llama/Llama-3.2-3B-Instruct",
    temperature=0,
    messages=[]
)

print(response.to_json())