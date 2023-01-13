from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from my_pyside import Section
from my_pyside import Widget

from combat_log import CombatLog

import constants as cons
import functions as func
import functools

class CombatLogGUI:
    def __init__(self):

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
            group=True,  
        )

        #DICE
        #Small loop that create a widget class for each dice type.
        dice = [("%",100),("D4",4),("D6",6), ("D8",8), ("D10",10), ("D12",12), ("D20",20)]
        for die in dice:
            Widget(
                widget_type=QPushButton(),
                parent_layout=self.log_dice.inner_layout(0),
                text=die[0],
                height=cons.WSIZE,
                signal=functools.partial(self.update_log, die[1]),
            )
            
    def update_log(self,die=0, modifier=0, character="Dungeon Master"):
        roll = func.roll_dice(die) + modifier
        print(f"Roll: {roll}")
        print(f"Modifier: {modifier}")
        print(f"character: {character}")
        CombatLog(self.get_widget_directory()).set_entry(character,roll)

    def get_widget_directory(self):
        # we create 10 entries in the log, and update the different widget. This is to reduce the interface popping and too many entries to be added to the interface.
        self.log_dictionary = {}
        for entry in range(20):
            entry_ui = self.create_log_entry(self.log_scroll.inner_layout(0))
            self.log_dictionary[entry] = {"character":entry_ui[0],"icon":entry_ui[1],"type":entry_ui[2],"roll":entry_ui[3],"time":entry_ui[4]}
        latest_entry_ui = self.create_log_entry(self.log_latest.inner_layout(0))
        self.log_dictionary[20] = {"character":latest_entry_ui[0],"icon":latest_entry_ui[1],"type":latest_entry_ui[2],"roll":latest_entry_ui[3],"time":latest_entry_ui[4]}
        return self.log_dictionary



    def create_log_entry(self, layout):
        # MAIN LOG LAYOUT

        self.single_log_layout = Section (
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 3),
            parent_layout = layout,
            # spacing = 2
        )       

        name_stylesheet = "font-size: 12px; font-weight: bold; color: hsl(0%, 0%, 50%)"
        icon_stylesheet = "background-color: hsl(0%, 0%, 80%);"
        type_stylesheet = "font-size: 12px; font-weight: bold; background-color: hsl(0%, 0%, 80%); color: hsl(0%, 0%, 20%); border: 0px;"
        roll_stylesheet = "font-size: 20px; font-weight: bold; background-color: hsl(0%, 0%, 80%); color: hsl(0%, 0%, 10%); border: 0px; border-top-right-radius: 8px; border-bottom-right-radius: 8px;"
        date_stylesheet = "font-size: 10px; color: hsl(0%, 0%, 30%)"

        # LOG CONTENT
        self.log_character_name = Widget(
            widget_type = QLabel(),
            parent_layout = self.single_log_layout.inner_layout(0),
            stylesheet = name_stylesheet,
        )

        self.log_character_icon = Widget(
            widget_type = QToolButton(),
            parent_layout = self.single_log_layout.inner_layout(1),
            height = 40,
            width = 40,
            stylesheet = icon_stylesheet,
        )

        self.log_roll_type = Widget(
            widget_type = QLineEdit(),
            parent_layout = self.single_log_layout.inner_layout(1),
            stylesheet = type_stylesheet,
            align="left",
            height = 40,
        )

        self.log_roll = Widget(
            widget_type = QLineEdit(),
            parent_layout = self.single_log_layout.inner_layout(1),
            enabled = False,
            height = 40,
            width = 40,
            align="center",
            stylesheet = roll_stylesheet,
        )

        self.log_entry_date = Widget(
            widget_type = QLabel(),
            parent_layout = self.single_log_layout.inner_layout(2),
            align="right",
            stylesheet = date_stylesheet,
        )

        return (
            self.log_character_name.get_widget(), 
            self.log_character_icon.get_widget(), 
            self.log_roll_type.get_widget(), 
            self.log_roll.get_widget(), 
            self.log_entry_date.get_widget()
        )

    def get_main_layout(self):
        return self.log_layout.outer_layout()