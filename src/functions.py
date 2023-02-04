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
 

def inventory_roll(self,dictionary,character,slot):
    print(f"Rolling for {character} {slot}")
    print("--------------------")
    item = self.findChild(QLineEdit, f"inventory{slot}").text()
    item_label = self.findChild(QPushButton, f"inventory_label{slot}").text()

    evoke = self.findChild(QPushButton, f"evoke{slot}").text().replace("+","")
    hit = self.findChild(QPushButton, f"hit_dc{slot}").text().replace("+","")
    roll = self.findChild(QPushButton, f"roll{slot}").text()

    evoke_mod = self.findChild(QPushButton, f"evoke_label{slot}").text()
    hit_mod = self.findChild(QPushButton, f"hit_dc_label{slot}").text()
    roll_mod = self.findChild(QPushButton, f"roll_label{slot}").text()

    if evoke != "":

        evoke_roll = random.randint(1, 20)
        evoke_result = evoke_roll+int(evoke)
        evoke_dc = int(evoke_mod.replace("Evoke ",""))

        breakdown_roll_dice = f"d20 + {evoke}" 
        breakdown_roll_result = f"{evoke_roll}+{evoke}"


        if evoke_result >= evoke_dc:
            double_roll(dictionary,character,item,item_label,hit,hit_mod,roll,roll_mod)
        else:
            print(f"Evoke Failed: {evoke_result}")
            breakdown_dict = {"hit_dice":"","hit_results":"", "roll_dice":breakdown_roll_dice, "roll_results": breakdown_roll_result,}
            CombatLog(dictionary).set_entry(character, action_type=item, action_name=breakdown_dict["roll_dice"], hit_desc="", roll_desc=evoke_mod, hit="", roll=evoke_result, breakdown=breakdown_dict)
    else:
        double_roll(dictionary,character,item,item_label,hit,hit_mod,roll,roll_mod)

def double_roll(dictionary,character,item,item_label,hit,hit_mod,roll,roll_mod):
    if hit != "":
        if "Save" in hit_mod:
            total_hit = hit
            hit_result_breakdown = ""
            print(f"{hit_mod}: {total_hit}")
        else:
            hit_roll = random.randint(1, 20)
            total_hit = hit_roll+int(hit)
            hit_result_breakdown = f"{hit_roll}+{hit}"
            print(f"Hit Roll: {total_hit}")
    else:
        hit_result_breakdown = ""
        total_hit=""

    if roll != "":
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

    breakdown_hit_dice = f"1d20+{hit}"
    breakdown_hit_result = hit_result_breakdown
    breakdown_roll_dice = f"{roll_multiplier}d{roll_die}+{roll_modifier}"
    breakdown_roll_result = "+".join(str(x) for x in all_roll)+"+"+str(roll_modifier)
 
    breakdown_dict = {"hit_dice":breakdown_hit_dice,"hit_results":breakdown_hit_result, "roll_dice":breakdown_roll_dice, "roll_results": breakdown_roll_result,}
    CombatLog(dictionary).set_entry(character, action_type=item, action_name=breakdown_dict["roll_dice"], hit_desc=hit_mod, roll_desc=roll_mod, hit=total_hit, roll=total_roll, breakdown=breakdown_dict)

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