from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

# import functools
from pyside import Section
from pyside import Widget

import constants as cons
import stylesheet as style
import functools

from gui_functions import custom_rolls
from gui_functions import custom_log
from gui_functions import roll

from gui_encounter.encounter import Encounter
from gui_encounter.encounter_party_gui import PartySelectGUI

from gui_encounter import encounter_func as efunc



class EncounterGUI(QWidget):
    def __init__(self):
        super().__init__()

        #This list it to keep track of the creatures that are in the encounter
        self.master_layout = QVBoxLayout()
        self.encounter_list = []
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
            spacing=5,
            class_group=self.section_group
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
            text="3",
            objectname = "adventure_level",
            parent_layout=self.adventure_layout.inner_layout(1),
            class_group=self.widget_group,
            size_policy=(QSizePolicy.Expanding, QSizePolicy.Expanding),
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
            text="1",
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

        self.creature_list = ["Brute","Fighter","Specialist","Rogue","Ranger","Caster"]
        for number,creature in enumerate(self.creature_list):
            number = number + 1
            self.creature_button = Widget(
                widget_type=QPushButton(),
                stylesheet=style.CREATURE_BUTTONS,
                text=creature,
                parent_layout = self.creature_type_layout.inner_layout(1),
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                objectname=creature,
                checkable=True,
                signal=functools.partial(efunc.set_creature_type, self, creature, self.creature_list),
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
            #signal=self.add_creature(self.creature_damage_combobox.get_widget().currentText()),
            objectname="add_creature",
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
            #signal=self.add_creature(self.creature_damage_combobox.get_widget().currentText()),
            objectname="add_leader",
            class_group=self.widget_group
        )

        for widget in self.widget_group:
            widget.connect_to_parent()
            widget.set_signal()

        for section in self.section_group:
            section.connect_to_parent()

        self.setStyleSheet(style.BASE_STYLE)
        self.setLayout(self.master_layout)
    
    def add_creature(self,damage_type):
        for creature in self.creature_list:
            if self.findChild(QPushButton, creature).isChecked():
                creature_type = creature

        damage_type = self.creature_damage_combobox.get_widget().currentText()
        self.encounter_list.append((creature_type,"Normal",damage_type))
        print(self.encounter_list)
        creature_count = len(self.encounter_list)-1
        self.add_gui_creatures(creature_type,creature_count)

    def add_gui_creatures(self,creature_type,creature_count):
        print("adding creature")
        print(creature_count)
        self.creature_main_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.creature_layout.inner_layout(1),
            spacing=3,
            group=True
        )

        self.base_stats_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.creature_main_layout.inner_layout(1),
        )

        self.action_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.creature_main_layout.inner_layout(1),
            class_group=self.action_group
        )

        self.initiative_label = Widget(
            widget_type=QLabel(),
            text="",
            parent_layout = self.base_stats_layout.inner_layout(1),
            width=cons.WSIZE*1.5,
            objectname=f"init{creature_count}",
            stylesheet=style.INVENTORY,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.hp_label = Widget(
            widget_type=QPushButton(),
            text="",
            parent_layout = self.base_stats_layout.inner_layout(1),
            width=cons.WSIZE*1.5,
            objectname=f"hp{creature_count}",
            stylesheet=style.INVENTORY,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.ac_label = Widget(
            widget_type=QPushButton(),
            text="",
            parent_layout = self.base_stats_layout.inner_layout(1),
            width=cons.WSIZE*1.5,
            objectname=f"ac{creature_count}",
            stylesheet=style.INVENTORY,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.creature_type_label = Widget(
            widget_type=QPushButton(),
            stylesheet=style.INVENTORY,
            text=creature_type,
            parent_layout = self.base_stats_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            objectname=f"type{creature_count}",
        )

        self.hp_label.connect_to_parent()
        self.ac_label.connect_to_parent()
        self.creature_type_label.connect_to_parent()
        self.initiative_label.connect_to_parent()

        self.base_stats_layout.connect_to_parent()
        self.action_layout.connect_to_parent()
        self.creature_main_layout.connect_to_parent()
 

    def run_encounter(self):
        print(self.sender().objectName())
        if self.sender().objectName() == "adventure":
            level = int(self.adventure_level_button.get_widget().text())
        else:
            level = int(self.pc_level_button.get_widget().text())

        print(f"Running encounter at level {level} for {self.sender().objectName()}")

        if self.encounter_list == []:
            print("No creatures in encounter")
            return
        else:
            encounter = Encounter(level,self.encounter_list).get_encounter()
            for position, creature in enumerate(encounter):
                self.update_creature_gui(position,creature)

    def update_creature_gui(self,position,creature):
        print(position)
        for stat in creature:
            widget = stat+str(position)
            value = str(creature[stat])
            try:          
                self.findChild(QWidget, widget).setText(value) 
            except:
                print(f"Could not find {stat}{position}")

        for action in creature["actions"]:
            action_dict = creature["actions"][action]
            for key,value in action_dict.items():
                print(creature["actions"])

                self.single_action_layout = Section(
                    outer_layout = QHBoxLayout(),
                    inner_layout = ("HBox", 1),
                    parent_layout = self.action_group[position].inner_layout(1),
                )

                self.action_button1 = Widget(
                    widget_type=QPushButton(),
                    stylesheet=style.INVENTORY,
                    text=key,
                    parent_layout = self.single_action_layout.inner_layout(1),
                    objectname=f"action1{position}",
                )

                self.action_button2 = Widget(
                    widget_type=QPushButton(),
                    stylesheet=style.INVENTORY,
                    text=value,
                    parent_layout = self.single_action_layout.inner_layout(1),
                    objectname=f"action2{position}",
                )

                self.single_action_layout.connect_to_parent()
                self.action_button1.connect_to_parent()
                self.action_button2.connect_to_parent()
                

    def open_partyselect(self):
        self.party_select_gui = PartySelectGUI(self)
        self.party_select_gui.show()

    # def mousePressEvent(self, event): #this is a very specific event used to subtract values when right clicking on a widget
    #     if event.button() == Qt.RightButton:
    #         widget = self.childAt(event.pos())
    #         #if widget.objectName() in []:
    #         print("Right button was clicked on a stat widget")
