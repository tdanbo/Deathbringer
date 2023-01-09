from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from my_pyside import Section
from my_pyside import Widget

from character_sheet_gui import CharacterSheetGUI
from combat_log_gui import CombatLogGUI
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

        # Widget height
        self.widget_height = 30

        #Setting up layouts/sections
        self.log_section = QVBoxLayout()
        self.character_sheet = QVBoxLayout()
        self.log_scroll = QVBoxLayout()
        self.log_latest = QVBoxLayout()
        self.log_dice = QHBoxLayout()

        self.scroll_layout = QVBoxLayout()
        self.scroll_area_widget = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_widget.setLayout(self.scroll_layout)

        self.scroll_area_widget.setWidget(self.scroll_widget)

        self.scroll_layout.setAlignment(Qt.AlignBottom)
        self.scroll_layout.setSpacing(9)

        self.scroll_area_widget.setWidgetResizable(True)
        self.scroll_area_widget.setHorizontalScrollBarPolicy(
            Qt.ScrollBarAlwaysOff
        )

        self.log_scroll.addWidget(self.scroll_area_widget)

        # we create 10 entries in the log, and update the different widget. This is to reduce the interface popping and too many entries to be added to the interface.
        self.log_dictionary = {}
        for entry in range(10):
            entry_ui = self.create_log_entry(self.scroll_layout)
            self.log_dictionary[entry] = {"character":entry_ui[0],"icon":entry_ui[1],"type":entry_ui[2],"roll":entry_ui[3],"time":entry_ui[4]}
        latest_entry_ui = self.create_log_entry(self.log_latest)
        self.log_dictionary[10] = {"character":latest_entry_ui[0],"icon":latest_entry_ui[1],"type":latest_entry_ui[2],"roll":latest_entry_ui[3],"time":latest_entry_ui[4]}  

        self.combat_log = CombatLog(self.log_dictionary)        
        self.combat_log.update_combat_log()
        self.combat_log.start_watching()

        # BUTTONS
        dice = [("%",100),("D4",4),("D6",6), ("D8",8), ("D10",10), ("D12",12), ("D20",20)]
        for die in dice:
            Widget(
                widget_type=QPushButton(),
                parent_layout=self.log_dice,
                text=die[0],
                tooltip=f"Roll {die[0]}",
                signal=self.update_log,
                objectname=str(die[1]),
                width=self.widget_height,
                height=self.widget_height,
            )
                
        self.character_name = Widget(
            widget_type=QLineEdit(),
            parent_layout=self.character_sheet,
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

        self.log_section.addLayout(self.log_scroll)
        self.log_section.addLayout(self.log_latest)
        self.log_section.addLayout(self.log_dice)

        self.main_layout.addLayout(self.log_section)
        self.main_layout.addLayout(CombatLogGUI().get_main_layout())
        self.main_layout.addLayout(CharacterSheetGUI().get_main_layout())

        self.setLayout(self.main_layout)

    def closeEvent(self, event: QCloseEvent):
        self.combat_log.stop_watching()

    def update_log(self, modifier=0):
        die = int(self.sender().objectName())
        roll = func.roll_dice(die) + modifier
        self.combat_log.set_entry(self.character_name.get_widget().text(),roll)

    def create_log_entry(self, layout):
        # MAIN LOG LAYOUT

        self.log_parent_layout = layout
        self.log_layout = QVBoxLayout()
        self.log_layout.setSpacing(2)

        name_stylesheet = "font-size: 12px; font-weight: bold; color: hsl(0%, 0%, 50%)"
        icon_stylesheet = "background-color: hsl(0%, 0%, 80%);"
        type_stylesheet = "font-size: 12px; font-weight: bold; background-color: hsl(0%, 0%, 80%); color: hsl(0%, 0%, 20%); border: 0px;"
        roll_stylesheet = "font-size: 20px; font-weight: bold; background-color: hsl(0%, 0%, 80%); color: hsl(0%, 0%, 10%); border: 0px; border-top-right-radius: 8px; border-bottom-right-radius: 8px;"
        date_stylesheet = "font-size: 10px; color: hsl(0%, 0%, 30%)"

        # MAIN LOG SUB LAYOUTS
        self.log_name = QHBoxLayout()
        self.log_data = QHBoxLayout()
        self.log_date = QHBoxLayout()

        # LOG CONTENT
        self.log_character_name = Widget(
            widget_type = QLabel(),
            parent_layout = self.log_name,
            stylesheet = name_stylesheet,
        )

        self.log_character_icon = Widget(
            widget_type = QToolButton(),
            parent_layout = self.log_data,
            height = 40,
            width = 40,
            stylesheet = icon_stylesheet,
        )

        self.log_roll_type = Widget(
            widget_type = QLineEdit(),
            parent_layout = self.log_data,
            stylesheet = type_stylesheet,
            align="left",
            height = 40,
        )

        self.log_roll = Widget(
            widget_type = QLineEdit(),
            parent_layout = self.log_data,
            enabled = False,
            height = 40,
            width = 40,
            align="center",
            stylesheet = roll_stylesheet,
        )

        self.log_entry_date = Widget(
            widget_type = QLabel(),
            parent_layout = self.log_date,
            align="right",
            stylesheet = date_stylesheet,
        )

        self.log_layout.addLayout(self.log_name)
        self.log_layout.addLayout(self.log_data)
        self.log_layout.addLayout(self.log_date)

        self.log_parent_layout.addLayout(self.log_layout)

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

def run_gui(name, version):
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("%s v%s" % (name, str(version)))
    w.show()
    app.exec_()

