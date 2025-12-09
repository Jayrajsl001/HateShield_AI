# app/config.py
import os
from dotenv import load_dotenv

load_dotenv()

API_TITLE = "HateShield AI API"
API_VERSION = "0.1.0"

# Optional: MongoDB URI (for later)
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "hate_shield_ai")
