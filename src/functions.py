from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import os
import random

from combat_log import CombatLog
import constants as cons
import json
from character_sheet import CharacterSheet
import stylesheet as style

import re
import time
 

def single_roll(self,dictionary,character,roll_type,slot):
    item = self.findChild(QLineEdit, f"inventory{slot}").text()

    roll = self.findChild(QPushButton, f"{roll_type}{slot}").text()
    roll_type_label = self.findChild(QLabel, f"{roll_type}_label{slot}").text()
    rolle_type_label_check = roll_type_label.split(" ")[0]

    breakdown_dict = {
        "hit_dice":"",
        "hit_reroll_dice":"", 

        "roll_dice":"",
        "roll_reroll_dice":"",  

        "hit_results":"",
        "hit_reroll_results":"", 

        "roll_results":"",
        "roll_reroll_results":"", 
    }

    if roll_type_label == "":
        return

    if "Save" in roll_type_label:
        return

    elif rolle_type_label_check in ["Hit","Evoke"]:
        hit = roll.replace("+","")

        hit_reroll = random.randint(1, 20)
        hit_roll = random.randint(1, 20)

        roll_reroll_result = hit_reroll+int(hit)
        roll_result = hit_roll+int(hit)

        breakdown_dict["roll_dice"] = f"1d20+{hit}"
        breakdown_dict["roll_reroll_results"] = f"{hit_reroll}+{hit}" 
        breakdown_dict["roll_results"] = f"{hit_roll}+{hit}"

    elif rolle_type_label_check in ["Damage","Healing"]:
        rolls = []
        for r in range(2):
            result = [0, 0, 0]
            numbers = re.findall(r'\d+', roll)
            for i, number in enumerate(numbers):
                result[i % 3] += int(number)

            roll_multiplier = result[0]
            roll_die = result[1]
            roll_modifier = result[2]

            all_roll = []
            for i in range(roll_multiplier):
                all_roll.append(random.randint(1, roll_die))

            total_roll = sum(all_roll)+roll_modifier

            breakdown_roll_dice = f"{roll_multiplier}d{roll_die}+{roll_modifier}"
            breakdown_roll_result = "+".join(str(x) for x in all_roll)+"+"+str(roll_modifier)

            rolls.append((total_roll,breakdown_roll_dice,breakdown_roll_result))

        roll_result=rolls[0][0] 
        roll_reroll_result = rolls[1][0]

        breakdown_dict["roll_dice"] = rolls[0][1]
        breakdown_dict["roll_reroll_results"] = rolls[1][2]
        breakdown_dict["roll_results"] = rolls[0][2]  

    CombatLog(dictionary).set_entry(character, action_type=item, action_name=breakdown_dict["roll_dice"], hit_desc="", roll_desc=roll_type_label, reroll_hit="", reroll_roll=roll_reroll_result, hit="", roll=roll_result, breakdown=breakdown_dict)

def double_roll(self,dictionary,character,slot):
    item = self.findChild(QLineEdit, f"inventory{slot}").text()

    hit = self.findChild(QPushButton, f"hit_dc{slot}").text().replace("+","")
    roll = self.findChild(QPushButton, f"roll{slot}").text()

    hit_mod = self.findChild(QLabel, f"hit_dc_label{slot}").text()
    roll_mod = self.findChild(QLabel, f"roll_label{slot}").text()

    if roll_mod == "":
        return

    if hit != "":
        if "Save" in hit_mod:
            hit_reroll_result = ""
            hit_result = hit

            breakdown_hit_reroll_result = ""
            breakdown_hit_result = ""
        else:
            hit_reroll = random.randint(1, 20)
            hit_roll = random.randint(1, 20)

            hit_reroll_result = hit_reroll+int(hit)
            hit_result = hit_roll+int(hit)

            breakdown_hit_reroll_result = f"{hit_reroll_result}+{hit}" 
            breakdown_hit_result = f"{hit_result}+{hit}"
    else:
        breakdown_hit_reroll_result = ""
        breakdown_hit_result = ""

        hit_reroll_result = ""
        hit_result=""

    breakdown_hit_dice = f"1d20+{hit}"

    rolls = []
    for r in range(2):
        result = [0, 0, 0]
        numbers = re.findall(r'\d+', roll)
        for i, number in enumerate(numbers):
            result[i % 3] += int(number)

        roll_multiplier = result[0]
        roll_die = result[1]
        roll_modifier = result[2]

        all_roll = []
        for i in range(roll_multiplier):
            all_roll.append(random.randint(1, roll_die))

        print(all_roll)
        total_roll = sum(all_roll)+roll_modifier
        print(f"{roll_mod} Roll: {total_roll}")

        breakdown_roll_dice = f"{roll_multiplier}d{roll_die}+{roll_modifier}"
        breakdown_roll_result = "+".join(str(x) for x in all_roll)+"+"+str(roll_modifier)

        rolls.append((total_roll,breakdown_roll_dice,breakdown_roll_result))

    breakdown_roll_dice = rolls[0][1]
    breakdown_roll_reroll_dice = rolls[1][1]

    breakdown_roll_result = rolls[0][2]
    breakdown_roll_reroll_result = rolls[1][2]

    roll_result=rolls[0][0] 
    roll_reroll_result = rolls[1][0]

 
    breakdown_dict = {
        "hit_dice":breakdown_hit_dice,
        "hit_reroll_dice":breakdown_hit_dice, 

        "roll_dice":breakdown_roll_dice,
        "roll_reroll_dice":breakdown_roll_reroll_dice,  

        "hit_results":breakdown_hit_result,
        "hit_reroll_results":breakdown_hit_reroll_result, 

        "roll_results":breakdown_roll_result,
        "roll_reroll_results":breakdown_roll_reroll_result, 
    }

    CombatLog(dictionary).set_entry(character, action_type=item, action_name=breakdown_dict["roll_dice"], hit_desc=hit_mod, roll_desc=roll_mod, reroll_hit=hit_reroll_result, reroll_roll=roll_reroll_result, hit=hit_result, roll=roll_result, breakdown=breakdown_dict)

def create_folder(dir_path):
    isExist = os.path.exists(dir_path)
    if not isExist:
        os.makedirs(dir_path)

def read_json(file_path):
    file_json = json.load(open(file_path, "r"))
    return file_json

def set_icon(widget, icon, color):
    qicon = QIcon()
    if icon in [".png",""]:
        pixmap = QPixmap()
    else:
        pixmap = QPixmap(os.path.join(cons.ICONS, icon))
        if color != "":
            paint = QPainter(pixmap)
            if paint.isActive():
                paint.setCompositionMode(QPainter.CompositionMode_SourceIn)
                paint.fillRect(pixmap.rect(), QColor(color))
                paint.end()
    qicon.addPixmap(pixmap)
    try:
        widget.setIcon(qicon)
    except:
        widget.setPixmap(pixmap)
        widget.setScaledContents(True)