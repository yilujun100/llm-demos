import requests
import json
from config import OPENAI_API_KEY

url = 'https://xiaoai.plus/v1/chat/completions'

requests_data = json.dumps({
    'messages': [
        {
            'role': 'system',
            'content': 'You are a large language model robot'
        },
        {
            'role': 'user',
            'content': 'Tell me what the U.S. GDP will be in 2022?'
        }
    ],
    'stream': False,
    'model': 'gpt-5-nano',
    # 'temperature': 0.5,
    # 'presence_penalty': 0.2,
    # 'frequency_penalty': 0.2,
    # 'top_p': 1
})

headers = {
    'Authorization': f'Bearer {OPENAI_API_KEY}',
    'Content-Type': 'application/json'
}

response = requests.request('POST', url, headers=headers, data=requests_data)
data = response.json()
print('>>>response text:', response.text)
print('>>>content:', data['choices'][0]['message']['content'])
