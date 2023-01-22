
import functions as func
import os
import sys

ROOT = os.path.abspath(os.path.dirname(__file__))
try:
    ROOT = sys._MEIPASS
except:
    ROOT = os.path.dirname(__file__)

SCRIPT_NAME = "Deathbringer App"
LOCAL_DIRECTORY = os.path.join(os.getenv("APPDATA"), SCRIPT_NAME)
VERSION = "0.0.1"
USER = "test-user"
PASSWORD = "7kHYdt9kna9d9w3t" 
CONNECT = f"mongodb+srv://{USER}:{PASSWORD}@cluster0.2oqhlud.mongodb.net/?retryWrites=true&w=majority"
SETTINGS = os.path.join(LOCAL_DIRECTORY, "settings.json")
ICONS = os.path.join(ROOT, ".icons")

ITEMS = os.path.join(ROOT, ".items")

WSIZE = 22
ICON_COLOR = "#CCCCCC"

MAX_SLOTS = 16
BASE_AC = 9
HIT_DICE = 6

func.create_folder(LOCAL_DIRECTORY)
