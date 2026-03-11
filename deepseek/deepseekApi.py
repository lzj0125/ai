# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

client = OpenAI(
    #api_key=os.environ.get('sk-e3e0b17863794af0a38ff5a8dd86dd1d'),
    api_key='sk-e3e0b17863794af0a38ff5a8dd86dd1d',
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=False
)

print(response.choices[0].message.content)