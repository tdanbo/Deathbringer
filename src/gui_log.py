from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from my_pyside import Section
from my_pyside import Widget

from combat_log import CombatLog

import constants as cons
import functions as func
import functools

class CombatLogGUI(QWidget):
    def __init__(self):
        super().__init__()
        #Setting up layouts/sections
        self.log_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            spacing = 10,   
        )

        self.log_scroll = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.log_layout.inner_layout(0),
            scroll=True,
            group=True,
            title="COMBAT LOG",
            icon = ("combatlog.png",cons.WSIZE/2,cons.ICON_COLOR)	 	
        )

        self.log_latest = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.log_layout.inner_layout(0), 
            group=True,   
        )

        self.log_dice = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("HBox", 1),   
            parent_layout = self.log_layout.inner_layout(0),
            title="DICE",  
            group=True,
            icon = ("dice.png",cons.WSIZE/2,cons.ICON_COLOR)	
        )

        #DICE
        #Small loop that create a widget class for each dice type.
        dice = [("%",100),("D4",4),("D6",6), ("D8",8), ("D10",10), ("D12",12), ("D20",20)]
        for die_type in dice:
            Widget(
                widget_type=QPushButton(),
                parent_layout=self.log_dice.inner_layout(0),
                height=cons.WSIZE/1.25,
                text=die_type[0],
                signal=functools.partial(
                    func.roll_dice,
                    dictionary = self.get_widget_directory, 
                    die=die_type[1],
                    modifier=0,
                    roll_type="Custom", 
                    roll_breakdown=die_type[0],
                    character="Beasttoe"
                ),
            )       

        self.setLayout(self.log_layout.outer_layout())

    def update_log(self,die=0, modifier=0, character="Dungeon Master"):
        roll = func.roll_dice(die) + modifier
        print(f"Roll: {roll}")
        print(f"Modifier: {modifier}")
        print(f"character: {character}")
        CombatLog(self.get_widget_directory()).set_entry(character,roll)

    def get_widget_directory(self):
        # we create 20 blank entries in the log, and update the different widget. This is to reduce the interface popping and too many entries to be added to the interface.
        self.log_dictionary = {}
        for entry in range(20):
            entry_ui = self.create_log_entry(self.log_scroll.inner_layout(0))
            self.log_dictionary[entry] = {"character":entry_ui[0],"icon":entry_ui[1],"type":entry_ui[2],"breakdown":entry_ui[3],"roll":entry_ui[4],"time":entry_ui[5]}
        latest_entry_ui = self.create_log_entry(self.log_latest.inner_layout(0))
        self.log_dictionary[20] = {"character":latest_entry_ui[0],"icon":latest_entry_ui[1],"type":latest_entry_ui[2],"breakdown":latest_entry_ui[3],"roll":latest_entry_ui[4],"time":latest_entry_ui[5]}
        return self.log_dictionary



    def create_log_entry(self, layout):
        # MAIN LOG LAYOUT
        self.single_log_layout = Section (
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 3),
            parent_layout = layout,
        )       

        roll_type = {"Custom":"#bd4f00", "Attack":"#bd0000", "Defend":"#0062bd"}

        name_stylesheet = "font-size: 12px; font-weight: bold; color: hsl(0%, 0%, 50%)"
        icon_stylesheet = "background-color: hsl(0%, 0%, 80%);"
        type_stylesheet = f"font-size: 12px; font-weight: bold; background-color: hsl(0%, 0%, 80%); color: hsl(0%, 0%, 20%); border: 0px;"
        breakdown_stylesheet = "font-size: 10px; color: hsl(0%, 0%, 30%)"
        roll_stylesheet = "font-size: 20px; font-weight: bold; background-color: hsl(0%, 0%, 80%); color: hsl(0%, 0%, 10%); border: 0px; border-top-right-radius: 8px; border-bottom-right-radius: 8px;"
        date_stylesheet = "font-size: 10px; color: hsl(0%, 0%, 30%)"

        # LOG CONTENT
        self.log_character_name = Widget(
            widget_type = QLabel(),
            parent_layout = self.single_log_layout.inner_layout(1),
            stylesheet = name_stylesheet,
        )

        self.log_character_icon = Widget(
            widget_type = QToolButton(),
            parent_layout = self.single_log_layout.inner_layout(2),
            height = cons.WSIZE*1.50,
            width = cons.WSIZE*1.50,
            stylesheet = icon_stylesheet,
        )

        self.log_roll_type = Widget(
            widget_type = QLineEdit(),
            parent_layout = self.single_log_layout.inner_layout(2),
            stylesheet = type_stylesheet,
            align="right",
            height = cons.WSIZE*1.50,
            width = cons.WSIZE*2.5, 
        )

        self.log_roll = Widget(
            widget_type = QLineEdit(),
            parent_layout = self.single_log_layout.inner_layout(2),
            enabled = False,
            height = cons.WSIZE*1.50,
            align="right",
            stylesheet = roll_stylesheet,
        )

        self.log_entry_date = Widget(
            widget_type = QLabel(),
            parent_layout = self.single_log_layout.inner_layout(3),
            align="left",
            stylesheet = date_stylesheet,
        )

        self.log_roll_breakdown = Widget(
            widget_type = QLabel(),
            parent_layout = self.single_log_layout.inner_layout(3),
            stylesheet = breakdown_stylesheet,
            align="right",
        )

        return (
            self.log_character_name.get_widget(), 
            self.log_character_icon.get_widget(), 
            self.log_roll_type.get_widget(), 
            self.log_roll_breakdown.get_widget(), 
            self.log_roll.get_widget(), 
            self.log_entry_date.get_widget()
        )