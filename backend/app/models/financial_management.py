import os
from openai import OpenAI
import requests

FINANCIAL_MANAGEMENT_API_KEY = os.getenv("FINANCIAL_MANAGEMENT_API_KEY")
FINANCIAL_MANAGEMENT_ENDPOINT = "https://api.microsoft.com/v1/financial_management"

client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY")
)

def get_financial_management_response(data):
    headers = {
        "Authorization": f"Bearer {FINANCIAL_MANAGEMENT_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(FINANCIAL_MANAGEMENT_ENDPOINT, json=data, headers=headers)
    return response.json()

response = client.chat.completions.create(
    model="microsoft/Phi-3.5-MoE-instruct",
    max_tokens=1024,
    temperature=0.7,
    top_p=1,
    extra_body={
        "top_k": 50
    },
    messages=[]
)

print(response.to_json())