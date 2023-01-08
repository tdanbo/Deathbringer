from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import os
import sys
import constants as cons

import functions as func
import stylesheet as style
from combat_log import CombatLog

import json


class MainWindow(QWidget):
    def __init__(self):
        super().__init__(None, Qt.WindowStaysOnTopHint)

        # Layouts
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        # Widget height
        self.widget_height = 30

        #Setting up layouts/sections
        self.log_section = Section(
            QVBoxLayout(),
            self.main_layout,
            group=True,
        )
        self.character_sheet = Section(
            QVBoxLayout(),
            self.main_layout,
            group=True,
        )
        self.log_scroll = Section(
            QVBoxLayout(),
            self.log_section.get_layout(),
            scroll=True,
        )
        self.log_latest = Section(
            QVBoxLayout(),
            self.log_section.get_layout(),
            group=True,
        )
        self.log_dice = Section(
            QHBoxLayout(),
            self.log_section.get_layout(),
            group=True,
        )

        self.combat_log = CombatLog().get_log()

        # we create 10 entries in the log, and update the different widget. This is to reduce the interface popping and too many entries to be added to the interface.
        self.log_dictionary = {}
        for entry in range(10):
            entry_ui = self.create_log_entry(self.log_scroll.get_layout())
            self.log_dictionary[entry] = {"character":entry_ui[0],"icon":entry_ui[1],"type":entry_ui[2],"roll":entry_ui[3],"time":entry_ui[4]}
        latest_entry_ui = self.create_log_entry(self.log_latest.get_layout())
        self.log_dictionary[10] = {"character":latest_entry_ui[0],"icon":latest_entry_ui[1],"type":latest_entry_ui[2],"roll":latest_entry_ui[3],"time":latest_entry_ui[4]}  

        self.update_combat_log()

        # BUTTONS
        dice = [("%",100),("D4",4),("D6",6), ("D8",8), ("D10",10), ("D12",12), ("D20",20)]
        for die in dice:
            Widget(
                widget=QPushButton(),
                layout=self.log_dice.get_layout(),
                text=die[0],
                tooltip=f"Roll {die[0]}",
                signal=self.update_log,
                objectname=str(die[1]),
                width=self.widget_height,
                height=self.widget_height,
            )
                
        self.character_name = Widget(
            widget=QLineEdit(),
            layout=self.character_sheet.get_layout(),
            text="Character Name",
            setting = "text",
            objectname="character_name_button",
            height=self.widget_height,
        )

        # general settings and styling for UI
        self.main_layout.setSpacing(2)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # setting stylesheet
        self.setStyleSheet(style.DARK_STYLE)

    def update_combat_log(self):
        combat_log = CombatLog().get_log()
        for count,entry in enumerate(combat_log):
            character = self.log_dictionary[count]["character"]
            icon = self.log_dictionary[count]["icon"]
            type = self.log_dictionary[count]["type"]
            roll = self.log_dictionary[count]["roll"]
            time = self.log_dictionary[count]["time"]

            character.setText(entry["character"])
            icon.setIcon(QIcon(os.path.join(cons.ICONS,entry["character"]+".png")))
            icon.setIconSize(QSize(30, 30))
            type.setText(entry["type"])
            roll.setText(str(entry["roll"]))
            time.setText(entry["time"])


    def update_log(self, modifier=0):
        die = int(self.sender().objectName())
        roll = func.roll_dice(die) + modifier
        CombatLog().set_entry(self.character_name.get_widget().text(),roll)
        self.update_combat_log()

    def create_log_entry(self, layout):
        # MAIN LOG LAYOUT
        self.log_layout = Section(
            QVBoxLayout(),
            layout,
            group = True,
        )

        # MAIN LOG SUB LAYOUTS
        self.log_name = Section( 
            QHBoxLayout(),
            self.log_layout.get_layout(),
            group=False,
        )

        self.log_data = Section( 
            QHBoxLayout(),
            self.log_layout.get_layout(),
            group=False,
        )

        self.log_date = Section( 
            QHBoxLayout(),
            self.log_layout.get_layout(),
            group=False,
        )

        # LOG CONTENT
        self.log_character_name = Widget(
            QLabel(),
            self.log_name.get_layout(),
        )

        self.log_character_icon = Widget(
            QToolButton(),
            self.log_data.get_layout(),
        )

        self.log_roll_type = Widget(
            QLabel(),
            self.log_data.get_layout(),
        )

        self.log_roll = Widget(
            QLabel(),
            self.log_data.get_layout(),
        )

        self.log_entry_date = Widget(
            QLabel(),
            self.log_date.get_layout(),
            align="right",
        )

        return (
            self.log_character_name.get_widget(), 
            self.log_character_icon.get_widget(), 
            self.log_roll_type.get_widget(), 
            self.log_roll.get_widget(), 
            self.log_entry_date.get_widget()
        )

    def show_hide_settings(self):
        if self.sender().isChecked():
            self.settings_section.get_group().setHidden(False)
        else:
            self.settings_section.get_group().setHidden(True)

