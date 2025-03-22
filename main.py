import os
from dotenv import load_dotenv
from fastapi import FastAPI

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Access environment variables
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL")

# ...existing code...

@app.get("/")
def read_root():
    return {"message": "Welcome to Everydai-Hub"}

# ...existing code...
