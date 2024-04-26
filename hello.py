from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

response = openai.ChatCompletion.Create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", 
        "content": "Helllo World!"}
    ]
)

print(response['choice'][0].message.content)