class Section:
    def __init__(
        self,
        layout_type,
        parent_layout,
        group=False,
        scroll=False,
        hidden=False,
    ):
        self.layout = layout_type
        self.scroll = scroll

        if group == True:
            self.group = QGroupBox()
            self.group.setLayout(self.layout)
            self.group.setHidden(hidden)
            parent_layout.addWidget(self.group)
        else:
            parent_layout.addLayout(self.layout)

        if self.scroll == True:
            self.scroll_layout = QVBoxLayout()
            self.scroll_widget = QWidget()
            self.scroll_area_widget = QScrollArea()
            self.scroll_area_widget.setWidget(self.scroll_widget)
            self.scroll_widget.setLayout(self.scroll_layout)

            self.scroll_layout.setAlignment(Qt.AlignBottom)
            self.scroll_layout.setSpacing(0)

            self.scroll_area_widget.setWidgetResizable(True)
            self.scroll_area_widget.setHorizontalScrollBarPolicy(
                Qt.ScrollBarAlwaysOff
            )

            self.layout.addWidget(self.scroll_area_widget)

    def get_layout(self):
        if self.scroll == False:
            return self.layout
        else:
            return self.scroll_layout

    def get_group(self):
        return self.group


class Widget:
    _registry = []
    _task_registry = []

    def __init__(
        self,
        widget="",
        layout="",
        text="",
        tooltip="",
        objectname="",
        signal="",
        icon="",
        width="",
        height="",
        align="",
        enabled=True,
        checkable=False,
        task=False,
        validator="",
        placeholder="",
        setting ="",
    ):
        self.text = text
        self.widget = widget
        self.object = objectname
        self.setting = setting
        self.widget.setToolTip(tooltip)
        self.widget.setObjectName(self.object)
        self.widget_key = f"{self.object}_{self.setting}"
        self.set_enabled(enabled)
        self.set_checkable(checkable)
        self.set_text(widget, self.text)
        self.set_signal(widget, signal, setting)
        self.set_alignment(widget, align)
        self.set_size(self.widget, width, height)
        self.set_validator(widget, validator)
        self.set_placeholder(widget, placeholder)
        self.load_setting(objectname, setting)
        if icon != "":
            self.set_icon(self.widget, icon, 30)
        layout.addWidget(self.widget)

        if task == True:
            self._task_registry.append(self)
        else:
            self._registry.append(self)

    def load_setting(self, objectname, setting):
        if os.path.exists(cons.SETTINGS):   
            open_file = open(cons.SETTINGS, "r")
            open_json = json.load(open_file)
            if self.widget_key in open_json:
                if setting == "checked":
                    self.widget.setChecked(open_json[self.widget_key])
                elif setting == "text":
                    self.widget.setText(open_json[self.widget_key])
                elif setting == "value":
                    self.widget.setValue(open_json[self.widget_key])
        else:
            json.dump({}, open(cons.SETTINGS, "w"), indent=4)
        self.save_setting()

    def save_setting(self):
        open_json = json.load(open(cons.SETTINGS, "r"))
        if self.setting == "text":
            open_json[self.widget_key] = self.widget.text()
        elif self.setting == "value":
            open_json[self.widget_key] = self.widget.value()
        elif self.setting == "checked":
            open_json[self.widget_key] = self.widget.isChecked()
        json.dump(open_json, open(cons.SETTINGS, "w"), indent=4)

    def set_enabled(self, enabled):
        try:
            self.widget.setEnabled(enabled)
        except:
            pass

    def set_placeholder(self, widget, placeholder):
        if placeholder != "":
            widget.setPlaceholderText(placeholder)

    def set_validator(self, widget, validator):
        if validator == "":
            pass
        elif validator == "numbers":
            widget.setValidator(QIntValidator())
        elif validator == "percent":
            widget.setValidator(QIntValidator())
            widget.setMaxLength(3)
        else:
            pass

    def set_checkable(self, checkable):
        try:
            self.widget.setCheckable(checkable)
            self.widget.setChecked(checkable)
        except:
            pass

    def get_parent_layout(self, layout):
        return layout

    def get_widget(self):
        return self.widget

    def set_alignment(self, widget, align):
        if align == "":
            pass
        elif align == "left":
            widget.setAlignment(Qt.AlignLeft)
        elif align == "right":
            widget.setAlignment(Qt.AlignRight)
        elif align == "vcenter":
            widget.setAlignment(Qt.AlignVCenter)
        else:
            widget.setAlignment(Qt.AlignHCenter)

    def set_text(self, widget, text):
        try:
            widget.setText(text)
        except:
            pass
        try:
            widget.setValue(int(text))
        except:
            pass

    def set_size(self, widget, width, height):
        try:
            widget.setFixedWidth(width)
        except:
            pass
        try:
            widget.setFixedHeight(height)
        except:
            pass

    def set_signal(self, widget, signal, setting):
        if signal != "":
            try:
                self.widget.clicked.connect(signal)
            except:
                pass
            try:
                self.widget.textEdited.connect(signal)

            except:
                pass
            try:
                self.widget.textChanged.connect(signal)
            except:
                pass

        if setting == "checked":
            self.widget.clicked.connect(self.save_setting)
        elif setting == "text":
            self.widget.textEdited.connect(self.save_setting)

    def set_icon(self, widget, icon, size):
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap(os.path.join(cons.ICONS, icon)))
        widget.setIcon(self.icon)
        widget.setIconSize(QSize(size, size))


def run_gui(name, version):
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("%s v%s" % (name, str(version)))
    w.show()
    app.exec_()
