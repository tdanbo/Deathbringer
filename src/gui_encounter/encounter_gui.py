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
            spacing=10,
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
            text="7",
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

        self.section_creatures_group = []
        self.widget_creatures_group = []

        self.single_creature_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 5),
            parent_layout=self.creature_layout.inner_layout(1),
            class_group=self.section_creatures_group
        )   

        self.slot_layot = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 11),
            parent_layout=self.single_creature_layout.inner_layout(1),
            class_group=self.section_creatures_group,
            content_margin=(0,0,8,1)
        ) 

        self.action_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout=self.single_creature_layout.inner_layout(1),
            class_group=self.action_group
        )   

        self.hp = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            parent_layout=self.slot_layot.inner_layout(1),
            width = cons.WSIZE*2,
            height = cons.WSIZE*2,
            objectname=f"hp{creature_count}",
            signal=functools.partial(roll.inventory_prepare_double_roll, self,creature_count),
            class_group=self.widget_creatures_group,
        )

        self.hp_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(1),
            height = cons.WSIZE/1.5,
            objectname=f"max hp{creature_count}",
            text="HP",
            align="center",
            class_group=self.widget_creatures_group,
            width = cons.WSIZE*2
        )

        self.ac = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            parent_layout=self.slot_layot.inner_layout(2),
            width = cons.WSIZE*2,
            height = cons.WSIZE*2,
            objectname=f"ac{creature_count}",
            signal=functools.partial(roll.inventory_prepare_double_roll, self,creature_count),
            class_group=self.widget_creatures_group,
        )

        self.ac_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(2),
            height = cons.WSIZE/1.5,
            objectname=f"icon_label{creature_count}",
            text="AC",
            align="center",
            class_group=self.widget_creatures_group,
            width = cons.WSIZE*2
        )

        self.passive = Widget(
            widget_type=QToolButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(3),
            width = cons.WSIZE*2,
            height = cons.WSIZE*2,
            objectname=f"passive{creature_count}",
            signal=functools.partial(roll.inventory_prepare_double_roll, self,creature_count),
            class_group=self.widget_creatures_group,
        )

        self.passive_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(3),
            height = cons.WSIZE/1.5,
            objectname=f"passive_label{creature_count}",
            text="MOD",
            align="center",
            class_group=self.widget_creatures_group,
            width = cons.WSIZE*2
        )

        self.icon = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(4),
            width = cons.WSIZE*5,
            height = cons.WSIZE*2,
            objectname=f"icon{creature_count}",
            class_group=self.widget_creatures_group,
            icon=(f"{creature_type}.png","","",100),
        )

        self.icon_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(4),
            height = cons.WSIZE/1.5,
            objectname=f"speed{creature_count}",
            text="",
            align="center",
            class_group=self.widget_creatures_group,
            width = cons.WSIZE*5,
        )

        self.backpack_item = Widget(
            widget_type=QLineEdit(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(5),
            height = cons.WSIZE*2,
            #signal= self.select_item,
            objectname=f"type{creature_count}",
            align="center",
            class_group=self.widget_creatures_group,
            text=f"{creature_type}"

        )

        self.initiative = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            text="",
            parent_layout=self.slot_layot.inner_layout(5),
            height = cons.WSIZE/1.5,
            objectname=f"init{creature_count}",
            align="center",
            class_group=self.widget_creatures_group
        )

        for number, stat in enumerate(["STR", "DEX", "CON", "INT", "WIS", "CHA"]):
            self.stat = Widget(
                widget_type=QPushButton(),
                stylesheet=style.INVENTORY,
                parent_layout=self.slot_layot.inner_layout(number+6),
                width = cons.WSIZE*1.40,
                height = cons.WSIZE*2,
                objectname=f"{stat}{creature_count}",
                #signal = functools.partial(roll.inventory_prepare_roll, self, "roll", creature_count),
                class_group=self.widget_creatures_group,
                text="",

            )

            self.stat_label = Widget(
                widget_type=QLabel(),
                stylesheet=style.INVENTORY,
                text=stat,
                parent_layout=self.slot_layot.inner_layout(number+6),
                height = cons.WSIZE/1.5,
                objectname=f"stat_label{creature_count}",
                align="center",
                class_group=self.widget_creatures_group
            )

        for s in self.section_creatures_group:
            s.connect_to_parent()

        for s in self.action_group:
            s.connect_to_parent()

        for w in self.widget_creatures_group:
            w.connect_to_parent()
            w.set_signal()

    # 
    # Below is the sections that generates the actions bars for each creature
    #

    def create_gui_action(self, action, attack, position):

        if len(action["Modifiers"]) == 0:
            modifier1icon = ""
            modifier2icon = ""
        if len(action["Modifiers"]) == 1:
            modifier1icon = f'{action["Modifiers"][0]}.png'
            modifier2icon = ""
        if len(action["Modifiers"]) == 2:
            modifier1icon = f'{action["Modifiers"][0]}.png'
            modifier2icon = f'{action["Modifiers"][1]}.png'


        self.slot_layot = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 8),
            parent_layout=self.action_group[position].inner_layout(1),
            content_margin=(0,0,8,0),
            class_group=self.section_group
        )

        self.backpack= Widget(
            widget_type=QToolButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(1),
            width = cons.WSIZE*2,
            height = cons.WSIZE,
            objectname=f"icon{position}",
            signal=functools.partial(roll.inventory_prepare_double_roll, self,position),
            class_group=self.widget_group,
            icon=("weapon.png",cons.WSIZE*1.5,cons.ICON_COLOR),
        )

        self.backpack_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(1),
            height = cons.WSIZE/1.5,
            objectname=f"icon_label{position}",
            text=f"{attack+1}.",
            align="center",
            class_group=self.widget_group,
            width = cons.WSIZE*2
        )

        self.first_mod= Widget(
            widget_type=QToolButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(2),
            width = cons.WSIZE*2,
            height = cons.WSIZE,
            objectname=f"first_mod{position}",
            signal=functools.partial(roll.inventory_prepare_double_roll, self,position),
            class_group=self.widget_group,
            icon=(modifier1icon,cons.WSIZE*1.5,cons.ICON_COLOR),
        )

        self.first_mod_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(2),
            height = cons.WSIZE/1.5,
            objectname=f"first_mod_label{position}",
            text="",
            align="center",
            class_group=self.widget_group,
            width = cons.WSIZE*2
        )

        self.second_mod= Widget(
            widget_type=QToolButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(3),
            width = cons.WSIZE*2,
            height = cons.WSIZE,
            objectname=f"icon{position}",
            signal=functools.partial(roll.inventory_prepare_double_roll, self,position),
            class_group=self.widget_group,
            icon=(modifier2icon,cons.WSIZE*1.5,cons.ICON_COLOR),
        )

        self.second_mod_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(3),
            height = cons.WSIZE/1.5,
            objectname=f"icon_label{position}",
            text="",
            align="center",
            class_group=self.widget_group,
            width = cons.WSIZE*2
        )

        self.spacer = Widget(
            widget_type=QPushButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(4),
            width = 130,
            height = cons.WSIZE,
            objectname=f"spacer{position}",
            class_group=self.widget_group,	
        )

        self.spacer_label = Widget(
            widget_type=QPushButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(4),
            height = cons.WSIZE/1.5,
            objectname=f"spacer_label{position}",
            class_group=self.widget_group,
            width = 130,
        )

        self.backpack_item = Widget(
            widget_type=QLineEdit(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(5),
            height = cons.WSIZE,
            #signal= self.select_item,
            objectname=f"inventory{position}",
            align="center",
            class_group=self.widget_group,
            text="Claw"

        )

        self.backpack_item_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            text="Creature Attack",
            parent_layout=self.slot_layot.inner_layout(5),
            height = cons.WSIZE/1.5,
            objectname=f"inventory_label{position}",
            align="center",
            class_group=self.widget_group
        )

        self.backpack_action= Widget(
            widget_type=QPushButton(),
            stylesheet=style.INVENTORY,
            text="21",
            parent_layout=self.slot_layot.inner_layout(6),
            width = cons.WSIZE*3,
            height = cons.WSIZE,
            objectname=f"evoke{position}",
            signal = functools.partial(roll.inventory_prepare_roll, self, "evoke", position),
            class_group=self.widget_group
        )

        self.defense_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            text="Defense",
            parent_layout=self.slot_layot.inner_layout(6),
            height = cons.WSIZE/1.5,  
            objectname=f"evoke_label{position}",
            align="center",
            class_group=self.widget_group
        )

        self.secondary_damage= Widget(
            widget_type=QPushButton(),
            stylesheet=style.INVENTORY,
            text=f'{action["Secondary Damage"]}',
            parent_layout=self.slot_layot.inner_layout(7),
            width = cons.WSIZE*3,
            height = cons.WSIZE,
            objectname=f"hit_dc{position}",
            signal = functools.partial(roll.inventory_prepare_roll, self, "hit_dc", position),
            class_group=self.widget_group
        )

        self.secondary_type = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            text=f'{action["Secondary Type"]}',
            parent_layout=self.slot_layot.inner_layout(7),
            height = cons.WSIZE/1.5,
            objectname=f"hit_dc_label{position}",
            align="center",
            class_group=self.widget_group
        )

        self.primary_damage = Widget(
            widget_type=QPushButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(8),
            width = cons.WSIZE*3,
            height = cons.WSIZE,
            objectname=f"roll{position}",
            signal = functools.partial(roll.inventory_prepare_roll, self, "roll", position),
            class_group=self.widget_group,
            text=f'{action["Primary Damage"]}',

        )

        self.primary_type = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            text=f'{action["Primary Type"]}',
            parent_layout=self.slot_layot.inner_layout(8),
            height = cons.WSIZE/1.5,
            objectname=f"roll_label{position}",
            align="center",
            class_group=self.widget_group
        )

        for s in self.section_group:
            s.connect_to_parent()

        for w in self.widget_group:
            w.connect_to_parent()
            w.set_signal()

    def update_creature_gui(self,position,creature):
        print(creature)
        for stat in creature:
            print(stat)
            widget = stat+str(position)
            value = str(creature[stat])
            if stat in ["passive","icon"]:
                try:
                    selected_widget = self.findChild(QWidget, widget)
                    icon_name = f"{value.lower()}.png"
                    if stat == "icon":      
                        func.set_icon(selected_widget,icon_name,"",100)
                    else:
                        func.set_icon(selected_widget,icon_name,cons.ICON_COLOR)
                except:
                    print(f"Could not find {stat}{position}")
            elif stat == "init":
                try:          
                    self.findChild(QWidget, widget).setText(f"Initiative {value}") 
                except:
                    print(f"Could not find {stat}{position}")
            else:
                try:          
                    self.findChild(QWidget, widget).setText(value) 
                except:
                    print(f"Could not find {stat}{position}")

        # set all stats
        for stat in creature["stats"]:
            widget = stat.upper()+str(position)
            value = str(creature["stats"][stat])
            try:          
                self.findChild(QWidget, widget).setText(value) 
            except:
                print(f"Could not find {stat}{position}")
        
        for attack, action in enumerate(creature["actions"]):
            self.create_gui_action(action,attack,position)

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

    def open_partyselect(self):
        self.party_select_gui = PartySelectGUI(self)
        self.party_select_gui.show()

    # def mousePressEvent(self, event): #this is a very specific event used to subtract values when right clicking on a widget
    #     if event.button() == Qt.RightButton:
    #         widget = self.childAt(event.pos())
    #         #if widget.objectName() in []:
    #         print("Right button was clicked on a stat widget")
