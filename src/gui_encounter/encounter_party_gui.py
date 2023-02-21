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

from gui_encounter import encounter_func as efunc

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

        character_list = self.connect_to_database()
        
        for character in character_list[0]:
            level = character_list[1].find_one({"character":character})["level"]

            self.character_button = Widget(
                widget_type=QPushButton(),
                stylesheet=style.PARTY_BUTTONS,
                parent_layout=self.party_scroll_layout.inner_layout(1),
                text = character,
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                height=cons.WSIZE*1.5,
                checkable=True,
                signal=self.add_party_member,
                class_group=self.widget_group,
                objectname = level
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
        name_list = self.collection.distinct("character")
        return (name_list,self.collection)

    def add_party_member(self):
        if self.sender().isChecked():
            self.party_members.append((self.sender().text(),self.sender().objectName()))
        else:
            self.party_members.remove((self.sender().text(),self.sender().objectName()))
        print(self.party_members)

    def confirm(self):
        efunc.clear_layout(self.encounter_gui.creature_layout.inner_layout(1))
        self.encounter_gui.player_list.clear()
        self.encounter_gui.player_encounter_list.clear()
        
        self.encounter_gui.creature_list.clear()
        self.encounter_gui.action_group.clear()

        self.encounter_gui.party_size_button.get_widget().setText(str(len(self.party_members)))
        
        avg_level = 0
        for player in self.party_members:
            self.encounter_gui.player_list.append((player[0],"Player",""))
            self.encounter_gui.add_player(player[0])
            avg_level += int(player[1])

        avg_level = avg_level / len(self.party_members)
        self.encounter_gui.world_level_button.get_widget().setText(str(round(avg_level)))
        self.hide()

