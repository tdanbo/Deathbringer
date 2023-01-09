from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from my_pyside import Section
from my_pyside import Widget

class CharacterSheetGUI:
    def __init__(self):
        self.character_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = (QVBoxLayout(), 1),     
        )

        self.stat_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = (QHBoxLayout(), 6),
            parent_layout = self.character_layout.inner_layout(0)
        )

        for number,stat in enumerate(["STR", "DEX", "CON", "INT", "WIS", "CHA"]):
            self.stat_label = Widget(
                widget_type=QLabel(),
                text=stat,
                parent_layout = self.stat_layout.inner_layout(number)
            )

    def get_main_layout(self):
        return self.character_layout.outer_layout()