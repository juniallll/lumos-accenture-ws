import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

endpoint = "https://lumos-ws.services.ai.azure.com/openai/v1/"
model_name = "Kimi-K2.6"
deployment_name = "Kimi-K2.6"

api_key = os.getenv("AZURE_OPENAI_API_KEY")

if not api_key:
    raise ValueError("API Key not found. Please check your .env file.")

client = OpenAI(
    base_url=endpoint,
    api_key=api_key
)

completion = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?",
        }
    ],
)

print(completion.choices[0].message.content)