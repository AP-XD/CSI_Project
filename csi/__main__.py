import glob
from pathlib import Path
from . import *
import logging
from telethon import TelegramClient
import telethon.utils
from csi.utils import load_plugins

async def start(hehe):
    await csi.start(hehe)
    csi.me = await csi.get_me() 
    csi.uid = telethon.utils.get_peer_id(csi.me)

async def bot_info(BOT_TOKEN):
    asstinfo = await asst.get_me()
    bot_name = asstinfo.username

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
                    
                    
csi.asst = None
print("Initialising...")
if BOT_TOKEN is not None:
    print("Setting up CSI...")
    csi.asst = TelegramClient("BOT_TOKEN",api_id=Var.API_ID,api_hash=Var.API_HASH).start(bot_token=Var.BOT_TOKEN)
    print ("CSI loaded.")
    print("Starting csi UserBot!")
    csi.loop.run_until_complete(start(Var.BOT_TOKEN))
    print("Done, startup completed")
else:
    print("Starting User Mode...")
    csi.start()

path = "csi/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
    
print("csi has been deployed!!")

if __name__ == "__main__":
    csi.run_until_disconnected()
