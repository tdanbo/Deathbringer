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

def adjust_stat_widget(self, stat, state):
    sender_widget = self.findChild(QPushButton, stat)
    max_morale = self.findChild(QPushButton, "max_morale")
    current_value = int(sender_widget.text())
    if state == "add":
        current_value += 1
        if stat == "current_morale":
            if current_value > int(max_morale.text()):
                current_value = int(max_morale.text())
    else:
        current_value -= 1
        if stat != "current_morale":
            if current_value < 0:
                current_value = 0

    if current_value >= 0:
        sender_widget.setStyleSheet(style.QPUSHBUTTON)
    else:
        sender_widget.setStyleSheet(style.QPUSHBUTTON_INJURY)

    sender_widget.setText(str(current_value))
    CharacterSheet(self).update_dictionary()        

def roll_dice(dictionary, character, die, roll_type, roll_breakdown, modifier=0):
    print(f"Rolling a {die} sided dice")
    result = random.randint(1, die)
    roll = result + modifier
    CombatLog(dictionary).set_entry(character, roll, roll_type, roll_breakdown)

def inventory_roll(self,dictionary,character,slot):
    print(f"Rolling for {character} {slot}")
    print("--------------------")
    item = self.findChild(QLineEdit, f"inventory{slot}").text()
    item_label = self.findChild(QPushButton, f"inventory_label{slot}").text()

    evoke = self.findChild(QPushButton, f"evoke{slot}").text().replace("+","")
    hit = self.findChild(QPushButton, f"hit_dc{slot}").text().replace("+","")
    roll = self.findChild(QPushButton, f"roll{slot}").text()

    evoke_mod = self.findChild(QPushButton, f"evoke_label{slot}").text().replace("Evoke ","")
    hit_mod = self.findChild(QPushButton, f"hit_dc_label{slot}").text()
    roll_mod = self.findChild(QPushButton, f"roll_label{slot}").text()

    if evoke != "":
        evoke_roll = random.randint(1, 20)+int(evoke)
        evoke_dc = int(evoke_mod)
        if evoke_roll >= evoke_dc:
            double_roll(dictionary,character,item,item_label,hit,hit_mod,roll,roll_mod)
        else:
            print(f"Evoke Failed: {evoke_roll}")
            CombatLog(dictionary).set_entry(character, action_type=item, action_name="Spell Cast", hit_desc="", roll_desc="Evoke", hit="", roll=evoke_roll, breakdown="")
    else:
        double_roll(dictionary,character,item,item_label,hit,hit_mod,roll,roll_mod)

def double_roll(dictionary,character,item,item_label,hit,hit_mod,roll,roll_mod):
    if item_label == "Weapon":
        action_type = "Attack"
    else:
        action_type = "Spell Cast"

    if hit != "":
        if "Save" in hit_mod:
            total_hit = hit
            print(f"{hit_mod}: {total_hit}")
        else:
            hit_roll = random.randint(1, 20)+int(hit)
            total_hit = hit_roll
            print(f"Hit Roll: {total_hit}")
    else:
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

        roll_breakdown = " + ".join(str(x) for x in all_roll)+" + "+str(roll_modifier)

        print(all_roll)
        total_roll = sum(all_roll)+roll_modifier
        print(f"{roll_mod} Roll: {total_roll}")

    CombatLog(dictionary).set_entry(character, action_type=item, action_name=action_type, hit_desc=hit_mod, roll_desc=roll_mod, hit=total_hit, roll=total_roll, breakdown=roll_breakdown)

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