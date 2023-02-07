from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import constants as cons

from character_sheet import CharacterSheet

def adjust_xp(self, adjust="add", increment=1):
    level_w = self.character_level.get_widget()
    current_level = float(level_w.text())

    if adjust == "add":
        current_level += increment
    else:
        current_level -= increment
        if current_level < 0:
            current_level = 0

    current_level = round(current_level, 1)

    if current_level.is_integer():
        level_w.setText(str(int(current_level)))
    else:
        level_w.setText(str(float(current_level)))

    stats = total_stats(self, current_level)

    label = self.stat_layout.get_title()[1]

    if stats == 0:
        stat_message = ""
        label.setText(stat_message)
    elif stats < 0:
        stat_message = f"Remove {stats} stat points."
        label.setText(stat_message)
    elif stats > 0:
        stat_message = f"{stats} remaining stat points."
        label.setText(stat_message)

    CharacterSheet(self).update_sheet()


def total_stats(self, current_level):
    #Sum the total stats the character have.
    strength = self.findChild(QPushButton, "STR").text()
    dexterity = self.findChild(QPushButton, "DEX").text()
    constitution = self.findChild(QPushButton, "CON").text()
    intelligence = self.findChild(QPushButton, "INT").text()
    wisdom = self.findChild(QPushButton, "WIS").text()
    charisma = self.findChild(QPushButton, "CHA").text()

    available_stats = int(current_level) * cons.STATS_PER_LEVEL
    total_stats = int(strength) + int(dexterity) + int(constitution) + int(intelligence) + int(wisdom) + int(charisma)

    missing_stats = available_stats - total_stats

    return missing_stats