from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import constants as cons

from character_sheet import CharacterSheet

def adjust_stat(self, stat, adjust="add"):
    current_level = int(self.character_level.get_widget().text())
    sender_widget = self.findChild(QPushButton, stat)
    current_value = int(sender_widget.text())
    if adjust == "add":
        current_value += 1
        if available_stats(self, current_level) > 0:
            if current_value > current_level:
                current_value = current_level
        else:
            return
    else:
        available_stats(self, current_level)
        current_value -= 1
        if current_value < 0:
            current_value = 0

    sender_widget.setText(str(current_value))

    stats = available_stats(self, current_level)

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

def available_stats(self, current_level):
    #Sum the total stats the character have.
    strength = self.findChild(QPushButton, "STR").text()
    dexterity = self.findChild(QPushButton, "DEX").text()
    constitution = self.findChild(QPushButton, "CON").text()
    intelligence = self.findChild(QPushButton, "INT").text()
    wisdom = self.findChild(QPushButton, "WIS").text()
    charisma = self.findChild(QPushButton, "CHA").text()

    available_stats = int(current_level) * cons.STATS_PER_LEVEL
    total_stats = int(strength) + int(dexterity) + int(constitution) + int(intelligence) + int(wisdom) + int(charisma)

    stats = available_stats - total_stats

    print(stats)
    print(total_stats)
    return stats