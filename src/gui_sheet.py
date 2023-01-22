from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from pyside import Section
from pyside import Widget

import functions as func
import constants as cons
from character_sheet import CharacterSheet

import stylesheet as style

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
            group = (True,113,cons.WSIZE*3),
            title = "Beasttoe",
            parent_layout = self.character_basic.inner_layout(1),
        )

        self.stat_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 6),
            parent_layout = self.character_basic.inner_layout(1),
            group = (True,None,cons.WSIZE*3),
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

        self.hp_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 2),
            parent_layout = self.combat_layout.inner_layout(1),
            group = (True,None,cons.WSIZE*3),
            title = "HP",
            icon = ("hp.png",cons.WSIZE/2,cons.ICON_COLOR) 
        )

        self.defense_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.combat_layout.inner_layout(1),
            group = (True,None,cons.WSIZE*3),
            title = "AC",
            icon = ("armorclass.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.feat_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 2),
            parent_layout = self.combat_layout.inner_layout(1),
            group = (True,None,cons.WSIZE*3),
            title = "FEATS",
            icon = ("feats.png",cons.WSIZE/2,cons.ICON_COLOR)
        )

        self.initiative_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.combat_layout.inner_layout(1),
            group = (True,None,cons.WSIZE*3),
            title = "INIT",
            icon = ("initiative.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.inventory_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            title = "INVENTORY",
            group = (True,None,None),
            icon = ("backpack.png",cons.WSIZE/2,cons.ICON_COLOR),
            scroll=(True,"top"),	 
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
            group = (True,None,cons.WSIZE*2),
            icon = ("herodice.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.corruption_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_lower_basic.inner_layout(1),
            group = (True,None,cons.WSIZE*2),
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
            self.feats = Widget(
                widget_type=QToolButton(),
                stylesheet=style.QTOOLBUTTON,
                parent_layout = self.feat_layout.inner_layout(layout_nr),
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                signal=lambda: CharacterSheet(self).update_dictionary(),
                objectname=f"feat{number}",
            )

        for number in range(1,11):
            self.hero_dice = Widget(
                widget_type=QToolButton(),
                stylesheet=style.QTOOLBUTTON,
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
                stylesheet=style.QSTATS,
                text=stat,               
                height = cons.WSIZE/1.25,
                parent_layout = self.stat_layout.inner_layout(number),
            )
            self.stat_label = Widget(
                widget_type=QLineEdit(),
                stylesheet=style.QSTATS,
                height = cons.WSIZE*1.5,
                align = "center",
                text="0",
                parent_layout = self.stat_layout.inner_layout(number),
                signal=lambda: CharacterSheet(self).update_dictionary(),
                objectname=stat,
            )

        #INITIATIVE AND AC AND HP FEATS
        self.initiative_stat_label = Widget(
            widget_type=QPushButton(),
            text="0",
            parent_layout = self.initiative_layout.inner_layout(1),
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname="initiative",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.character_ac = Widget(
            widget_type=QPushButton(),
            stylesheet=style.QPUSHBUTTON,
            parent_layout=self.defense_layout.inner_layout(1),
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname = "ac",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.character_hp_max = Widget(
            widget_type=QPushButton(),
            stylesheet=style.QPUSHBUTTON,
            parent_layout=self.hp_layout.inner_layout(1),
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname = "max_hp",
            text = cons.HIT_DICE,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.character_hp_current= Widget(
            widget_type=QPushButton(),
            stylesheet=style.QPUSHBUTTON,
            parent_layout=self.hp_layout.inner_layout(1),
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname = "current_hp",
            text = "0",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.character_hp_minus = Widget(
            widget_type=QPushButton(),
            stylesheet=style.QPUSHBUTTON,
            text="-",
            parent_layout=self.hp_layout.inner_layout(2),
            signal=lambda: CharacterSheet(self).adjust_hp("minus",self.character_hp_line.get_widget().text()),
            objectname = "hp_minus",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.character_hp_line = Widget(
            widget_type=QLineEdit(),
            stylesheet=style.QLINEEDIT,
            text="",
            align="center",
            parent_layout=self.hp_layout.inner_layout(2),
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname = "hp_adjuster",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            width=cons.WSIZE*2,
        )

        self.character_hp_plus = Widget(
            widget_type=QPushButton(),
            stylesheet=style.QPUSHBUTTON,
            text="+",
            parent_layout=self.hp_layout.inner_layout(2),
            signal=lambda: CharacterSheet(self).adjust_hp("plus",self.character_hp_line.get_widget().text()),
            objectname = "hp_plus",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )


        self.portrait = Widget(
            widget_type=QLabel(),
            parent_layout=self.portrais_layout.inner_layout(1),
            icon=("beasttoe_portrait.png","",""),
            align="center",
        )


        for count in range(1,cons.MAX_SLOTS+1):
            self.slot_layot = Section(
                outer_layout = QVBoxLayout(),
                inner_layout = ("HBox", 1),
                parent_layout=self.inventory_layout.inner_layout(1),
            )
            self.backpack= Widget(
                widget_type=QToolButton(),
                stylesheet=style.INVENTORY,
                text="",
                parent_layout=self.slot_layot.inner_layout(1),
                width = cons.WSIZE*1.50,
                height = cons.WSIZE*1.50,
                enabled=False,
                objectname=f"icon{count}",
            )
            self.backpack_item = Widget(
                widget_type=QLineEdit(),
                stylesheet=style.INVENTORY,
                parent_layout=self.slot_layot.inner_layout(1),
                height = cons.WSIZE*1.50,
                signal=lambda: CharacterSheet(self).update_dictionary(),
                objectname=f"inventory{count}",
                align="center",
                enabled=False,

            )
            self.backpack= Widget(
                widget_type=QPushButton(),
                stylesheet=style.INVENTORY,
                text="",
                parent_layout=self.slot_layot.inner_layout(1),
                width = cons.WSIZE*3,
                height = cons.WSIZE*1.50,
                enabled=False,
                objectname=f"action{count}",
            )
            self.backpack= Widget(
                widget_type=QPushButton(),
                stylesheet=style.INVENTORY,
                text="",
                parent_layout=self.slot_layot.inner_layout(1),
                width = cons.WSIZE*2,
                height = cons.WSIZE*1.50,
                enabled=False,
                objectname=f"modifier{count}",
            )
            self.weapon_modifier = Widget(
                widget_type=QPushButton(),
                stylesheet=style.INVENTORY,
                parent_layout=self.slot_layot.inner_layout(1),
                width = cons.WSIZE*2,
                height = cons.WSIZE*1.50,
                objectname=f"roll{count}",
                enabled=False,
            )

        for count in range(1,11):
            self.corruption_icon = Widget(
                widget_type=QToolButton(),
                stylesheet=style.QTOOLBUTTON,
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