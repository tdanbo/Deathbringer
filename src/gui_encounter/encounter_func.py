from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

def set_creature_type(self, creature, creature_list):
    print(f"Creature: {creature}")
    for creature_item in creature_list:
        if creature_item != creature:
            self.findChild(QPushButton, creature_item).setChecked(False)