from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from pyside import Section
from pyside import Widget

import functions as func
import constants as cons

from gui_spells import SpellsGUI
from gui_log import CombatLogGUI
from character_sheet import CharacterSheet

import functools
import stylesheet as style
from gui_feats import FeatsGUI
from gui_add_sub import AddSubGUI

from gui_functions import character_xp
from gui_functions import character_stats
from gui_functions import character_morale
from gui_functions import custom_rolls

class CharacterSheetGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.character_sheet_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            spacing = 10,     
        )

        self.character_basic = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            spacing=10,     
        )

        self.portrait_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 2),
            parent_layout = self.character_basic.inner_layout(1),
            group = (True,None,cons.WSIZE*4),
            title = "CHARACTER",
            icon = ("character.png",cons.WSIZE/2,cons.ICON_COLOR),
            spacing = 3,	

        )

        self.stat_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 7),
            parent_layout = self.character_basic.inner_layout(1),
            group = (True,None,cons.WSIZE*4),
            title = "STATS",
            icon = ("character.png",cons.WSIZE/2,cons.ICON_COLOR),
            spacing = 3,	

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
            icon = ("hp.png",cons.WSIZE/2,cons.ICON_COLOR), 
            spacing = 3,
        )

        self.morale_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 2),
            parent_layout = self.combat_layout.inner_layout(1),
            group = (True,None,cons.WSIZE*3),
            title = "MORALE",
            icon = ("feats.png",cons.WSIZE/2,cons.ICON_COLOR),
            spacing = 3,
        )

        self.defense_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.combat_layout.inner_layout(1),
            group = (True,None,cons.WSIZE*3),
            title = "AC",
            icon = ("armorclass.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.initiative_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.combat_layout.inner_layout(1),
            group = (True,None,cons.WSIZE*3),
            title = "Mobility",
            icon = ("initiative.png",cons.WSIZE/2,cons.ICON_COLOR),
            spacing = 3,	 
        )

        self.inventory_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            title = "INVENTORY",
            group = (True,None,None),
            icon = ("backpack.png",cons.WSIZE/2,cons.ICON_COLOR),
            scroll=(True,"top"),
            spacing=5,	 
        )

        self.character_lower_basic = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_sheet_layout.inner_layout(1),
            spacing=10,     
        )

        self.feats_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_lower_basic.inner_layout(1),
            title = "FEATS",
            spacing = 3,
            group = (True,None,cons.WSIZE*2.2),
            icon = ("feats.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.herodice_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_lower_basic.inner_layout(1),
            title = "FOCUS",
            spacing = 3,
            group = (True,None,cons.WSIZE*2.2),
            icon = ("focus.png",cons.WSIZE/2,cons.ICON_COLOR)	 
        )

        self.corruption_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 1),
            parent_layout = self.character_lower_basic.inner_layout(1),
            group = (True,None,cons.WSIZE*2.2),
            spacing = 3,
            title = "SPELL SLOTS",
            icon = ("spell.png",cons.WSIZE/2,cons.ICON_COLOR),
        )

        #Below is all the widgets used in the character sheet

        self.portrait = Widget(
            widget_type=QLabel(),
            parent_layout=self.portrait_layout.inner_layout(1),
            stylesheet=style.PORTRAIT,
            objectname="portrait",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            icon = ("beasttoe.png","",""),
        )

        self.character_name = Widget(
            widget_type=QComboBox(),
            parent_layout=self.portrait_layout.inner_layout(2),
            stylesheet=style.TEST_COMBO,
            objectname="name",
            text=["Beastoe","Decipio","Chakademus","Wolf"],
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.character_level= Widget(
            widget_type=QPushButton(),
            parent_layout=self.portrait_layout.inner_layout(2),
            stylesheet=style.BIG_BUTTONS,
            objectname="level",
            text="1",
            signal = lambda: character_xp.adjust_xp(self,adjust="add"),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        for number in range(1,4):
            self.feats = Widget(
                widget_type=QToolButton(),
                stylesheet=style.BUTTONS,
                parent_layout = self.feats_layout.inner_layout(1),
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                signal=self.open_features,
                #height=cons.WSIZE*1.25,
                width=cons.WSIZE*1.25,
                objectname=f"feat{number}",
                enabled=False,
            )

        for number in range(1,11):
            self.hero_dice = Widget(
                widget_type=QToolButton(),
                stylesheet=style.BUTTONS,
                checkable=True,
                parent_layout = self.herodice_layout.inner_layout(1),
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                #height=cons.WSIZE/1.25,
                signal=lambda: CharacterSheet(self).update_dictionary(),
                objectname=f"herodice{number}",
                enabled=False,
            )

        for number,stat in enumerate(["STR", "DEX", "INT", "CON", "WIS", "CHA"]):
            number = number + 2
            self.stat_label = Widget(
                widget_type=QPushButton(),
                stylesheet=style.QSTATS,
                text=stat,
                parent_layout = self.stat_layout.inner_layout(number),
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                height=cons.WSIZE,
                objectname="label",
                signal=functools.partial(
                    custom_rolls.roll_check,
                    self,
                    CombatLogGUI().get_widget_directory(),
                    stat,
                ),
            )
            self.stat_button = Widget(
                widget_type=QPushButton(),
                stylesheet=style.BIG_BUTTONS,
                text="0",
                parent_layout = self.stat_layout.inner_layout(number),
                signal=functools.partial(
                    character_stats.adjust_stat,
                    self,
                    stat,
                    adjust="add"
                ),
                objectname=stat,
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            )

        #INITIATIVE AND AC AND HP FEATS
        self.initiative_stat_label = Widget(
            widget_type=QPushButton(),
            text="0 Init",
            parent_layout = self.initiative_layout.inner_layout(1),
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname="initiative",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet=style.BUTTONS,
        )

        self.speed_stat_label = Widget(
            widget_type=QPushButton(),
            text="0 ft.",
            parent_layout = self.initiative_layout.inner_layout(1),
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname="movement",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet=style.BUTTONS,
        )

        self.character_ac = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            parent_layout=self.defense_layout.inner_layout(1),
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname = "ac",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.character_max_morale = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            parent_layout=self.morale_layout.inner_layout(1),
            text = "0",
            objectname = "max_morale",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.character_current_morale = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            parent_layout=self.morale_layout.inner_layout(1),
            signal=lambda: character_morale.adjust_morale(self, adjust="add"),
            text = "0",
            objectname = "current_morale",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
        )

        self.character_hp_max = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            parent_layout=self.hp_layout.inner_layout(1),
            signal=lambda: CharacterSheet(self).update_dictionary(),
            objectname = "max_hp",
            text = cons.HIT_DICE,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            #height=cons.WSIZE*1.5,
        )

        self.character_hp_current= Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            parent_layout=self.hp_layout.inner_layout(1),
            signal=self.open_addsub,
            objectname = "current_hp",
            text = "0",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            #height=cons.WSIZE*1.5,
        )

        # below you will find the widges that make up the inventory
        for count in range(1,cons.MAX_SLOTS+1):
            self.slot_layot = Section(
                outer_layout = QHBoxLayout(),
                inner_layout = ("VBox", 5),
                parent_layout=self.inventory_layout.inner_layout(1),
                content_margin=(0,0,8,0)
            )
            self.backpack= Widget(
                widget_type=QToolButton(),
                stylesheet=style.INVENTORY,
                text="",
                parent_layout=self.slot_layot.inner_layout(1),
                width = cons.WSIZE*1.50,
                height = cons.WSIZE,
                enabled=False,
                objectname=f"icon{count}",
                signal=functools.partial(func.double_roll,self,CombatLogGUI().get_widget_directory(),"Beasttoe",count),
            )

            self.backpack_label = Widget(
                widget_type=QLabel(),
                stylesheet=style.INVENTORY,
                parent_layout=self.slot_layot.inner_layout(1),
                height = cons.WSIZE/1.5,
                objectname=f"icon_label{count}",
                text=f"{count}.",
                align="center",
            )
                
            self.backpack_item = Widget(
                widget_type=QLineEdit(),
                stylesheet=style.INVENTORY,
                parent_layout=self.slot_layot.inner_layout(2),
                height = cons.WSIZE,
                signal= self.select_item,
                objectname=f"inventory{count}",
                align="center",
                enabled=False,

            )

            self.backpack_item_label = Widget(
                widget_type=QLabel(),
                stylesheet=style.INVENTORY,
                text="",
                parent_layout=self.slot_layot.inner_layout(2),
                enabled=False,
                height = cons.WSIZE/1.5,
                objectname=f"inventory_label{count}",
                align="center",
            )

            self.backpack_action= Widget(
                widget_type=QPushButton(),
                stylesheet=style.INVENTORY,
                text="",
                parent_layout=self.slot_layot.inner_layout(3),
                width = cons.WSIZE*3,
                height = cons.WSIZE,
                enabled=False,
                objectname=f"evoke{count}",
                signal=functools.partial(func.single_roll,self,CombatLogGUI().get_widget_directory(),"Beasttoe","evoke",count),
            )

            self.backpack_action_label = Widget(
                widget_type=QLabel(),
                stylesheet=style.INVENTORY,
                text="",
                parent_layout=self.slot_layot.inner_layout(3),
                enabled=False,
                height = cons.WSIZE/1.5,  
                objectname=f"evoke_label{count}",
                align="center",
            )

            self.backpack= Widget(
                widget_type=QPushButton(),
                stylesheet=style.INVENTORY,
                text="",
                parent_layout=self.slot_layot.inner_layout(4),
                width = cons.WSIZE*3,
                height = cons.WSIZE,
                enabled=False,
                objectname=f"hit_dc{count}",
                signal=functools.partial(func.single_roll,self,CombatLogGUI().get_widget_directory(),"Beasttoe","hit_dc",count),
            )

            self.backpack_hit_label = Widget(
                widget_type=QLabel(),
                stylesheet=style.INVENTORY,
                text="",
                parent_layout=self.slot_layot.inner_layout(4),
                enabled=False,
                height = cons.WSIZE/1.5,
                objectname=f"hit_dc_label{count}",
                align="center",
            )

            self.weapon_modifier = Widget(
                widget_type=QPushButton(),
                stylesheet=style.INVENTORY,
                parent_layout=self.slot_layot.inner_layout(5),
                width = cons.WSIZE*3,
                height = cons.WSIZE,
                objectname=f"roll{count}",
                enabled=False,
                signal = functools.partial(func.single_roll,self,CombatLogGUI().get_widget_directory(),"Beasttoe","roll",count)
            )

            self.backpack_damage_label = Widget(
                widget_type=QLabel(),
                stylesheet=style.INVENTORY,
                text="",
                parent_layout=self.slot_layot.inner_layout(5),
                enabled=False,
                height = cons.WSIZE/1.5,
                objectname=f"roll_label{count}",
                align="center",
            )

        for count in range(1,11):
            self.corruption_icon = Widget(
                widget_type=QToolButton(),
                stylesheet=style.BUTTONS,
                parent_layout=self.corruption_layout.inner_layout(1),
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                #height=cons.WSIZE/1.25,
                checkable=True,
                checked=False,	
                signal=lambda: CharacterSheet(self).update_dictionary(),
                objectname=f"corruption{count}",
                enabled=False,	
            )

        self.setLayout(self.character_sheet_layout.outer_layout())
    
    def mousePressEvent(self, event): #this is a very specific event used to subtract values when right clicking on a widget
        if event.button() == Qt.RightButton:
            widget = self.childAt(event.pos())
            if widget.objectName() in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
                print("Right button was clicked on a stat widget")
                character_stats.adjust_stat(self, widget.objectName(), adjust="subtract")
            elif widget.objectName() == "level":
                character_xp.adjust_xp(self,adjust="subtract")
            elif widget.objectName() == "current_morale":
                character_morale.adjust_morale(self, adjust="subtract")

            print("Right button was clicked") 

    def select_item(self):
        sender = self.sender()
        if sender.text().lower() in cons.SPELL_LISTS:
            print("found in list")
            self.spells = SpellsGUI(self, sender)
        else:
            CharacterSheet(self).update_dictionary()

    def open_features(self):
        sender = self.sender()
        self.features = FeatsGUI(sender)
        self.features.show()

    def open_addsub(self):
        sender = self.sender()
        self.addsub = AddSubGUI(self, sender)
        self.addsub.show()