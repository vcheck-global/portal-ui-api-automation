import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()


class Config:
    BASE_URL = os.getenv("BASE_URL")
    API_URL = os.getenv("API_URL")
    EMAIL = os.getenv("EMAIL")
    PASSWORD = os.getenv("PASSWORD")
