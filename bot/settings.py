from os import getenv as ENV


TOKEN = ENV("BOT_TOKEN")

API_KEY = ENV("API_KEY", "1")
API_URL = ENV("API_URL", "http://api:8000")
