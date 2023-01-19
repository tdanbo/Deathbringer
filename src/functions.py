from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import os
import random

from combat_log import CombatLog
import constants as cons
import json

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
    pixmap = QPixmap(os.path.join(cons.ICONS, icon))
    if color != "":
        paint = QPainter()
        paint.begin(pixmap)
        paint.setCompositionMode(QPainter.CompositionMode_SourceIn)
        paint.fillRect(pixmap.rect(), QColor(color))
        paint.end()
    qicon.addPixmap(pixmap)
    try:
        widget.setIcon(qicon)
    except:
        widget.setPixmap(pixmap)
        widget.setScaledContents(True)
