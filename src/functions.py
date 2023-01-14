import os
import random

from combat_log import CombatLog
from gui_sheet import CharacterSheetGUI

def roll_dice(dictionary, character, die, roll_type, roll_breakdown, modifier=0):
    print(f"Rolling a {die} sided dice")
    result = random.randint(1, die)
    roll = result + modifier
    CombatLog(dictionary).set_entry(character, roll, roll_type, roll_breakdown)

def create_folder(dir_path):
    isExist = os.path.exists(dir_path)
    if not isExist:
        os.makedirs(dir_path)