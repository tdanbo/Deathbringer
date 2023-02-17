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

from gui_encounter import encounter_func as efunc

class EncounterGUI(QWidget):
    def __init__(self):
        super().__init__()

        #This list it to keep track of the creatures that are in the encounter
        self.encounter_list = []

        #Setting up layouts/sections
        self.encounter_main_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            spacing = 10, 

        )

        self.settings_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 2),
            parent_layout = self.encounter_main_layout.inner_layout(1),
            title="Settings",
            icon = ("encounter.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            group=(None,None,None),
            spacing = 10, 
        )

        self.adventure_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 2),
            parent_layout = self.settings_layout.inner_layout(1),
            title="Encounter Level",
            icon = ("adventure_level.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            group=(True,None,None),
        )

        self.creature_type_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 3),
            parent_layout = self.settings_layout.inner_layout(2),
            title="Creature Setup",
            icon = ("creature_setup.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            group=(True,None,None),
        )

        self.creature_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.encounter_main_layout.inner_layout(1),
            title="Encounter",
            icon = ("encounter.png",cons.WSIZE*1.5,cons.ICON_COLOR),
            group=(True,None,None),
        )

        self.adventure_level_button = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            text="3",
            objectname = "adventure_level",
            parent_layout=self.adventure_layout.inner_layout(1),
            size_policy=(QSizePolicy.Expanding, QSizePolicy.Expanding),
        )

        self.adventure_select_button = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BUTTONS,
            text="Run Adventure",
            objectname = "adventure_select",
            height=cons.WSIZE*1.5,
            parent_layout=self.adventure_layout.inner_layout(1),
            size_policy=(QSizePolicy.Expanding, QSizePolicy.Expanding),
        )

        self.pc_level_button = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            text="1",
            objectname = "pc_level",
            parent_layout=self.adventure_layout.inner_layout(2),
            size_policy=(QSizePolicy.Expanding, QSizePolicy.Expanding),
        )

        self.pc_select_button = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BUTTONS,
            text="Run Player",
            objectname = "pc_select",
            height=cons.WSIZE*1.5,
            parent_layout=self.adventure_layout.inner_layout(2),
            size_policy=(QSizePolicy.Expanding, QSizePolicy.Expanding),
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
                height=cons.WSIZE*1.5,
                objectname=creature,
                width=cons.WSIZE*3,
                checkable=True,
                signal=functools.partial(efunc.set_creature_type, self, creature, self.creature_list),
            )

            self.creature_button.get_widget().clicked.connect(functools.partial(efunc.set_creature_type, self, creature, self.creature_list))
            self.creature_type_layout.inner_layout(1).addWidget(self.creature_button.get_widget())

        self.creature_damage_combobox = Widget(
            widget_type=QComboBox(),
            parent_layout = self.creature_type_layout.inner_layout(2),
            stylesheet=style.QCOMBOBOX,
            text=[item for item in cons.ELEMENTS],
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            height=cons.WSIZE*1.5,
            objectname="damage_type",
        )

        self.add_creature_button = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BUTTONS,
            text="Add Creature",
            parent_layout = self.creature_type_layout.inner_layout(3),
            height=cons.WSIZE*1.5,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            #signal=self.add_creature(self.creature_damage_combobox.get_widget().currentText()),
            objectname="add_creature",
        )

        self.add_leader_button = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BUTTONS,
            text="Add Leader",
            parent_layout = self.creature_type_layout.inner_layout(3),
            height=cons.WSIZE*1.5,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            #signal=self.add_creature(self.creature_damage_combobox.get_widget().currentText()),
            objectname="add_leader",
        )

        self.clear_creature_button = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BUTTONS,
            text="Clear Encounter",
            parent_layout = self.creature_type_layout.inner_layout(3),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            height=cons.WSIZE*1.5,
            objectname="clear_creature",
        )

        self.add_creature_button.get_widget().clicked.connect(self.add_creature)
            
        self.creature_type_layout.inner_layout(2).addWidget(self.creature_damage_combobox.get_widget())
        self.creature_type_layout.inner_layout(2).addWidget(self.add_creature_button.get_widget())
        self.creature_type_layout.inner_layout(2).addWidget(self.add_leader_button.get_widget())
        #self.creature_type_layout.inner_layout(3).addWidget(self.clear_creature_button.get_widget())

        self.adventure_layout.inner_layout(1).addWidget(self.adventure_level_button.get_widget())
        self.adventure_layout.inner_layout(1).addWidget(self.adventure_select_button.get_widget())

        self.adventure_layout.inner_layout(2).addWidget(self.pc_level_button.get_widget())    
        self.adventure_layout.inner_layout(2).addWidget(self.pc_select_button.get_widget())

        self.encounter_main_layout.inner_layout(1).addLayout(self.settings_layout.outer_layout())
        self.encounter_main_layout.inner_layout(1).addLayout(self.creature_layout.outer_layout())
        self.settings_layout.inner_layout(1).addLayout(self.adventure_layout.outer_layout())
        self.settings_layout.inner_layout(1).addLayout(self.creature_type_layout.outer_layout())


        self.setStyleSheet(style.BASE_STYLE)
        self.setLayout(self.encounter_main_layout.outer_layout())
    
    def add_creature(self,damage_type):
        for creature in self.creature_list:
            if self.findChild(QPushButton, creature).isChecked():
                creature_type = creature

        damage_type = self.creature_damage_combobox.get_widget().currentText()
        self.encounter_list.append((creature_type,"Normal",damage_type))
        print(self.encounter_list)
        self.add_gui_creatures()

    def add_gui_creatures(self):
        encounter = Encounter(1,self.encounter_list).get_stats()
        
        for creature in encounter :

            creature_details = encounter[creature]
            print(creature_details)

            self.creature_main_layout = Section(
                outer_layout = QVBoxLayout(),
                inner_layout = ("VBox", 1),
                spacing = 10, 
            )
            self.creature_button = Widget(
                widget_type=QPushButton(),
                stylesheet=style.BUTTONS,
                text=creature_details["type"],
                parent_layout = self.creature_main_layout.inner_layout(1),
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                height=cons.WSIZE*1.5,
                objectname=creature_details["type"],
            )

            self.creature_layout.inner_layout(1).addLayout(self.creature_main_layout.outer_layout())
            self.creature_main_layout.inner_layout(1).addWidget(self.creature_button.get_widget())

    # def mousePressEvent(self, event): #this is a very specific event used to subtract values when right clicking on a widget
    #     if event.button() == Qt.RightButton:
    #         widget = self.childAt(event.pos())
    #         #if widget.objectName() in []:
    #         print("Right button was clicked on a stat widget")
