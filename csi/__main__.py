import glob
from pathlib import Path
from . import *
import logging
from telethon import TelegramClient
import telethon.utils
logging.basicConfig(format="%(asctime)s - ⫸ %(name)s ⫷ - %(levelname)s - ║ %(message)s ║", level=INFO)
logger = logging.getLogger()
def load_plugins(plugin_name):
    if plugin_name.startswith("__"):
        pass
    elif plugin_name.endswith("_"):
        import importlib
        from pathlib import Path
        path = Path(f"csi/plugins/{plugin_name}.py")
        name = "csi.plugins.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        logger.info("csi has (re)Imported " + plugin_name)
    else:
        import importlib, sys
        from pathlib import Path                        
        path = Path(f"csi/plugins/{plugin_name}.py")
        name = "csi.plugins.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.csi = csi
        spec.loader.exec_module(mod)
        sys.modules["csi.plugins." + plugin_name] = mod
        logger.info("☣️CSI☣️ has Imported " + plugin_name)
        
async def start(hehe):
    await csi.start(hehe)
    csi.me = await csi.get_me() 
    csi.uid = telethon.utils.get_peer_id(csi.me)

async def bot_info(BOT_TOKEN):
    asstinfo = await asst.get_me()
    bot_name = asstinfo.username
                  
                    
csi.asst = None
logger.info("Initialising...")
if BOT_TOKEN is not None:
    logger.info("Setting up CSI...")
    csi.asst = TelegramClient("BOT_TOKEN",api_id=Var.API_ID,api_hash=Var.API_HASH).start(bot_token=Var.BOT_TOKEN)
    logger.info("CSI loaded.")
    logger.info("Starting csi UserBot!")
    csi.loop.run_until_complete(start(Var.BOT_TOKEN))
    logger.info("Done, startup completed")
else:
    logger.info("Starting User Mode...")
    csi.start()

path = "csi/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))
        print (f"CSI installed {plugin_name}")    
logger.info("csi has been deployed!!")

if __name__ == "__main__":
    csi.run_until_disconnected()
