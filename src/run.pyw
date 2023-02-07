import sys

sys.dont_write_bytecode = True  # Will supress __pycache__ creation

import os
from importlib import *

ROOT = os.path.abspath(os.path.dirname(__file__))
PACKAGES = os.path.join(os.path.abspath(os.path.dirname(__file__)), ".packages")
[sys.path.append(p) for p in [ROOT, PACKAGES] if p not in sys.path]

# CUSTOM MODULES
import gui_main
import constants as cons
import stylesheet as style
import functions as func

[reload(module) for module in [gui_main, func, cons, style]]

def run():
    gui_main.run_gui(cons.SCRIPT_NAME, cons.VERSION)

if __name__ == "__main__":
    run()
