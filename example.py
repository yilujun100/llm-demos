from openai import OpenAI
import config

# 初始化 OpenAI 客户端
client = OpenAI(
    base_url=config.OPENAI_BASE_URL,
    api_key=config.OPENAI_API_KEY
)

response = client.responses.create(
    model='gpt-5-nano',
    input='Write a one-sentence bedtime story about a unicorn.'
)

print('>>>', response.output_text)
# Under the moonlit quilt of night, a gentle unicorn trotted to a quiet glade, curled up on a bed of moss, and drifted off to dream of silver streams and dawn-lit rainbows.
