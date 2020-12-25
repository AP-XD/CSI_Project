import sys
import logging
import importlib
from pathlib import Path

def load_plugins(plugin_name):
    from csi import csi
    path = Path(f"csi/plugins/{plugin_name}.py")
    name = "csi.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["csi.plugins." + plugin_name] = load
    print("csi has Imported " + plugin_name)
    mod.csi = csi
