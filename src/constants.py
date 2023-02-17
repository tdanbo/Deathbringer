
import functions as func
import os
import sys
import json

ROOT = os.path.abspath(os.path.dirname(__file__))
try:
    ROOT = sys._MEIPASS
except:
    ROOT = os.path.dirname(__file__)

SCRIPT_NAME = "Vanguard 5e"
LOCAL_DIRECTORY = os.path.join(os.getenv("APPDATA"), SCRIPT_NAME)
VERSION = "1.0"
USER = "test-user"
PASSWORD = "7kHYdt9kna9d9w3t" 
CONNECT = f"mongodb+srv://{USER}:{PASSWORD}@cluster0.2oqhlud.mongodb.net/?retryWrites=true&w=majority"
SETTINGS = os.path.join(LOCAL_DIRECTORY, "settings.json")
ICONS = os.path.join(ROOT, ".icons")
FEATURES = os.path.join(ROOT, ".feats")

ITEMS = os.path.join(ROOT, ".items")

WSIZE = 22
ICON_COLOR = "#CCCCCC"

CHARACTER = "Beasttoe"
START_SLOTS = 6
MAX_SLOTS = 16
BASE_AC = 9
HIT_DICE = 6
BASE_MORALE = 3
BASE_SAVE = 11
STATS_PER_LEVEL = 3

ELEMENTS = json.load(open(os.path.join(ROOT, ".creatures", "elements.json"), "r"))

abjuration = ["abjuration 1","abjuration 2","abjuration 3","abjuration 4","abjuration 5"]
conjuration = ["conjuration 1","conjuration 2","conjuration 3","conjuration 4","conjuration 5"]
divination = ["divination 1","divination 2","divination 3","divination 4","divination 5"]
enchantment = ["enchantment 1","enchantment 2","enchantment 3","enchantment 4","enchantment 5"]
evocation = ["evocation 1","evocation 2","evocation 3","evocation 4","evocation 5"]
illusion = ["illusion 1","illusion 2","illusion 3","illusion 4","illusion 5"]
necromancy = ["necromancy 1","necromancy 2","necromancy 3","necromancy 4","necromancy 5"]
transmutation = ["transmutation 1", "transmutation 2", "transmutation 3", "transmutation 4", "transmutation 5"]

SPELL_LISTS = abjuration+conjuration+divination+enchantment+evocation+illusion+necromancy+transmutation        

COLOR_LABEL = {
    "abjuration": "#1f293d",
    "conjuration": "#1f293d",
    "divination": "#1f293d",
    "enchantment": "#1f293d",
    "evocation": "#1f293d",
    "illusion": "#1f293d",
    "necromancy": "#1f293d",
    "transmutation": "#1f293d",
    "weapon": "#3d1f1f",
    "armor": "#1f3d34",
    "potion": "#391f3d",
    "rest": "#3d2e1f",
    "gold": "#3d1f34",
    "misc": "#1a1a1a",
    "injury": "#1f293d",
}

func.create_folder(LOCAL_DIRECTORY)
