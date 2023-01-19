from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from pyside import Section
from pyside import Widget

from gui_sheet import CharacterSheetGUI
from gui_log import CombatLogGUI
import os
import sys
import constants as cons

import functions as func
import stylesheet as style

from combat_log import CombatLog
from character_sheet import CharacterSheet



class MainWindow(QWidget):
    def __init__(self):
        super().__init__(None, Qt.WindowStaysOnTopHint)

        # Layouts
        self.main_layout = QHBoxLayout()

        combat_log_gui = CombatLogGUI()
        character_sheet_gui = CharacterSheetGUI()
        combat_log_widgets = combat_log_gui.get_widget_directory()
        
        #initializing the two main classes
        self.combat_log = CombatLog(combat_log_widgets)    
        
        self.combat_log.update_combat_log()
        self.combat_log.start_watching() 

        for widget in Widget.all_widgets:
            widget.connect_to_parent()
            widget.set_signal()

        for section in Section.all_sections:
            section.connect_to_parent()

        character_sheet_gui.setFixedWidth(500)

        self.main_layout.addWidget(combat_log_gui)
        self.main_layout.addWidget(character_sheet_gui)

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

