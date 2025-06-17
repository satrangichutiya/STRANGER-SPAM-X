import asyncio
import glob
from pathlib import Path
from config import clients, BOT_TOKENS
from utils import load_plugins
import logging

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# Plugin loader
def load_all_plugins():
    path = "AltronX/modules/*.py"
    files = glob.glob(path)
    for name in files:
        patt = Path(name)
        plugin_name = patt.stem
        load_plugins(plugin_name)

print("⚡️ 𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑 ⚡️ 𝐁𝐎𝐓𝐒 𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 ✅")

load_all_plugins()

# Limit bots to 3
LIMIT = 3

async def main():
    for i, client in enumerate(clients[:LIMIT]):
        try:
            await client.start(bot_token=BOT_TOKENS[i])
            print(f"[INFO] MK{i+1} Started ✅")
        except Exception as e:
            print(f"[ERROR] MK{i+1} Failed ❌: {e}")
    
    await asyncio.gather(*[client.run_until_disconnected() for client in clients[:LIMIT]])

asyncio.run(main())
