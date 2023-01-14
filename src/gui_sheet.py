from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from my_pyside import Section
from my_pyside import Widget

import functions as func
import constants as cons
from character_sheet import CharacterSheet

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
            icon = ("stats.png",cons.WSIZE/2,cons.ICON_COLOR)	

        )

        self.name_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 3),
            parent_layout = self.character_basic.inner_layout(1),
            group = True,
            title = "CHARACTER",
            icon = ("character.png",cons.WSIZE/2,cons.ICON_COLOR)	  
        )

        self.initiative_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_basic.inner_layout(1),
            group = True,
            title = "INITIATIVE",
            icon = ("initiative.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.defense_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_basic.inner_layout(1),
            group = True,
            title = "ARMOR CLASS",
            icon = ("armorclass.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.hp_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_basic.inner_layout(1),
            group = True,
            title = "HEALTH POINTS",
            icon = ("hp.png",cons.WSIZE/2,cons.ICON_COLOR) 
        )

        self.equipment_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 4),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            group = True,
            title = "WEAPONS",
            icon = ("weapons.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )
        
        self.armor_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            group = True,
            title = "ARMOR",
            icon = ("armor.png",cons.WSIZE/2,cons.ICON_COLOR)	  
        )

        self.backpack_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 11),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            group = True,
            title = "BACKPACK",
            icon = ("backpack.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.character_lower_basic = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            spacing=10,     
        )

        self.deathbringer_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_lower_basic.inner_layout(1),
            title = "HERO DICE",
            spacing = 5,
            group = True,
            icon = ("herodice.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.corruption_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_lower_basic.inner_layout(1),
            group = True,
            spacing = 5,
            title = "CORRUPTION",
            icon = ("corruption.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        for number in range(10):
            self.deathbringer_dice = Widget(
                widget_type=QToolButton(),
                checkable=True,
                parent_layout = self.deathbringer_layout.inner_layout(1),
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                height=cons.WSIZE/1.25,
                signal=lambda: CharacterSheet().update()
            )

        for number,stat in enumerate(["STR", "DEX", "CON", "INT", "WIS", "CHA"]):
            self.stat_label = Widget(
                widget_type=QPushButton(),
                text=stat,               
                height = cons.WSIZE,
                parent_layout = self.stat_layout.inner_layout(number),
            )
            self.stat_label = Widget(
                widget_type=QSpinBox(),
                height = cons.WSIZE*2,
                align = "center",
                text=0,
                parent_layout = self.stat_layout.inner_layout(number),
                stylesheet="font-size: 18px; padding-left: 20px;",
                signal=func.character_sheet_json()
            )

        self.character_name_widget = Widget(
            widget_type=QLineEdit(),
            text="Character Name",
            parent_layout=self.name_layout.inner_layout(1),
            signal=lambda: CharacterSheet().update()
        )

        self.character_level_widget = Widget(
            widget_type=QLineEdit(),
            text="Level",
            parent_layout=self.name_layout.inner_layout(2),
            signal=lambda: CharacterSheet().update()
        )

        self.character_xp_widget = Widget(
            widget_type=QLineEdit(),
            text="Coins",
            parent_layout=self.name_layout.inner_layout(3),
            signal=lambda: CharacterSheet().update()
        )
        self.character_ac_widget = Widget(
            widget_type=QLineEdit(),
            text="0",
            align="center",
            parent_layout=self.defense_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet="font-size: 15px;",
            signal=lambda: CharacterSheet().update()
        )
        self.character_hp_widget = Widget(
            widget_type=QLineEdit(),
            text="0",
            align="center",
            parent_layout=self.hp_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet="font-size: 15px;",
            signal=lambda: CharacterSheet().update()
        )

        self.character_initiative_widget = Widget(
            widget_type=QLineEdit(),
            text="0",
            align="center",
            parent_layout=self.initiative_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet="font-size: 15px;",
        )

        for count in range(1,4):
            self.weapon_attack = Widget(
                widget_type=QPushButton(),
                text="Attack",
                parent_layout=self.equipment_layout.inner_layout(count),
                width = cons.WSIZE*2.5,
                height = cons.WSIZE
            )
            self.weapon_line = Widget(
                widget_type=QComboBox(),
                parent_layout=self.equipment_layout.inner_layout(count),
                height = cons.WSIZE,
                signal=lambda: CharacterSheet().update()
            )

        self.armor_defend = Widget(
            widget_type=QPushButton(),
            text="Defend",
            parent_layout=self.armor_layout.inner_layout(1),
            width = cons.WSIZE*2.5,
            height = cons.WSIZE
        )
        self.armor_line = Widget(
            widget_type=QComboBox(),
            parent_layout=self.armor_layout.inner_layout(1),
            height = cons.WSIZE,
            signal=lambda: CharacterSheet().update()
        )        

        for count in range(1,11):
            self.armor_defend = Widget(
                widget_type=QPushButton(),
                text="Misc",
                parent_layout=self.backpack_layout.inner_layout(count),
                width = cons.WSIZE*2.5,
                height = cons.WSIZE
            )
            self.backpack_line = Widget(
                widget_type=QLineEdit(),
                parent_layout=self.backpack_layout.inner_layout(count),
                height = cons.WSIZE,
                signal=lambda: CharacterSheet().update()

            )

        for count in range(0,10):
            self.corruption_icon = Widget(
                widget_type=QToolButton(),
                parent_layout=self.corruption_layout.inner_layout(1),
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                height=cons.WSIZE/1.25,
                checkable=True,
                signal=lambda: CharacterSheet().update()
            )    

    def get_main_layout(self):
        return self.character_sheet_layout.outer_layout()