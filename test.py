import os
from dotenv import load_dotenv
from google import genai

# Load the API key from .env
load_dotenv()

# Create the client (it reads GEMINI_API_KEY automatically)
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Send a prompt
response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Say hello and tell me one fun fact about engineering."
)

print(response.text)