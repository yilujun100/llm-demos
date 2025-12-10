from openai import OpenAI
from config import OPENAI_BASE_URL, OPENAI_API_KEY
import numpy as np

client = OpenAI(
    base_url=OPENAI_BASE_URL,
    api_key=OPENAI_API_KEY
)


def get_embedding(text, model='text-embedding-3-small'):
    return client.embeddings.create(input=text, model=model).data[0].embedding


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
