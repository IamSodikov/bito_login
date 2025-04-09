from dotenv import load_dotenv
import os

load_dotenv()

LOGIN_URL = os.getenv("LOGIN_URL")
VALID_PHONE = os.getenv("PHONE")
VALID_PASSWORD = os.getenv("PASSWORD")