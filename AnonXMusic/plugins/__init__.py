import glob
from os.path import dirname, isfile
import importlib

def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*/*.py")

    all_modules = [
        (((f.replace(work_dir, "")).replace("/", "."))[:-3])
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return all_modules

# Load all modules
ALL_MODULES = sorted(__list_all_modules())

# Import the web server explicitly
try:
    web_server_module = importlib.import_module("AnonXMusic.plugins.web_server")
    __all__ = ALL_MODULES + ["ALL_MODULES", "web_server_module"]
except ModuleNotFoundError:
    print("web_server.py not found in the plugins directory.")

__all__ = ALL_MODULES + ["ALL_MODULES"]  # Keep the original __all__ for dynamic imports
