from dotenv import load_dotenv
import os

load_dotenv(override=True)  # 强制覆盖系统环境变量

OPENAI_BASE_URL = os.getenv('OPENAI_BASE_URL')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
