from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import stylesheet as style
import constants as cons

import json
import functions as func
import os

from character_sheet import CharacterSheet
from pyside import Section, Widget

class NewCharacter(QWidget):
    def __init__(self,csheet):
        super().__init__(None, Qt.WindowStaysOnTopHint)

        self.csheet = csheet

        self.new_main_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
        )

        self.new_widget_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 2),
            parent_layout = self.new_main_layout.inner_layout(1),
            title="New Character",
            icon = ("plus.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            group=(True,None,None),
        )

        self.integer_line = Widget(
            widget_type=QLineEdit(),
            stylesheet=style.QADDSUB,
            text="",
            align="center",
            objectname = "name",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            height=cons.WSIZE*1.50,
        )

        self.cancel_widget = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BUTTONS,
            text="Cancel",
            objectname = "cancel",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.accept_widget = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BUTTONS,
            text="Accept",
            objectname = "accept",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.cancel_widget.get_widget().clicked.connect(self.create_character)
        self.accept_widget.get_widget().clicked.connect(self.create_character)



        self.new_widget_layout.inner_layout(1).addWidget(self.integer_line.get_widget())
        self.new_widget_layout.inner_layout(2).addWidget(self.accept_widget.get_widget())
        self.new_widget_layout.inner_layout(2).addWidget(self.cancel_widget.get_widget())

        self.new_main_layout.outer_layout().addLayout(self.new_widget_layout.outer_layout())

        self.setWindowTitle("New Character")
        self.setLayout(self.new_main_layout.outer_layout())
        self.setStyleSheet(style.BASE_STYLE)
        self.setFixedHeight(125)
        self.setMinimumWidth(250)

    def create_character(self):
        cname = self.integer_line.get_widget().text()
        for i in range(self.csheet.character_name.get_widget().count()):
            if self.csheet.character_name.get_widget().itemText(i).lower() == cname.lower():
                self.integer_line.get_widget().setText("Character already exists")
                return

        state = self.sender().objectName()
        if state == "accept":
            
            #Setting default values
            self.csheet.character_level.get_widget().setText("1")
            self.csheet.findChild(QPushButton,"STR").setText("0")
            self.csheet.findChild(QPushButton,"DEX").setText("0")
            self.csheet.findChild(QPushButton,"CON").setText("0")
            self.csheet.findChild(QPushButton,"INT").setText("0")
            self.csheet.findChild(QPushButton,"WIS").setText("0")
            self.csheet.findChild(QPushButton,"CHA").setText("0")

            self.csheet.findChild(QPushButton, "current_hp").setText(str(cons.HIT_DICE))

            self.csheet.findChild(QPushButton, "current_hp").setText(str(cons.HIT_DICE))
            self.csheet.findChild(QPushButton, "current_morale").setText(str(cons.BASE_MORALE))

            self.csheet.stat_layout.get_title()[1].setText("3 remaining stat points.")

            for slot in range(1, cons.MAX_SLOTS):
                self.csheet.findChild(QLineEdit, "inventory" + str(slot)).setText("")

            for focus in range(1, 11):
                self.csheet.findChild(QToolButton, "focusdice" + str(focus)).setChecked(False)

            for spell in range(1, 11):
                self.csheet.findChild(QToolButton, "spellslot" + str(spell)).setChecked(False)

            for feat in range(1,4):
                self.csheet.findChild(QToolButton, "feat" + str(feat)).setChecked(False)

            print("Needs to check if char exists")

            self.csheet.character_name.get_widget().addItem(cname)
            self.csheet.character_name.get_widget().setCurrentText(cname)

            CharacterSheet(self.csheet).update_sheet()

            self.hide()
        else:
            self.hide()