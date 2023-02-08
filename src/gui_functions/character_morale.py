from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import stylesheet as style

from character_sheet import CharacterSheet

def adjust_morale(self, adjust = "add"):
    current_morale = self.findChild(QPushButton, "current_morale")
    max_morale = self.findChild(QPushButton, "max_morale")
    current_value = int(current_morale.text())
    if adjust == "add":
        current_value += 1
        if current_value > int(max_morale.text()):
            current_value = int(max_morale.text())
    else:
        current_value -= 1

    if current_value >= 0:
        current_morale.setStyleSheet(style.BIG_BUTTONS)
    else:
        current_morale.setStyleSheet(style.BUTTONS_INJURY)

    current_morale.setText(str(current_value))
    
    CharacterSheet(self).update_sheet()   