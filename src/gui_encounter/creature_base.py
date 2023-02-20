from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from pyside import Section
from pyside import Widget
from pyside import SimpleSection

import stylesheet as style
import constants as cons

class CreatureBase(QWidget):
    def __init__(self, creature_type):
        super().__init__()
        self.section_creatures_group = []
        self.widget_creatures_group = []

        print(self.section_creatures_group)
        print(self.widget_creatures_group)

        self.master_layout = QVBoxLayout()
        
        self.single_creature_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 1),
            class_group=self.section_creatures_group,
            parent_layout=self.master_layout,
        )   

        self.slot_layot = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 11),
            parent_layout=self.single_creature_layout.inner_layout(1),
            class_group=self.section_creatures_group,
            content_margin=(0,0,8,1)
        ) 
        self.action_layout = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout=self.single_creature_layout.inner_layout(1),
            class_group=self.section_creatures_group
        )   
        self.hp = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            parent_layout=self.slot_layot.inner_layout(1),
            width = cons.WSIZE*2,
            height = cons.WSIZE*2,
            objectname=f"hp",
            class_group=self.widget_creatures_group,
        )

        self.hp_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(1),
            height = cons.WSIZE/1.5,
            objectname=f"max hp",
            text="HP",
            align="center",
            class_group=self.widget_creatures_group,
            width = cons.WSIZE*2
        )

        self.ac = Widget(
            widget_type=QPushButton(),
            stylesheet=style.BIG_BUTTONS,
            parent_layout=self.slot_layot.inner_layout(2),
            width = cons.WSIZE*2,
            height = cons.WSIZE*2,
            objectname=f"ac",
            class_group=self.widget_creatures_group,
        )

        self.ac_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(2),
            height = cons.WSIZE/1.5,
            objectname=f"ac_label",
            text="AC",
            align="center",
            class_group=self.widget_creatures_group,
            width = cons.WSIZE*2
        )

        self.passive = Widget(
            widget_type=QToolButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(3),
            width = cons.WSIZE*2,
            height = cons.WSIZE*2,
            objectname=f"passive",
            class_group=self.widget_creatures_group,
        )

        self.passive_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(3),
            height = cons.WSIZE/1.5,
            objectname=f"passive_label",
            text="MOD",
            align="center",
            class_group=self.widget_creatures_group,
            width = cons.WSIZE*2
        )

        self.icon = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(4),
            width = cons.WSIZE*5,
            height = cons.WSIZE*2,
            objectname=f"icon",
            class_group=self.widget_creatures_group,
            icon=(f"{creature_type}.png","","",100),
        )

        self.speed_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(4),
            height = cons.WSIZE/1.5,
            objectname=f"speed",
            text="",
            align="center",
            class_group=self.widget_creatures_group,
            width = cons.WSIZE*5,
        )

        self.creature_type = Widget(
            widget_type=QLineEdit(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(5),
            height = cons.WSIZE*2,
            #signal= self.select_item,
            objectname=f"{creature_type}",
            align="center",
            class_group=self.widget_creatures_group,
            text=f"{creature_type}"

        )

        self.initiative = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            text="",
            parent_layout=self.slot_layot.inner_layout(5),
            height = cons.WSIZE/1.5,
            objectname=f"init",
            align="center",
            class_group=self.widget_creatures_group
        )

        for number, stat in enumerate(["STR", "DEX", "CON", "INT", "WIS", "CHA"]):
            self.stat = Widget(
                widget_type=QPushButton(),
                stylesheet=style.INVENTORY,
                parent_layout=self.slot_layot.inner_layout(number+6),
                width = cons.WSIZE*1.40,
                height = cons.WSIZE*2,
                objectname=f"{stat}",
                #signal = functools.partial(roll.inventory_prepare_roll, self, "roll", position),
                class_group=self.widget_creatures_group,
                text="",

            )

            self.stat_label = Widget(
                widget_type=QLabel(),
                stylesheet=style.INVENTORY,
                text=stat,
                parent_layout=self.slot_layot.inner_layout(number+6),
                height = cons.WSIZE/1.5,
                objectname=f"stat_label",
                align="center",
                class_group=self.widget_creatures_group
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
        self.hp.get_widget().setText(str(dict["current hp"]))
        self.ac.get_widget().setText(str(dict["ac"]))
        self.speed_label.get_widget().setText(str(dict["speed"]))
        self.initiative.get_widget().setText(str(dict["init"]))
        for stat in ["STR", "DEX", "CON", "INT", "WIS", "CHA"]:
            stat_button = self.findChild(QPushButton, stat)
            stat_value = dict["stats"][stat]
            stat_button.setText(str(stat_value))

    def get_init(self):
        return int(self.initiative.get_widget().text())