from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from my_pyside import Section
from my_pyside import Widget

import functions as func
import constants as cons
from character_sheet import CharacterSheet

class CharacterSheetGUI(QWidget):
    def __init__(self):
        super().__init__()
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

        self.portrais_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("HBox", 1),
            group = True,
            parent_layout = self.character_basic.inner_layout(1),
        )

        self.stat_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 6),
            parent_layout = self.character_basic.inner_layout(1),
            group = True,
            title = "STATS",
            spacing=0,
            icon = ("character.png",cons.WSIZE/2,cons.ICON_COLOR)	

        )

        self.combat_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            spacing=10,   
        )

        self.initiative_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.combat_layout.inner_layout(1),
            group = True,
            title = "INITIATIVE",
            icon = ("initiative.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.defense_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.combat_layout.inner_layout(1),
            group = True,
            title = "AC",
            icon = ("armorclass.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.feat_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 2),
            parent_layout = self.combat_layout.inner_layout(1),
            group = True,
            title = "FEATS",
            icon = ("feats.png",cons.WSIZE/2,cons.ICON_COLOR)
        )

        self.hp_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 2),
            parent_layout = self.combat_layout.inner_layout(1),
            group = True,
            title = "HP",
            icon = ("hp.png",cons.WSIZE/2,cons.ICON_COLOR) 
        )

        self.inventory_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 20),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            group = True,
            title = "INVENTORY",
            icon = ("backpack.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.character_lower_basic = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            spacing=10,     
        )

        self.herodice_layout = Section(
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
            icon = ("corruption.png",cons.WSIZE/2,cons.ICON_COLOR), 
        )

        #Below is all the widgets used in the character sheet


        for number in range(1,5):
            if number <= 2:
                layout_nr = 1
            else:
                layout_nr = 2
            self.portrait = Widget(
                widget_type=QToolButton(),
                checkable=True,
                parent_layout = self.feat_layout.inner_layout(layout_nr),
                height=cons.WSIZE*1.5,
                width=cons.WSIZE*1.5,
                signal=lambda: CharacterSheet(self).update_dictionary(),
                objectname=f"portrait{number}",
                enabled=False,
            )

        for number in range(1,11):
            self.hero_dice = Widget(
                widget_type=QToolButton(),
                checkable=True,
                parent_layout = self.herodice_layout.inner_layout(1),
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                height=cons.WSIZE/1.25,
                signal=lambda: CharacterSheet(self).update_dictionary(),
                objectname=f"herodice{number}",
                enabled=False,
            )

        for number,stat in enumerate(["STR", "DEX", "INT", "CON", "WIS", "CHA"]):
            number = number + 1
            self.stat_label = Widget(
                widget_type=QPushButton(),
                text=stat,               
                height = cons.WSIZE/1.25,
                parent_layout = self.stat_layout.inner_layout(number),
            )
            self.stat_label = Widget(
                widget_type=QSpinBox(),
                height = cons.WSIZE*1.5,
                align = "center",
                text=0,
                parent_layout = self.stat_layout.inner_layout(number),
                stylesheet="font-size: 18px; padding-left: 20px;",
                signal=lambda: CharacterSheet(self).update_dictionary(),
                objectname=stat,
            )
            self.stat_label.get_widget().lineEdit().setReadOnly(True)
            self.stat_label.get_widget().lineEdit().setEnabled(False)

        self.character_ac = Widget(
            widget_type=QPushButton(),
            text="0",
            parent_layout=self.defense_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet="font-size: 15px;",
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname = "ac"
        )

        self.character_hp_max = Widget(
            widget_type=QLineEdit(),
            text="0",
            align="center",
            parent_layout=self.hp_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet="font-size: 15px;",
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname = "hp",
        )

        self.character_hp_current= Widget(
            widget_type=QLineEdit(),
            text="0",
            align="center",
            parent_layout=self.hp_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet="font-size: 15px;",
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname = "hp",
        )

        self.character_hp_minus = Widget(
            widget_type=QPushButton(),
            text="-",
            parent_layout=self.hp_layout.inner_layout(2),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            signal=lambda: CharacterSheet(self).update_dictionary(),
            height=cons.WSIZE*1.5,
            width=cons.WSIZE*1.5,
            objectname = "hp_minus"
        )

        self.character_hp_line = Widget(
            widget_type=QLineEdit(),
            text="",
            align="center",
            parent_layout=self.hp_layout.inner_layout(2),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname = "hp_line"
        )

        self.character_hp_plus = Widget(
            widget_type=QPushButton(),
            text="+",
            parent_layout=self.hp_layout.inner_layout(2),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet="font-size: 15px;",
            height=cons.WSIZE*1.5,
            width=cons.WSIZE*1.5,
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname = "hp_plus"
        )

        self.character_initiative = Widget(
            widget_type=QPushButton(),
            text="0",
            parent_layout=self.initiative_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet="font-size: 15px;",
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname = "initiative"
        )

        self.portrait = Widget(
            widget_type=QLabel(),
            parent_layout=self.portrais_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            icon=("beasttoe.png",cons.WSIZE*3,""),
        )


        for count in range(1,21):
            self.backpack= Widget(
                widget_type=QPushButton(),
                text="",
                parent_layout=self.inventory_layout.inner_layout(count),
                width = cons.WSIZE*2.5,
                height = cons.WSIZE,
                enabled=False,
                objectname=f"selector{count}",
            )
            self.backpack= Widget(
                widget_type=QPushButton(),
                text="",
                parent_layout=self.inventory_layout.inner_layout(count),
                width = cons.WSIZE*2.5,
                height = cons.WSIZE,
                enabled=False,
                objectname=f"action{count}",
            )
            self.weapon_modifier = Widget(
                widget_type=QLineEdit(),
                parent_layout=self.inventory_layout.inner_layout(count),
                width = cons.WSIZE*2.5,
                height = cons.WSIZE,
                objectname=f"modifier{count}",
                enabled=False,
            )
            self.backpack_item = Widget(
                widget_type=QComboBox(),
                parent_layout=self.inventory_layout.inner_layout(count),
                height = cons.WSIZE,
                signal=lambda: CharacterSheet(self).update_dictionary(),
                objectname=f"inventory{count}",
                enabled=False,

            )

        for count in range(1,11):
            self.corruption_icon = Widget(
                widget_type=QToolButton(),
                parent_layout=self.corruption_layout.inner_layout(1),
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                height=cons.WSIZE/1.25,
                checkable=True,
                checked=False,	
                signal=lambda: CharacterSheet(self).update_dictionary(),
                objectname=f"corruption{count}",
                enabled=False,	
            )

        self.setLayout(self.character_sheet_layout.outer_layout())