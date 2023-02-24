from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

# import functools
from pyside import Section
from pyside import Widget
from pyside import SimpleSection

import constants as cons
import functions as func
import stylesheet as style
import functools
import math
import random

from gui_functions import custom_rolls
from gui_functions import custom_log
from gui_functions import roll

from gui_functions import character_stats

from gui_encounter.encounter import Encounter
from gui_encounter.encounter_party_gui import PartySelectGUI

from gui_encounter import encounter_func as efunc
from gui_encounter import encounter_database as ebase

from gui_encounter.creature_base import CreatureBase
from gui_encounter.creature_actions import CreatureAction

class EncounterGUI(QWidget):
    def __init__(self):
        super().__init__()

        #This list it to keep track of the creatures that are in the encounter
        self.master_layout = QVBoxLayout()
        self.player_list = []
        self.creature_list = []

        self.encounter_list = []
        self.player_encounter_list = []

        self.action_group = []
        self.section_group = []
        self.widget_group = []

        #Setting up layouts/sections
        self.encounter_main_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            spacing = 10,
            class_group = self.section_group 

        )

        self.settings_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.master_layout,
            icon = ("encounter.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            group=False,
            class_group=self.section_group,
            height=120,
            spacing=5
        )

        self.pc_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 2),
            parent_layout = self.settings_layout.inner_layout(1),
            title="Party",
            icon = ("party.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            group=True,
            class_group=self.section_group,
            width=cons.WSIZE*3
        )

        self.adventure_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 2),
            parent_layout = self.settings_layout.inner_layout(1),
            title="Encounter Level",
            icon = ("adventure.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            group=True,
            class_group=self.section_group,
            width=cons.WSIZE*6
        )

        self.creature_type_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 2),
            parent_layout = self.settings_layout.inner_layout(1),
            title="Creature Setup",
            icon = ("creature_setup.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            group=True,
            class_group=self.section_group
        )

        self.creature_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.master_layout,
            title="Encounter",
            icon = ("encounter.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            scroll=(True,"top"),
            group=True,
            spacing=10,
            class_group=self.section_group
        )

        title_layout = self.creature_layout.get_title()[2]

        self.reset_encounter_button = Widget(
            widget_type=QPushButton(),
            text="Clear Encounter",
            objectname = "reset_encounter",
            parent_layout=title_layout,
            signal=self.clear_encounter,
            class_group=self.widget_group,
        )        

        self.party_size_button = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            text="0",
            objectname = "pc_size",
            parent_layout=self.pc_layout.inner_layout(1),
            signal=self.open_partyselect,
            class_group=self.widget_group,
            size_policy=(QSizePolicy.Expanding, QSizePolicy.Expanding)
        )

        self.party_icon = Widget(
            widget_type=QToolButton(),
            stylesheet=style.BUTTONS,
            objectname = "pc_icon",
            parent_layout=self.pc_layout.inner_layout(1),
            icon = ("party.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            signal=self.open_partyselect,
            class_group=self.widget_group,
            size_policy=(QSizePolicy.Expanding, QSizePolicy.Expanding),
            height=cons.WSIZE*1.5,
        )
        
        self.adventure_level_button = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            text="0",
            objectname = "adventure_level",
            parent_layout=self.adventure_layout.inner_layout(1),
            class_group=self.widget_group,
            size_policy=(QSizePolicy.Expanding, QSizePolicy.Expanding),
            signal=lambda: efunc.adjust_stat(self, "adventure_level", "add")
        )

        self.adventure_select_button = Widget(
            widget_type=QToolButton(),
            stylesheet=style.BUTTONS,
            objectname = "adventure",
            parent_layout=self.adventure_layout.inner_layout(1),
            signal=self.run_encounter,
            icon=("adventure.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            size_policy=(QSizePolicy.Expanding, QSizePolicy.Expanding),
            height=cons.WSIZE*1.5,
            class_group=self.widget_group
            
        )

        self.world_level_button = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            text="0",
            objectname = "world_level",
            parent_layout=self.adventure_layout.inner_layout(2),
            class_group=self.widget_group,
            size_policy=(QSizePolicy.Expanding, QSizePolicy.Expanding),
        )

        self.world_select_button = Widget(
            widget_type=QToolButton(),
            stylesheet=style.BUTTONS,
            objectname = "world",
            parent_layout=self.adventure_layout.inner_layout(2),
            signal=self.run_encounter,
            icon=("world.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            class_group=self.widget_group,
            size_policy=(QSizePolicy.Expanding, QSizePolicy.Expanding),
            height=cons.WSIZE*1.5,
        )

        self.creature_type_list = ["Brute","Fighter","Specialist","Rogue","Ranger","Caster"]
        for number,creature in enumerate(self.creature_type_list):
            number = number + 1
            self.creature_button = Widget(
                widget_type=QPushButton(),
                stylesheet=style.CREATURE_BUTTONS,
                text=creature,
                parent_layout = self.creature_type_layout.inner_layout(1),
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                objectname=creature,
                checkable=True,
                signal=functools.partial(efunc.set_creature_type, self, creature, self.creature_type_list),
                class_group=self.widget_group
            )

        self.creature_damage_combobox = Widget(
            widget_type=QComboBox(),
            parent_layout = self.creature_type_layout.inner_layout(2),
            stylesheet=style.QCOMBOBOX,
            text=[item for item in cons.ELEMENTS],
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            height=cons.WSIZE*1.5,
            objectname="damage_type",
            class_group=self.widget_group
        )

        self.add_creature_button = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BUTTONS,
            text="Add Creature",
            parent_layout = self.creature_type_layout.inner_layout(2),
            height=cons.WSIZE*1.5,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            objectname="Normal",
            signal=self.add_creature,
            class_group=self.widget_group
        )

        self.add_leader_button = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BUTTONS,
            text="Add Leader",
            parent_layout = self.creature_type_layout.inner_layout(2),
            height=cons.WSIZE*1.5,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            signal=self.add_creature,
            objectname="Leader",
            class_group=self.widget_group
        )

        for widget in self.widget_group:
            widget.connect_to_parent()
            widget.set_signal()

        for section in self.section_group:
            section.connect_to_parent()

        self.setStyleSheet(style.BASE_STYLE)
        self.setLayout(self.master_layout)
        self.setGeometry(-1000, 100, 700, 800)

    def clear_encounter(self):
        
        self.creature_list.clear()
        self.action_group.clear()

        efunc.clear_layout(self.creature_layout.inner_layout(1))     

        print(f"Encounter List: {self.creature_list}")

        for player in self.player_list:
            player_base = CreatureBase(player[0],"Player")
            ebase.character_gui_update(player_base)
            self.creature_layout.inner_layout(1).addWidget(player_base)

    def add_creature(self):
        rank = self.sender().objectName()
        for creature in self.creature_type_list:
            if self.findChild(QPushButton, creature).isChecked():
                creature_type = creature

        damage_type = self.creature_damage_combobox.get_widget().currentText()
        self.creature_list.append((creature_type, rank, damage_type))
        creature_base = CreatureBase(creature_type, rank)
        self.creature_layout.inner_layout(1).addWidget(creature_base)

    def add_player(self, player_name):
        player_base = CreatureBase(player_name,"Player")
        ebase.character_gui_update(player_base)
        self.player_encounter_list.append({"type":player_name, "rank":"Player", "init":player_base.get_init()})
        self.creature_layout.inner_layout(1).addWidget(player_base)
           
    def run_encounter(self):
        if self.sender().objectName() == "adventure":
            level = int(self.adventure_level_button.get_widget().text())
        else:
            level = int(self.world_level_button.get_widget().text())

        if self.creature_list == []:
            print("No creatures to add")
            return
        
        if self.player_encounter_list == []:
            print("No players to add")
            return

        adjusted_level = self.adjust_encounter_level(level,self.sender().objectName())

        print(self.player_encounter_list)

        encounter = Encounter(adjusted_level,self.creature_list,self.player_encounter_list).get_encounter()
        efunc.clear_layout(self.creature_layout.inner_layout(1))  
        for creature in encounter:
            if creature["rank"] == "Player":
                creature_base = CreatureBase(creature["type"],"Player")
                ebase.character_gui_update(creature_base) # Setting the player stats using the database
                self.creature_layout.inner_layout(1).addWidget(creature_base)
            else:
                creature_base = CreatureBase(creature["type"],creature["rank"])
                for attack,action in enumerate(creature["actions"]):
                    print(attack,creature["attacks"])
                    creature_action = CreatureAction(attack,action,creature["attacks"])
                    creature_base.get_action_layout().addWidget(creature_action)
                creature_base.set_creature_stats(creature) # Setting the create stats using the encounter class
                self.creature_layout.inner_layout(1).addWidget(creature_base)

    def adjust_encounter_level(self, level, stage):
        self.level = level
        self.start_level = level
        self.level_max = math.ceil(self.level*0.5)
        if "Leader" in [creature[1] for creature in self.creature_list]:
            self.level += self.level_max
            level_string = f"{stage.capitalize()} Encounter {self.start_level} with a +{self.level_max} difficulty"
        else:
            self.level_adjuster = random.randint(0, self.level_max)
            self.level += self.level_adjuster
            level_string = f"{stage.capitalize()} Encounter {self.start_level} with a +{self.level_adjuster} difficulty"

        title_label = self.creature_layout.get_title()[1]
        title_label.setText(level_string)
        return self.level

    def open_partyselect(self):
        self.party_select_gui = PartySelectGUI(self)
        self.party_select_gui.show()

    def mousePressEvent(self, event): #this is a very specific event used to subtract values when right clicking on a widget
        if event.button() == Qt.RightButton:
            widget = self.childAt(event.pos())
            if widget.objectName() in ["adventure_level"]:
                efunc.adjust_stat(self, "adventure_level", "subtract")
