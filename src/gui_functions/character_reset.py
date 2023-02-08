from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import stylesheet as style
from character_sheet import CharacterSheet

def reset_hp(self):
    max_hp = self.character_hp_max.get_widget().text()
    current_hp = self.character_hp_current.get_widget().text()

    difference = int(max_hp) - int(current_hp)

    CharacterSheet(self).adjust_hp("plus", str(difference))

def reset_morale(self):
    max_morale = self.character_max_morale.get_widget().text()
    self.character_current_morale.get_widget().setText(max_morale)
    self.character_current_morale.get_widget().setStyleSheet(style.BIG_BUTTONS)
    CharacterSheet(self).update_sheet()

def reset_focus(self):
    for widget in ["focusdice1", "focusdice2", "focusdice3", "focusdice4", "focusdice5", "focusdice6", "focusdice7", "focusdice8", "focusdice9", "focusdice10"]:
        focus_widget = self.findChild(QToolButton, widget)
        focus_widget.setChecked(False)
    CharacterSheet(self).update_sheet()

def reset_spell_slots(self):
    for widget in ["spellslot1", "spellslot2", "spellslot3", "spellslot4", "spellslot5", "spellslot6", "spellslot7", "spellslot8", "spellslot9", "spellslot10"]:
        spell_slot_widget = self.findChild(QToolButton, widget)
        spell_slot_widget.setChecked(False)
    CharacterSheet(self).update_sheet()