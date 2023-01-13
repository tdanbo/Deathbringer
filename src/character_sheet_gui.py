from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from my_pyside import Section
from my_pyside import Widget

import constants as cons

class CharacterSheetGUI:
    def __init__(self):
        self.character_sheet_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            spacing = 10,     
        )

        self.character_basic = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            spacing=10,     
        )

        self.stat_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 6),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            group = True,
            title = "STATS",
            spacing=0,    
        )

        self.name_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 3),
            parent_layout = self.character_basic.inner_layout(1),
            group = True,
            title = "CHARACTER"  
        )

        self.defense_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_basic.inner_layout(1),
            group = True,
            title = "DEFENSE"     
        )

        self.deathbringer_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 3),
            parent_layout = self.defense_layout.inner_layout(1),
            #title = "HERO DICE",
            spacing = 10,
            group = True,	
        )

        self.equipment_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 4),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            group = True,
            title = "WEAPONS" 
        )
        
        self.armor_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            group = True,
            title = "ARMOR" 
        )

        self.backpack_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 11),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            group = True,
            title = "BACKPACK" 
        )

        self.corruption_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            group = True,
            title = "CORRUPTION"
        )

        for number in range(9):
            if number <= 2:
                index = 1
                print("1")
            elif number <= 5:
                index = 2
                print("2")
            else:
                index = 3
                print("3")

            self.deathbringer_dice = Widget(
                widget_type=QToolButton(),
                checkable=True,
                parent_layout = self.deathbringer_layout.inner_layout(index),
                icon=("skull.png",cons.WSIZE/1.5),
                #width = cons.WSIZE,
                #height = cons.WSIZE
            )

        for number,stat in enumerate(["STR", "DEX", "CON", "INT", "WIS", "CHA"]):
            self.stat_label = Widget(
                widget_type=QLineEdit(),
                enabled=False,
                text=stat,               
                width = cons.WSIZE*2,
                height = cons.WSIZE,
                align = "center",
                parent_layout = self.stat_layout.inner_layout(number)
            )
            self.stat_label = Widget(
                widget_type=QSpinBox(),
                width = cons.WSIZE*2,
                height = cons.WSIZE,
                align = "center",
                text=0,
                parent_layout = self.stat_layout.inner_layout(number),
                stylesheet="padding-left: 10px;"
            )

        self.character_name_widget = Widget(
            widget_type=QLineEdit(),
            text="Character Name",
            parent_layout=self.name_layout.inner_layout(1),
        )

        self.character_level_widget = Widget(
            widget_type=QLineEdit(),
            text="Level",
            parent_layout=self.name_layout.inner_layout(2),
        )

        self.character_xp_widget = Widget(
            widget_type=QLineEdit(),
            text="Coins",
            parent_layout=self.name_layout.inner_layout(3),
        )
        self.character_ac_widget = Widget(
            widget_type=QLineEdit(),
            text="AC",
            align="center",
            parent_layout=self.defense_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet=f"font-size: {cons.WSIZE/2}px;"
        )
        self.character_hp_widget = Widget(
            widget_type=QLineEdit(),
            text="HP",
            align="center",
            parent_layout=self.defense_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet=f"font-size: {cons.WSIZE/2}px;"
        )

        for count in range(1,4):
            print(count)
            self.weapon_icon = Widget(
                widget_type=QToolButton(),
                parent_layout=self.equipment_layout.inner_layout(count),
                width = cons.WSIZE,
                height = cons.WSIZE,
                icon = ("attack.png",cons.WSIZE/2)	
            )
            self.weapon_attack = Widget(
                widget_type=QPushButton(),
                text="Attack",
                parent_layout=self.equipment_layout.inner_layout(count),
                width = 60,
                height = cons.WSIZE
            )
            self.weapon_line = Widget(
                widget_type=QLineEdit(),
                parent_layout=self.equipment_layout.inner_layout(count),
                height = cons.WSIZE
            )

        self.armor_icon = Widget(
            widget_type=QToolButton(),
            parent_layout=self.armor_layout.inner_layout(1),
            width = cons.WSIZE,
            height = cons.WSIZE,
            icon = ("defend.png",cons.WSIZE/2)	
        )
        self.armor_defend = Widget(
            widget_type=QPushButton(),
            text="Defend",
            parent_layout=self.armor_layout.inner_layout(1),
            width = 60,
            height = cons.WSIZE
        )
        self.armor_line = Widget(
            widget_type=QLineEdit(),
            parent_layout=self.armor_layout.inner_layout(1),
            height = cons.WSIZE
        )        

        for count in range(1,11):
            print(count)
            self.backpack_icon = Widget(
                widget_type=QToolBox(),
                parent_layout=self.backpack_layout.inner_layout(count),
                width = cons.WSIZE/2,
                height = cons.WSIZE/2
            )
            self.backpack_line = Widget(
                widget_type=QLineEdit(),
                parent_layout=self.backpack_layout.inner_layout(count),
            )

        for count in range(0,10):
            print(count)
            self.corruption_icon = Widget(
                widget_type=QToolButton(),
                parent_layout=self.corruption_layout.inner_layout(1),
                width = cons.WSIZE/3,
                height = cons.WSIZE/3,
                checkable=True
            )    

    def get_main_layout(self):
        return self.character_sheet_layout.outer_layout()