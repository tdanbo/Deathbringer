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

from gui_functions import custom_rolls

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
            signal = lambda: custom_rolls.roll_dice(self, self.get_widget_directory())
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
                
        self.setLayout(self.log_layout.outer_layout())        

    def get_widget_directory(self):
        # we create 20 blank entries in the log, and update the different widget. This is to reduce the interface popping and too many entries to be added to the interface.
        self.log_dictionary = {}
        for entry in range(20):
            entry_ui = self.create_log_entry(self.log_scroll.inner_layout(0),entry)
            self.log_dictionary[entry] = {"character":entry_ui[0],"icon":entry_ui[1],"type":entry_ui[2],"name":entry_ui[3],"hit desc":entry_ui[4],"roll desc":entry_ui[5],"hit":entry_ui[6],"roll":entry_ui[7],"time":entry_ui[8]}#,"breakdown":entry_ui[9]
        l_entry_ui = self.create_log_entry(self.log_latest.inner_layout(0),20)
        self.log_dictionary[20] = {"character":l_entry_ui[0],"icon":l_entry_ui[1],"type":l_entry_ui[2],"name":l_entry_ui[3],"hit desc":l_entry_ui[4],"roll desc":l_entry_ui[5],"hit":l_entry_ui[6],"roll":l_entry_ui[7],"time":l_entry_ui[8]}#,"breakdown":l_entry_ui[9]
        return self.log_dictionary



    def create_log_entry(self, layout, slot):
   
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
            widget_type = QPushButton(),
            parent_layout = self.result_roll_layout.inner_layout(1),
            height = cons.WSIZE*1.10,
            width = cons.WSIZE*2, 
            stylesheet = style.COMBAT_BUTTON_1,
            objectname=f"hit{slot}",
            signal=lambda: custom_rolls.dice_reroll(self, self.get_widget_directory(), slot)
        )

        self.action_roll = Widget(
            widget_type = QPushButton(),
            parent_layout = self.result_roll_layout.inner_layout(2),
            height = cons.WSIZE*1.10,
            width = cons.WSIZE*2, 
            stylesheet = style.COMBAT_BUTTON_2,
            objectname=f"roll{slot}",
            signal=lambda: custom_rolls.dice_reroll(self, self.get_widget_directory(), slot)
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
        
    def mousePressEvent(self, event): #this is a very specific event used to subtract values when right clicking on a widget
        if event.button() == Qt.RightButton:
            widget = self.childAt(event.pos())
            if widget.objectName() in ["d4","d6","d8","d10","d12","d20","MOD","d4_count","d6_count","d8_count","d10_count","d12_count","d20_count","MOD_count"]:
                print("Right button was clicked on a stat widget")
                custom_rolls.add_dice(self, widget.objectName(), adjust="subtract")
            elif widget.objectName() == "roll":
                custom_rolls.clear_rolls(self)


