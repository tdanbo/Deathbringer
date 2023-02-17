from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import sys
import os

from pyside import Section
from pyside import Widget

from gui_encounter.encounter_gui import EncounterGUI

        
print(Section)

for widget in Widget.all_widgets:
    widget.connect_to_parent()
    widget.set_signal()

for section in Section.all_sections:
    print(section)
    section.connect_to_parent()

app = QApplication(sys.argv)
window = EncounterGUI()
window.show()
app.exec_()