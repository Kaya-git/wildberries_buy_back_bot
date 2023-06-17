import os
from dotenv import load_dotenv


load_dotenv()
# Database
DB_USER=os.environ.get("DB_USER")
DB_HOST=os.environ.get("DB_HOST")
DB_PASS=os.environ.get("DB_PASS")
DB_NAME=os.environ.get("DB_NAME")
DB_PORT=os.environ.get("DB_PORT")

# Telegram
BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")
