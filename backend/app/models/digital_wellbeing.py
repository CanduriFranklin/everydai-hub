import os
from openai import OpenAI

client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=os.environ.get("NEBIUS_API_KEY")
)

response = client.chat.completions.create(
    model="microsoft/Phi-3-mini-4k-instruct",
    max_tokens=1024,
    temperature=0.7,
    top_p=1,
    extra_body={
        "top_k": 50
    },
    messages=[]
)

print(response.to_json())