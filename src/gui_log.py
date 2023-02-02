from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from pyside import Section
from pyside import Widget

from combat_log import CombatLog

import constants as cons
import functions as func
import functools
import stylesheet as style

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
            scroll=(True,"bottom"),
            title="COMBAT LOG",
            group = (True,None,None),   
            icon = ("combatlog.png",cons.WSIZE/2,cons.ICON_COLOR),	 	
        )

        self.log_latest = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.log_layout.inner_layout(0), 
            title="LAST ROLL",  
            group = (True,None,100), 
            icon = ("combatlog.png",cons.WSIZE/2,cons.ICON_COLOR)	
        )

        self.log_dice = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("HBox", 1),   
            parent_layout = self.log_layout.inner_layout(0),
            title="DICE",  
            group = (True,None,cons.WSIZE*2),
            icon = ("dice.png",cons.WSIZE/2,cons.ICON_COLOR),
            spacing = 3,	
        )

        #DICE
        #Small loop that create a widget class for each dice type.
        dice = [("%",100),("D4",4),("D6",6), ("D8",8), ("D10",10), ("D12",12), ("D20",20)]
        for die_type in dice:
            Widget(
                widget_type=QPushButton(),
                stylesheet=style.BUTTONS,
                parent_layout=self.log_dice.inner_layout(0),
                text=die_type[0],
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
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

    def get_widget_directory(self):
        # we create 20 blank entries in the log, and update the different widget. This is to reduce the interface popping and too many entries to be added to the interface.
        self.log_dictionary = {}
        for entry in range(20):
            entry_ui = self.create_log_entry(self.log_scroll.inner_layout(0))
            self.log_dictionary[entry] = {"character":entry_ui[0],"icon":entry_ui[1],"type":entry_ui[2],"name":entry_ui[3],"hit desc":entry_ui[4],"roll desc":entry_ui[5],"hit":entry_ui[6],"roll":entry_ui[7],"time":entry_ui[8]}#,"breakdown":entry_ui[9]
        l_entry_ui = self.create_log_entry(self.log_latest.inner_layout(0))
        self.log_dictionary[20] = {"character":l_entry_ui[0],"icon":l_entry_ui[1],"type":l_entry_ui[2],"name":l_entry_ui[3],"hit desc":l_entry_ui[4],"roll desc":l_entry_ui[5],"hit":l_entry_ui[6],"roll":l_entry_ui[7],"time":l_entry_ui[8]}#,"breakdown":l_entry_ui[9]
        return self.log_dictionary



    def create_log_entry(self, layout):
   
        # MAIN LOG LAYOUT
        self.single_log_layout = Section (
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 3),
            parent_layout = layout,
            spacing = 3,
            content_margin=(0,0,15,0)
        )    

        self.main_roll_layout = Section (
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 3),
            parent_layout = self.single_log_layout.inner_layout(2),
        )   

        self.label_roll_layout = Section (
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 2),
            parent_layout = self.main_roll_layout.inner_layout(2),
        ) 

        self.result_roll_layout = Section (
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 2),
            parent_layout = self.main_roll_layout.inner_layout(3),
        )  

        # LOG CONTENT
        self.log_character_name = Widget(
            widget_type = QLabel(),
            parent_layout = self.single_log_layout.inner_layout(1),
            stylesheet = style.COMBAT_LOG,
            objectname = "character"
        )

        self.log_character_icon = Widget(
            widget_type = QLabel(),
            parent_layout = self.main_roll_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet = style.COMBAT_LOG,
            width = cons.WSIZE*2.20,
            height = cons.WSIZE*2.20,
            objectname = "icon"
        )

        self.log_action_type = Widget(
            widget_type = QLabel(),
            parent_layout = self.label_roll_layout.inner_layout(1),
            stylesheet = style.COMBAT_LOG,
            height = cons.WSIZE*1.10,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            objectname = "label"
        )

        self.log_action_name = Widget(
            widget_type = QLabel(),
            parent_layout = self.label_roll_layout.inner_layout(2),
            stylesheet = style.COMBAT_LOG,
            height = cons.WSIZE*1.10,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            objectname = "label_sub"
        )

        self.description_hit_roll = Widget(
            widget_type = QLabel(),
            parent_layout = self.result_roll_layout.inner_layout(1),
            stylesheet = style.COMBAT_LOG,
            width = cons.WSIZE*3,
            height = cons.WSIZE*1.10,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            objectname = "hit_desc"
        )

        self.description_action_roll = Widget(
            widget_type = QLabel(),
            parent_layout = self.result_roll_layout.inner_layout(2),
            stylesheet = style.COMBAT_LOG,
            width = cons.WSIZE*3,
            height = cons.WSIZE*1.10,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            objectname = "roll_desc"
        )

        self.hit_roll = Widget(
            widget_type = QLabel(),
            parent_layout = self.result_roll_layout.inner_layout(1),
            enabled = False,
            height = cons.WSIZE*1.10,
            width = cons.WSIZE*2, 
            align="right",
            stylesheet = style.COMBAT_LOG,
            objectname = "hit"
        )

        self.action_roll = Widget(
            widget_type = QLabel(),
            parent_layout = self.result_roll_layout.inner_layout(2),
            enabled = False,
            height = cons.WSIZE*1.10,
            width = cons.WSIZE*2, 
            align="right",
            stylesheet = style.COMBAT_LOG,
            objectname = "roll"
        )

        self.log_entry_date = Widget(
            widget_type = QLabel(),
            parent_layout = self.single_log_layout.inner_layout(3),
            align="right",
            stylesheet = style.COMBAT_LOG,
            objectname = "date"
        )

        # self.log_roll_breakdown = Widget(
        #     widget_type = QLabel(),
        #     parent_layout = self.single_log_layout.inner_layout(3),
        #     stylesheet = style.COMBAT_LOG,
        #     align="right",
        #     objectname = "breakdown"
        # )

    
        self.log_action_type.get_widget().setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.log_action_name.get_widget().setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.description_hit_roll.get_widget().setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.description_action_roll.get_widget().setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.hit_roll.get_widget().setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.action_roll.get_widget().setAlignment(Qt.AlignVCenter | Qt.AlignCenter)


        return (
            self.log_character_name.get_widget(), 
            self.log_character_icon.get_widget(), 
            self.log_action_type.get_widget(), 
            self.log_action_name.get_widget(),
            self.description_hit_roll.get_widget(), 
            self.description_action_roll.get_widget(), 
            self.hit_roll.get_widget(), 
            self.action_roll.get_widget(),
            self.log_entry_date.get_widget(),
            # self.log_roll_breakdown.get_widget()
        )
        

