from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import stylesheet as style
import constants as cons

import json
import functions as func
import os

import pymongo

from pyside import Section, Widget
from character_sheet import CharacterSheet

class PartySelectGUI(QWidget):
    def __init__(self,encounter_gui):
        super().__init__(None, Qt.WindowStaysOnTopHint)

        self.encounter_gui = encounter_gui
        self.party_members = []

        self.section_group = []
        self.widget_group = []

        self.master_layout = QVBoxLayout()

        self.party_scroll_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.master_layout,
            scroll=(True,"top"),
            group=(True,None,None),
            title="Select Party Members",
            spacing = 5,
            icon=("party.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            class_group = self.section_group
        )

        for character in self.connect_to_database():

            self.character_button = Widget(
                widget_type=QPushButton(),
                stylesheet=style.PARTY_BUTTONS,
                parent_layout=self.party_scroll_layout.inner_layout(1),
                text = character,
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                height=cons.WSIZE*1.5,
                checkable=True,
                signal=self.add_party_member,
                class_group=self.widget_group
            )

        self.party_confirm = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BUTTONS,
            parent_layout=self.master_layout,
            text="Confirm",
            objectname = "confirm",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            height=cons.WSIZE*1.75,
            signal=self.confirm,
            class_group=self.widget_group
        )

        print(self.section_group)
        print(self.widget_group)

        for section in self.section_group:
            section.connect_to_parent()

        for widget in self.widget_group:
            widget.connect_to_parent()
            widget.set_signal()

        self.setStyleSheet(style.BASE_STYLE)
        self.setLayout(self.master_layout)

    def connect_to_database(self):
        self.client = pymongo.MongoClient(cons.CONNECT)
        self.db = self.client ["dnd"]
        self.collection = self.db["characters"]
        character_list = self.collection.distinct("character")
        return character_list

    def add_party_member(self):
        if self.sender().isChecked():
            self.party_members.append(self.sender().text())
        else:
            self.party_members.remove(self.sender().text())
        print(self.party_members)

    def confirm(self):
        self.encounter_gui.party_size_button.get_widget().setText(str(len(self.party_members)))
        self.encounter_gui.party_size_button.get_widget().setToolTip("\n".join(self.party_members))
        self.encounter_gui.party_icon.get_widget().setToolTip("\n".join(self.party_members))
        
        for member in self.party_members:
            self.encounter_gui.encounter_list.append((member,"Player","Slashing"))
            creature_count = len(self.encounter_gui.encounter_list)-1
            self.encounter_gui.add_gui_creatures(member,creature_count)
            
        self.hide()

