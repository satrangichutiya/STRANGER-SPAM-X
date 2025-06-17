import os
import logging
from telethon import TelegramClient
from decouple import config
from os import getenv

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# Basic values
API_ID = config("API_ID", cast=int)
API_HASH = config("API_HASH")
CMD_HNDLR = getenv("CMD_HNDLR", ".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
HEROKU_API_KEY = config("HEROKU_API_KEY", default=None)

# Bot Tokens (can be less than 10 — flexible)
BOT_TOKENS = [
    config("BOT_TOKEN", default=None),
    config("BOT_TOKEN2", default=None),
    config("BOT_TOKEN3", default=None),
    config("BOT_TOKEN4", default=None),
    config("BOT_TOKEN5", default=None),
    config("BOT_TOKEN6", default=None),
    config("BOT_TOKEN7", default=None),
    config("BOT_TOKEN8", default=None),
    config("BOT_TOKEN9", default=None),
    config("BOT_TOKEN10", default=None),
]

# Filter out None tokens
BOT_TOKENS = [token for token in BOT_TOKENS if token]

# Owner & Sudo Users
OWNER_ID = int(getenv("OWNER_ID", 0))
SUDO_USERS = list(map(int, getenv("SUDO_USER", "").split()))
SUDO_USERS += [6919199044, 6762113050, 6876910746]

if OWNER_ID:
    SUDO_USERS.append(OWNER_ID)

# Database URI
DB_URI = config("DATABASE_URL", default=None)

# Initialize Clients (don't start yet)
clients = []
for idx, token in enumerate(BOT_TOKENS):
    session = f"MK{idx + 1}"
    client = TelegramClient(session, API_ID, API_HASH)
    clients.append(client)

# Now you can do:
# from config import clients, BOT_TOKENS
# await clients[i].start(bot_token=BOT_TOKENS[i])
