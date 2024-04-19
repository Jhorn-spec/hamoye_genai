import openai

response = openai.ChatCompletion.Create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Helllo World!"}
    ]
)

print(response['choice'][0]['message']['content'])