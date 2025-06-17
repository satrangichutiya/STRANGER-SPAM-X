import glob
import asyncio
import logging
from pathlib import Path
from config import clients, BOT_TOKENS
from utils import load_plugins

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
)

# ⚡ Plugin Loader
def load_all_plugins():
    for file in glob.glob("AltronX/modules/*.py"):
        plugin_name = Path(file).stem
        load_plugins(plugin_name)
    print("\n⚡️𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑⚡️𝐒𝐏𝐀𝐌 𝐁𝐎𝐓𝐒 𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 😎🤘🏻\nᴍʏ ᴍᴀsᴛᴇʀ ---> @SHIVANSHDEVS")

# ✅ Async Safe Start
async def start_all_bots():
    for i, client in enumerate(clients):
        try:
            await client.start(bot_token=BOT_TOKENS[i])
            print(f"[INFO] MK{i+1} Started Successfully.")
        except Exception as e:
            print(f"[ERROR] MK{i+1} Failed: {e}")

# ✅ Keep All Running
async def run_forever():
    await asyncio.gather(*(client.run_until_disconnected() for client in clients))

# 🚀 Launch
async def main():
    await start_all_bots()
    load_all_plugins()
    await run_forever()

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
