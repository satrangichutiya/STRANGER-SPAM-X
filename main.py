import glob
from pathlib import Path
from utils import load_plugins
import logging
import asyncio
from config import MK1, MK2, MK3  # Only 3 bots now

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


def load_all_plugins():
    path = "AltronX/modules/*.py"
    files = glob.glob(path)
    for name in files:
        with open(name) as a:
            patt = Path(a.name)
            plugin_name = patt.stem
            load_plugins(plugin_name.replace(".py", ""))

    print("\n⚡️𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑⚡️𝐒𝐏𝐀𝐌 𝐁𝐎𝐓𝐒 𝐃𝐄𝐏𝐋𝐎𝐘𝐄𝐃 𝐒𝐔𝐂𝐂𝐄𝐒𝐒𝐅𝐔𝐋𝐋𝐘 😎🤘🏻\nᴍʏ ᴍᴀsᴛᴇʀ ---> @SHIVANSHDEVS")


async def main():
    load_all_plugins()

    await MK1.run_until_disconnected()
    await MK2.run_until_disconnected()
    await MK3.run_until_disconnected()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
