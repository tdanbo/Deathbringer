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

        combat_log_gui = CombatLogGUI()
        character_sheet_gui = CharacterSheetGUI()
        combat_log_widgets = combat_log_gui.get_widget_directory()
        # print(combat_log_widgets)
        # self.combat_log = CombatLog(combat_log_widgets)        
        # self.combat_log.update_combat_log()
        # self.combat_log.start_watching() 

        for widget in Widget.all_widgets:
            widget.connect_to_parent()

        for section in Section.all_sections:
            section.connect_to_parent()

        self.main_layout.addLayout(combat_log_gui.get_main_layout())
        self.main_layout.addLayout(character_sheet_gui.get_main_layout())



        self.setLayout(self.main_layout)
        self.setStyleSheet(style.DARK_STYLE)

    def closeEvent(self, event: QCloseEvent):
        self.combat_log.stop_watching()

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

