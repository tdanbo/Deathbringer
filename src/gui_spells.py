from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import stylesheet as style
import constants as cons

import json
import os

from character_sheet import CharacterSheet
from pyside import Section, Widget

class SpellsGUI(QWidget):
    def __init__(self, csheet, sender_widget):
        super().__init__(None, Qt.WindowStaysOnTopHint)

        self.csheet = csheet

        self.sender_widget = sender_widget
        self.spell_school = self.sender_widget.text().split(" ")[0]
        self.spell_level= self.sender_widget.text().split(" ")[1]

        spell_file = f"2_{self.spell_school.lower()}.json"
        spell_json = json.load(open(os.path.join(cons.ITEMS,spell_file), "r"))

        self.spell_main_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            spacing = 10,   
        )

        self.spell_scroll = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.spell_main_layout.inner_layout(1),
            scroll=(True,"top"),
        )

        for spell,spell_values in spell_json.items():
            if int(spell_values["level"]) <= int(self.spell_level):
                self.single_spell_layout = Section (
                outer_layout = QVBoxLayout(),
                inner_layout = ("HBox", 3),
                group = (True,None,125), 
                title=spell,
                #icon = (f"{self.spell_school}.png",cons.WSIZE*1.5,cons.ICON_COLOR),	  
                parent_layout = self.spell_scroll.inner_layout(1),
                )

                self.spell_label = Widget(
                    widget_type=QPlainTextEdit(),
                    stylesheet=style.BUTTONS,
                    parent_layout=self.single_spell_layout.inner_layout(2),
                    text = spell_values["description"],
                    size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                    )
                
                self.select_spell = Widget(
                    widget_type=QPushButton(),
                    stylesheet=style.BUTTONS,
                    parent_layout=self.single_spell_layout.inner_layout(3),
                    text = "Select",
                    size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                    height = cons.WSIZE*1.5,
                    objectname=spell,
                    )

                self.select_spell.get_widget().clicked.connect(self.confirm_spell)
                self.single_spell_layout.inner_layout(2).addWidget(self.spell_label.get_widget())
                self.single_spell_layout.inner_layout(3).addWidget(self.select_spell.get_widget())
                self.spell_scroll.inner_layout(1).addLayout(self.single_spell_layout.outer_layout())

        self.spell_main_layout.outer_layout().addLayout(self.spell_scroll.outer_layout())
        self.setWindowTitle("Select Spell")
        self.setLayout(self.spell_main_layout.outer_layout())

        self.setStyleSheet(style.BASE_STYLE)
        self.show()

    def confirm_spell(self):
        self.sender().objectName()
        self.sender_widget.setText(self.sender().objectName())
        self.sender_widget.clearFocus()
        self.hide()
        CharacterSheet(self.csheet).update_sheet()
