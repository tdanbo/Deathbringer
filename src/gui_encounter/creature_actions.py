from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from pyside import Section
from pyside import Widget
from pyside import SimpleSection

import stylesheet as style
import constants as cons

import gui_encounter.encounter_style as estyle

class CreatureAction(QWidget):
    def __init__(self, attack, action, total_attacks):
        super().__init__()
        print(action["Modifiers"])
        print(len(action["Modifiers"]))
        if len(action["Modifiers"]) == 0:
            modifier1icon = ""
            modifier2icon = ""
            mod1_text = ""
            mod2_text = ""
        if len(action["Modifiers"]) == 1:
            modifier1icon = f'{action["Modifiers"][0]}.png'
            modifier2icon = ""
            mod1_text = "MOD"
            mod2_text = ""
        if len(action["Modifiers"]) == 2:
            modifier1icon = f'{action["Modifiers"][0]}.png'
            modifier2icon = f'{action["Modifiers"][1]}.png'
            mod1_text = "MOD"
            mod2_text = "MOD"

        self.action_sections = []
        self.action_widgets = []

        self.master_layout = QHBoxLayout()

        self.slot_layot = Section(
            outer_layout = QHBoxLayout(),
            inner_layout = ("VBox", 8),
            parent_layout=self.master_layout,
            class_group=self.action_sections,

        )

        if total_attacks == 1:
            attack_times = "x1"
        elif total_attacks == 2:
            if attack == 0:
                attack_times = "x1"
            elif attack == 1:
                attack_times = "x1"
        elif total_attacks == 3:
            if attack == 0:
                attack_times = "x2"
            elif attack == 1:
                attack_times = "x1"



        self.backpack= Widget(
            widget_type=QPushButton(),
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
            stylesheet=estyle.SUB_LABEL,
            parent_layout=self.slot_layot.inner_layout(1),
            height = cons.WSIZE/1.5,
            objectname=f"icon_label",
            text=attack_times,
            class_group=self.action_widgets,
            width = cons.WSIZE*2,
            align="center"
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

        self.first_label = Widget(
            widget_type=QLabel(),
            stylesheet=estyle.SUB_LABEL,
            parent_layout=self.slot_layot.inner_layout(2),
            height = cons.WSIZE/1.5,
            objectname=f"icon_label",
            text=mod1_text,
            class_group=self.action_widgets,
            width = cons.WSIZE*2,
            align="center",
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

        self.second_label = Widget(
            widget_type=QLabel(),
            stylesheet=estyle.SUB_LABEL,
            parent_layout=self.slot_layot.inner_layout(3),
            height = cons.WSIZE/1.5,
            objectname=f"icon_label",
            text=mod2_text,
            class_group=self.action_widgets,
            width = cons.WSIZE*2,
            align="center"
        )

        self.spacer = Widget(
            widget_type=QPushButton(),
            stylesheet=style.INVENTORY,
            parent_layout=self.slot_layot.inner_layout(4),
            width = 20,
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
            width = 20,
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