import os
from dotenv import load_dotenv

load_dotenv()

class EnvConfig:
    UI_BASE_URL = os.getenv("UI_BASE_URL")
    API_BASE_URL = os.getenv("API_BASE_URL")
