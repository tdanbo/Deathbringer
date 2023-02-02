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



class AddSubGUI(QWidget):
    def __init__(self, csheet, sender_widget):
        super().__init__(None, Qt.WindowStaysOnTopHint)

        self.csheet = csheet

        self.addsub_main_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
        )

        self.addsub_widget_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 2),
            parent_layout = self.addsub_main_layout.inner_layout(1),
            title="Adjust HP",
            icon = ("hp.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            group=(True,None,None),
        )

        self.integer_line = Widget(
            widget_type=QLineEdit(),
            stylesheet=style.QADDSUB,
            text="",
            align="center",
            objectname = "adjuster",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            height=cons.WSIZE*1.50,
        )

        self.minus_widget = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BUTTONS,
            text="-",
            objectname = "minus",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.plus_widget = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BUTTONS,
            text="+",
            objectname = "plus",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.minus_widget.get_widget().clicked.connect(self.send_value)
        self.plus_widget.get_widget().clicked.connect(self.send_value)



        self.addsub_widget_layout.inner_layout(1).addWidget(self.integer_line.get_widget())
        self.addsub_widget_layout.inner_layout(2).addWidget(self.minus_widget.get_widget())
        self.addsub_widget_layout.inner_layout(2).addWidget(self.plus_widget.get_widget())

        self.addsub_main_layout.outer_layout().addLayout(self.addsub_widget_layout.outer_layout())

        self.setWindowTitle("Set Value")
        self.setLayout(self.addsub_main_layout.outer_layout())
        self.setStyleSheet(style.BASE_STYLE)
        self.setFixedHeight(125)

    def send_value(self):
        state = self.sender().objectName()
        CharacterSheet(self.csheet).adjust_hp(state, self.integer_line.get_widget().text())