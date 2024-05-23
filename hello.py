from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
import os

OPENAI_API_KEY = os.getenv("SAM_OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", 
        "content": "Helllo World!"}
    ]
)

print(response.choices[0].message.content)