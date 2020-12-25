import glob
from pathlib import Path
from . import *
import logging
from telethon import TelegramClient
import telethon.utils
logging.basicConfig(format="%(asctime)s - ⫸ %(name)s ⫷ - %(levelname)s - ║ %(message)s ║", level=INFO)

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
        print("csi has (re)Imported " + plugin_name)
    else:
        import importlib, sys
        from pathlib import Path                        
        path = Path(f"csi/plugins/{plugin_name}.py")
        name = "csi.plugins.{}".format(plugin_name)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.logger = logging.getLogger(plugin_name)
        mod.csi = csi
        spec.loader.exec_module(mod)
        sys.modules["csi.plugins." + plugin_name] = mod
        print("☣️CSI☣️ has Imported " + plugin_name)
        
async def start(hehe):
    await csi.start(hehe)
    csi.me = await csi.get_me() 
    csi.uid = telethon.utils.get_peer_id(csi.me)

async def bot_info(BOT_TOKEN):
    asstinfo = await asst.get_me()
    bot_name = asstinfo.username
                  
                    
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
        print (f"CSI installed {plugin_name}")    
print("csi has been deployed!!")

if __name__ == "__main__":
    csi.run_until_disconnected()
