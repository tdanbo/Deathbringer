from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import sys
import os

from pyside import Section
from pyside import Widget

from gui_encounter.encounter_gui import EncounterGUI

app = QApplication(sys.argv)
window = EncounterGUI()
window.show()
app.exec_()