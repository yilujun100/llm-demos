from openai import OpenAI
from config import OPENAI_BASE_URL, OPENAI_API_KEY

client = OpenAI(
    base_url=OPENAI_BASE_URL,
    api_key=OPENAI_API_KEY
)

# turn text into numbers
response = client.embeddings.create(
    model='text-embedding-3-small',
    input='I like AI large model development',
    dimensions=512
)

print(response.data[0].embedding)  # [0.01635017618536949, -0.031141765415668488, 0.024682622402906418, ...]
print(len(response.data[0].embedding))  # 1536
