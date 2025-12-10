from openai import OpenAI
from config import OPENAI_BASE_URL, OPENAI_API_KEY

client = OpenAI(
    base_url=OPENAI_BASE_URL,
    api_key=OPENAI_API_KEY
)

completion = client.chat.completions.create(
    model='gpt-5-nano',
    messages=[
        {
            'role': 'system',
            'content': 'You are a happy little helper'
        },
        {
            'role': 'user',
            'content': 'Help me generate a 200-word experience of participating in the parent-teacher conference'
        }
    ]
)

print(completion.choices[0].message.content)
