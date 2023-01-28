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
    print(widget)
    print(icon)