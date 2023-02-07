from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from pyside import Section
from pyside import Widget

import constants as cons
import functions as func
import functools
import stylesheet as style

from gui_functions import custom_rolls
from gui_functions import custom_log
from gui_functions import roll

class CombatLogGUI(QWidget):
    def __init__(self):
        super().__init__()
        #Setting up layouts/sections
        self.log_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 3),
            spacing = 10, 

        )

        self.log_scroll = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.log_layout.inner_layout(1),
            scroll=(True,"bottom"),
            title="COMBAT LOG",
            group = (True,None,None),   
            icon = ("combatlog.png",cons.WSIZE/2,cons.ICON_COLOR),	 	
        )

        self.log_latest = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.log_layout.inner_layout(2), 
            title="LAST ROLL",  
            group = (True,None,110), 
            icon = ("combatlog.png",cons.WSIZE/2,cons.ICON_COLOR)	
        )

        self.log_dice = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("HBox", 2),   
            parent_layout = self.log_layout.inner_layout(3),
            title="DICE",  
            group = (True,None,cons.WSIZE*2.2),
            icon = ("dice.png",cons.WSIZE/2,cons.ICON_COLOR),
            spacing = 3,	
        )

        self.roll_button = Widget(
            widget_type=QPushButton(),
            parent_layout=self.log_dice.get_title()[2],
            text="ROLL",
            stylesheet=style.QTITLE,
            height=cons.WSIZE,
            objectname="roll",
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            signal= lambda: roll.custom_prepare_roll(self,"Custom")
        )   

        self.roll_button.get_widget().setHidden(True)

        #DICE
        #Small loop that create a widget class for each dice type.
        dice = [("d4",4),("d6",6), ("d8",8), ("d10",10), ("d12",12), ("d20",20), ("MOD",0)]
        for die_type in dice:
            self.dice_layout = Section(
                outer_layout = QHBoxLayout(),
                inner_layout = ("HBox", 1),
                parent_layout = self.log_dice.inner_layout(0),
                spacing=0,
                
            )

            self.dice_count = Widget(
                widget_type=QPushButton(),
                parent_layout=self.dice_layout.inner_layout(0),
                text="",
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                stylesheet=style.DICE_TRAY2,
                objectname=f"{die_type[0]}_count",
                signal=functools.partial(
                    custom_rolls.add_dice,
                    self,
                    die_type[0],
                ),
            )   

            self.dice_w = Widget(
                widget_type=QPushButton(),
                parent_layout=self.dice_layout.inner_layout(0),
                text=die_type[0],
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                stylesheet=style.DICE_TRAY,
                objectname=die_type[0],
                signal=functools.partial(
                    custom_rolls.add_dice,
                    self,
                    die_type[0]
                ),
            )       

            self.dice_count.get_widget().setMinimumWidth(cons.WSIZE*1.5)
            self.dice_w.get_widget().setMinimumWidth(cons.WSIZE*1.5)
            self.dice_count.get_widget().setHidden(True)

        #Setting up all slots for the combat log
        for slot in range(20, -1, -1):
            print(slot)
            self.create_log_entry(slot)

        self.setLayout(self.log_layout.outer_layout())        

    def create_log_entry(self, slot):
        if slot == 0:
            layout = self.log_latest.inner_layout(0)
        else:
            layout = self.log_scroll.inner_layout(0)

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
        self.log_character = Widget(
            widget_type = QLabel(),
            parent_layout = self.single_log_layout.inner_layout(1),
            stylesheet = style.COMBAT_LOG,
            objectname = f"character{slot}"
        )

        self.log_icon = Widget(
            widget_type = QLabel(),
            parent_layout = self.main_roll_layout.inner_layout(1),
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            stylesheet = style.COMBAT_LOG,
            width = cons.WSIZE*2.20,
            height = cons.WSIZE*2.20,
            objectname = f"icon{slot}"
        )

        self.log_action_name = Widget(
            widget_type = QLabel(),
            parent_layout = self.label_roll_layout.inner_layout(1),
            stylesheet = style.COMBAT_LOG,
            height = cons.WSIZE*1.10,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            objectname = f"action name{slot}"
        )

        self.log_action_dice = Widget(
            widget_type = QLabel(),
            parent_layout = self.label_roll_layout.inner_layout(2),
            stylesheet = style.COMBAT_LOG,
            height = cons.WSIZE*1.10,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            objectname = f"action dice{slot}"
        )

        self.second_hit = Widget(
            widget_type = QLabel(),
            parent_layout = self.result_roll_layout.inner_layout(1),
            height = cons.WSIZE*1.10,
            width = cons.WSIZE*1.75, 
            stylesheet = style.COMBAT_BUTTON_1_REROLL,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            objectname=f"second hit{slot}",
        )

        self.desc_hit = Widget(
            widget_type = QPushButton(),
            parent_layout = self.result_roll_layout.inner_layout(1),
            stylesheet = style.COMBAT_LOG,
            width = cons.WSIZE*2.5,
            height = cons.WSIZE*1.10,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            objectname = f"desc hit{slot}",
            signal= functools.partial(custom_log.show_reroll, self, "hit", slot)
        )

        self.first_hit = Widget(
            widget_type = QLabel(),
            parent_layout = self.result_roll_layout.inner_layout(1),
            height = cons.WSIZE*1.10,
            width = cons.WSIZE*1.75, 
            stylesheet = style.COMBAT_BUTTON_1,
            objectname=f"first hit{slot}",
        )

        self.second_roll = Widget(
            widget_type = QLabel(),
            parent_layout = self.result_roll_layout.inner_layout(2),
            height = cons.WSIZE*1.10,
            width = cons.WSIZE*1.75, 
            stylesheet = style.COMBAT_BUTTON_2_REROLL,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            objectname=f"second roll{slot}",
        )

        self.desc_roll = Widget(
            widget_type = QPushButton(),
            parent_layout = self.result_roll_layout.inner_layout(2),
            stylesheet = style.COMBAT_LOG,
            width = cons.WSIZE*2.5,
            height = cons.WSIZE*1.10,
            size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
            objectname = f"desc roll{slot}",
            signal= functools.partial(custom_log.show_reroll, self, "roll", slot)
        )

        self.first_roll = Widget(
            widget_type = QLabel(),
            parent_layout = self.result_roll_layout.inner_layout(2),
            height = cons.WSIZE*1.10,
            width = cons.WSIZE*1.75, 
            stylesheet = style.COMBAT_BUTTON_2,
            objectname=f"first roll{slot}",
        )

        self.time = Widget(
            widget_type = QLabel(),
            parent_layout = self.single_log_layout.inner_layout(3),
            align="right",
            stylesheet = style.COMBAT_LOG,
            objectname = f"time{slot}"
        )
    
        self.log_action_name.get_widget().setAlignment(Qt.AlignVCenter | Qt.AlignLeft)
        self.log_action_dice.get_widget().setAlignment(Qt.AlignVCenter | Qt.AlignLeft)

        self.second_hit.get_widget().setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.second_roll.get_widget().setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.first_hit.get_widget().setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        self.first_roll.get_widget().setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        
    def mousePressEvent(self, event): #this is a very specific event used to subtract values when right clicking on a widget
        if event.button() == Qt.RightButton:
            widget = self.childAt(event.pos())
            if widget.objectName() in ["d4","d6","d8","d10","d12","d20","MOD","d4_count","d6_count","d8_count","d10_count","d12_count","d20_count","MOD_count"]:
                print("Right button was clicked on a stat widget")
                custom_rolls.add_dice(self, widget.objectName(), adjust="subtract")
            elif widget.objectName() == "roll":
                custom_rolls.clear_rolls(self)


