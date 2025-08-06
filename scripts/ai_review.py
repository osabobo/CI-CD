import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def read_code(file_path):
    with open(file_path, "r") as file:
        return file.read()

code = read_code("app/app.py")

response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are a code reviewer. Identify improvements and bugs."},
        {"role": "user", "content": code}
    ]
)

print("AI Code Review Report:\n")
print(response['choices'][0]['message']['content'])