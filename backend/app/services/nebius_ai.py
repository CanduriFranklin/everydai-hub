import os
import requests

NEBIUS_AI_API_KEY = os.getenv("NEBIUS_AI_API_KEY")
NEBIUS_AI_ENDPOINT = os.getenv("NEBIUS_AI_ENDPOINT")

def get_nebius_ai_prediction(data):
    headers = {
        "Authorization": f"Bearer {NEBIUS_AI_API_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(NEBIUS_AI_ENDPOINT, json=data, headers=headers)
    return response.json()

class NebiusAIService:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def perform_inference(self, data: dict):
        return get_nebius_ai_prediction(data)
