from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from pyside import Section
from pyside import Widget
from pyside import SimpleSection

import stylesheet as style
import constants as cons

class CreatureAction(QWidget):
    def __init__(self, attack, action):
        super().__init__()

        if len(action["Modifiers"]) == 0:
            modifier1icon = ""
            modifier2icon = ""
        if len(action["Modifiers"]) == 1:
            modifier1icon = f'{action["Modifiers"][0]}.png'
            modifier2icon = ""
        if len(action["Modifiers"]) == 2:
            modifier1icon = f'{action["Modifiers"][0]}.png'
            modifier2icon = f'{action["Modifiers"][1]}.png'

        self.action_sections = []
        self.action_widgets = []

        self.master_layout = QVBoxLayout()

        self.slot_layot = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 8),
            parent_layout=self.master_layout,
            class_group=self.action_sections
        )

        self.backpack= Widget(
            widget_type=QToolButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(1),
            width = cons.WSIZE*2,
            height = cons.WSIZE,
            objectname=f"icon",
            #signal=functools.partial(roll.inventory_prepare_double_roll, self,position),
            class_group=self.action_widgets,
            icon=("weapon.png",cons.WSIZE*1.5,cons.ICON_COLOR),
        )

        self.backpack_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(1),
            height = cons.WSIZE/1.5,
            objectname=f"icon_label",
            text=f"{attack+1}.",
            align="center",
            class_group=self.action_widgets,
            width = cons.WSIZE*2
        )

        self.first_mod= Widget(
            widget_type=QToolButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(2),
            width = cons.WSIZE*2,
            height = cons.WSIZE,
            objectname=f"first_mod",
            #signal=functools.partial(roll.inventory_prepare_double_roll, self,position),
            class_group=self.action_widgets,
            icon=(modifier1icon,cons.WSIZE*1.5,cons.ICON_COLOR),
        )

        self.first_mod_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(2),
            height = cons.WSIZE/1.5,
            objectname=f"first_mod_label",
            text="",
            align="center",
            class_group=self.action_widgets,
            width = cons.WSIZE*2
        )

        self.second_mod= Widget(
            widget_type=QToolButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(3),
            width = cons.WSIZE*2,
            height = cons.WSIZE,
            objectname=f"icon",
            #signal=functools.partial(roll.inventory_prepare_double_roll, self,position),
            class_group=self.action_widgets,
            icon=(modifier2icon,cons.WSIZE*1.5,cons.ICON_COLOR),
        )

        self.second_mod_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(3),
            height = cons.WSIZE/1.5,
            objectname=f"icon_label",
            text="",
            align="center",
            class_group=self.action_widgets,
            width = cons.WSIZE*2
        )

        self.spacer = Widget(
            widget_type=QPushButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(4),
            width = 60,
            height = cons.WSIZE,
            objectname=f"spacer",
            class_group=self.action_widgets,	
        )

        self.spacer_label = Widget(
            widget_type=QPushButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(4),
            height = cons.WSIZE/1.5,
            objectname=f"spacer_label",
            class_group=self.action_widgets,
            width = 60,
        )

        self.backpack_item = Widget(
            widget_type=QLineEdit(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(5),
            height = cons.WSIZE,
            #signal= self.select_item,
            objectname=f"inventory",
            align="center",
            class_group=self.action_widgets,
            text="Claw"

        )

        self.backpack_item_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            text="Creature Attack",
            parent_layout=self.slot_layot.inner_layout(5),
            height = cons.WSIZE/1.5,
            objectname=f"inventory_label",
            align="center",
            class_group=self.action_widgets
        )

        self.backpack_action= Widget(
            widget_type=QPushButton(),
            stylesheet=style.INVENTORY,
            text="21",
            parent_layout=self.slot_layot.inner_layout(6),
            width = cons.WSIZE*3,
            height = cons.WSIZE,
            objectname=f"evoke",
            #signal = functools.partial(roll.inventory_prepare_roll, self, "evoke", position),
            class_group=self.action_widgets
        )

        self.defense_label = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            text="Defense",
            parent_layout=self.slot_layot.inner_layout(6),
            height = cons.WSIZE/1.5,  
            objectname=f"evoke_label",
            align="center",
            class_group=self.action_widgets
        )

        self.secondary_damage= Widget(
            widget_type=QPushButton(),
            stylesheet=style.INVENTORY,
            text=f'{action["Secondary Damage"]}',
            parent_layout=self.slot_layot.inner_layout(7),
            width = cons.WSIZE*3,
            height = cons.WSIZE,
            objectname=f"hit_dc",
            #signal = functools.partial(roll.inventory_prepare_roll, self, "hit_dc", position),
            class_group=self.action_widgets
        )

        self.secondary_type = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            text=f'{action["Secondary Type"]}',
            parent_layout=self.slot_layot.inner_layout(7),
            height = cons.WSIZE/1.5,
            objectname=f"hit_dc_label",
            align="center",
            class_group=self.action_widgets
        )

        self.primary_damage = Widget(
            widget_type=QPushButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(8),
            width = cons.WSIZE*3,
            height = cons.WSIZE,
            objectname=f"roll",
            #signal = functools.partial(roll.inventory_prepare_roll, self, "roll", position),
            class_group=self.action_widgets,
            text=f'{action["Primary Damage"]}',

        )

        self.primary_type = Widget(
            widget_type=QLabel(),
            stylesheet=style.INVENTORY,
            text=f'{action["Primary Type"]}',
            parent_layout=self.slot_layot.inner_layout(8),
            height = cons.WSIZE/1.5,
            objectname=f"roll_label",
            align="center",
            class_group=self.action_widgets
        )

        for s in self.action_sections:
            s.connect_to_parent()

        for w in self.action_widgets:
            w.connect_to_parent()
            w.set_signal()

        self.master_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.master_layout)