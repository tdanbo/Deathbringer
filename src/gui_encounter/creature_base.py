from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from pyside import Section
from pyside import Widget
from pyside import SimpleSection

import stylesheet as style
import constants as cons
import functions as func

import gui_encounter.encounter_style as estyle

class CreatureBase(QWidget):
    def __init__(self, creature_type, creature_rank):
        super().__init__()
        self.section_creatures_group = []
        self.widget_creatures_group = []

        print(self.section_creatures_group)
        print(self.widget_creatures_group)

        self.master_layout = QVBoxLayout()
        
        self.single_creature_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 4),
            class_group=self.section_creatures_group,
            parent_layout=self.master_layout,
            spacing=1,
            content_margin=(0,0,8,1),
        )   

        self.slot_layot = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 10),
            parent_layout=self.single_creature_layout.inner_layout(1),
            class_group=self.section_creatures_group,            
        ) 
        self.action_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout=self.single_creature_layout.inner_layout(2),
            class_group=self.section_creatures_group,
            spacing=1
        )

        self.bottom_label = Widget(
            widget_type=QLabel(),
            parent_layout=self.single_creature_layout.inner_layout(3),
            height = 6,
            objectname=f"bottom_label",
            class_group=self.widget_creatures_group,
        )
        
        if creature_rank != "Player":
            # self.top_label.get_widget().setStyleSheet(estyle.CREATURE_BOTTOM_LABEL)
            self.bottom_label.get_widget().setStyleSheet(estyle.CREATURE_BOTTOM_LABEL)
        else:
            # self.top_label.get_widget().setStyleSheet(estyle.PLAYER_BOTTOM_LABEL)
            self.bottom_label.get_widget().setStyleSheet(estyle.PLAYER_BOTTOM_LABEL)


        self.hp = Widget(
            widget_type=QPushButton(),
            parent_layout=self.slot_layot.inner_layout(1),
            width = cons.WSIZE*2,
            height = cons.WSIZE*2,
            objectname=f"hp",
            class_group=self.widget_creatures_group,
            stylesheet=estyle.BIG_BUTTONS,
        )

        self.hp_label = Widget(
            widget_type=QLabel(),
            parent_layout=self.slot_layot.inner_layout(1),
            height = cons.WSIZE/1.5,
            objectname=f"max hp",
            text="HP",
            align="center",
            class_group=self.widget_creatures_group,
            width = cons.WSIZE*2,
            stylesheet=estyle.SUB_LABEL
        )

        self.ac = Widget(
            widget_type=QPushButton(),
            parent_layout=self.slot_layot.inner_layout(2),
            width = cons.WSIZE*2,
            height = cons.WSIZE*2,
            objectname=f"ac",
            class_group=self.widget_creatures_group,
            stylesheet=estyle.BIG_BUTTONS,
        )

        self.ac_label = Widget(
            widget_type=QLabel(),
            parent_layout=self.slot_layot.inner_layout(2),
            height = cons.WSIZE/1.5,
            objectname=f"ac_label",
            text="AC",
            align="center",
            class_group=self.widget_creatures_group,
            width = cons.WSIZE*2,
            stylesheet=estyle.SUB_LABEL
        )

        self.passive = Widget(
            widget_type=QToolButton(),
            parent_layout=self.slot_layot.inner_layout(3),
            width = cons.WSIZE*2,
            height = cons.WSIZE*2,
            objectname=f"passive",
            class_group=self.widget_creatures_group,
            stylesheet=estyle.BIG_BUTTONS        
        )

        self.passive_label = Widget(
            widget_type=QLabel(),
            parent_layout=self.slot_layot.inner_layout(3),
            height = cons.WSIZE/1.5,
            objectname=f"passive_label",
            text="",
            align="center",
            class_group=self.widget_creatures_group,
            width = cons.WSIZE*2,
            stylesheet=estyle.SUB_LABEL
        )

        self.creature_type = Widget(
            widget_type=QLineEdit(),
            parent_layout=self.slot_layot.inner_layout(4),
            height = cons.WSIZE*2,
            #signal= self.select_item,
            objectname=f"{creature_type}",
            align="center",
            class_group=self.widget_creatures_group,
            text=f"{creature_type}",
            stylesheet=estyle.MAIN_LINE_EDIT
        )

        self.rank = Widget(
            widget_type=QLabel(),
            text=creature_rank,
            parent_layout=self.slot_layot.inner_layout(4),
            height = cons.WSIZE/1.5,
            objectname=f"rank",
            align="center",
            class_group=self.widget_creatures_group,
            stylesheet=estyle.SUB_LABEL,
        )

        for number, stat in enumerate(["STR", "DEX", "CON", "INT", "WIS", "CHA"]):
            self.stat = Widget(
                widget_type=QPushButton(),
                parent_layout=self.slot_layot.inner_layout(number+5),
                width = cons.WSIZE*1.40,
                height = cons.WSIZE*2,
                objectname=f"{stat}",
                #signal = functools.partial(roll.inventory_prepare_roll, self, "roll", position),
                class_group=self.widget_creatures_group,
                text="",
                stylesheet=estyle.STAT_LABEL,

            )

            self.stat_label = Widget(
                widget_type=QLabel(),
                text=stat,
                parent_layout=self.slot_layot.inner_layout(number+5),
                height = cons.WSIZE/1.5,
                objectname=f"stat_label",
                align="center",
                class_group=self.widget_creatures_group,
                stylesheet=estyle.STAT_LABEL
            )

        for s in self.section_creatures_group:
            s.connect_to_parent()

        for w in self.widget_creatures_group:
            w.connect_to_parent()
            w.set_signal()

        self.master_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.master_layout)
    
    def get_name(self):
        return self.creature_type.get_widget().text()
    
    def get_action_layout(self):
        return self.action_layout.inner_layout(1)
    
    def set_creature_stats(self,dict):
        self.dict = dict
        self.hp.get_widget().setText(str(dict["current hp"]))
        self.ac.get_widget().setText(str(dict["ac"]))
        # self.speed_label.get_widget().setText(str(dict["speed"]))

        self.rank.get_widget().setText(str(dict["rank"]))

        if "passive" in dict:
            if dict["passive"] != "":
                print(dict["passive"])
                self.passive_label.get_widget().setText("MOD")
            print(f'{dict["passive"]}.png')
            func.set_icon(self.passive.get_widget(),f'{dict["passive"]}.png',cons.ICON_COLOR)
            

        for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
            stat_button = self.findChild(QPushButton, stat)
            stat_value = dict["stats"][stat]
            stat_button.setText(str(stat_value))

    def get_init(self):
        return int(self.dict["init"])