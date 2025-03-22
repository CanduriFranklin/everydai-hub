import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY")
)

response = client.chat.completions.create(
    model="mistralai/Mixtral-8x7B-Instruct-v0.1",
    max_tokens=512,
    temperature=0.5,
    top_p=0.9,
    extra_body={
        "top_k": 50
    },
    messages=[]
)

print(response.to_json())