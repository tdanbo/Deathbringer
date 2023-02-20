from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

def set_creature_type(self, creature, creature_list):
    print(f"Creature: {creature}")
    for creature_item in creature_list:
        if creature_item != creature:
            self.findChild(QPushButton, creature_item).setChecked(False)

def clear_layout(layout):
    for item in range(layout.count()):
        layout.itemAt(item).widget().deleteLater()

def adjust_stat(self, objectname, adjust="add"):
    sender_widget = self.findChild(QWidget, objectname)
    current_value = int(sender_widget.text())
    if adjust == "add":
        current_value += 1
    else:
        current_value -= 1
        if current_value < 0:
            current_value = 0
    sender_widget.setText(str(current_value))
    
