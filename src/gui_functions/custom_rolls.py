import constants as cons

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import stylesheet as style
import random

from character_sheet import CharacterSheet
from combat_log import CombatLog

def add_dice(self, dice, adjust="add"):
    print(dice)
    if "_count" in dice:
        count_widget = self.findChild(QPushButton, f"{dice}")
    else:
        count_widget = self.findChild(QPushButton, f"{dice}_count")

    if count_widget.text() == "":
        current_value = 0
    else:
        current_value = int(count_widget.text())

    if adjust == "add":
        count_widget.setText(str(current_value + 1))
        count_widget.setHidden(False)
    else:
        if current_value > 0:
            count_widget.setText(str(current_value - 1))
            if count_widget.text() == "0":
                count_widget.setText("")
                count_widget.setHidden(True)
                
        else:
            count_widget.setText("")
            count_widget.setHidden(True)

    roll_button(self, shown=False)        
    for objectname in ["d4","d6","d8","d10","d12","d20","MOD"]:
        widget = self.findChild(QPushButton, objectname)
        counter = self.findChild(QPushButton, f"{objectname}_count")
        if counter.text() == "":
            widget.setStyleSheet(style.DICE_TRAY)
        else:
            widget.setStyleSheet(style.DICE_TRAY1)
            roll_button(self, shown=True)
            


def roll_button(self, shown=False):
    title_widgets = self.log_dice.get_title()
    title_widgets[0].setHidden(shown)
    title_widgets[1].setHidden(shown)

    self.roll_button.get_widget().setHidden(not shown)

def roll_check(self, dictionary, stat):
    stat_mod = int(self.findChild(QPushButton, stat).text())
    roll = random.randint(1, 20)

    breakdown_roll_dice = f"1d20+{stat_mod}"
    breakdown_roll_result = f"{roll}+{stat_mod}"

    result = stat_mod + roll

    breakdown_dict = {"hit_dice":"","hit_results":"", "roll_dice":breakdown_roll_dice, "roll_results": breakdown_roll_result,}

    stats = {"STR": "Strength", "DEX": "Dexterity", "CON": "Constitution", "INT": "Intelligence", "WIS": "Wisdom", "CHA": "Charisma"}
    stat_name = stats[stat]
    CombatLog(dictionary).set_entry("Beasttoe", action_type=stat_name, action_name=breakdown_dict["roll_dice"], hit_desc="", roll_desc="Check", hit="", roll=result, breakdown=breakdown_dict)  

def roll_dice(self, dictionary):
    custom_dice = []
    breakdown_dice = []
    breakdown_rolls = []
    for dice in ["d4","d6","d8","d10","d12","d20"]:
        counter = self.findChild(QPushButton, f"{dice}_count").text()
        if counter != "":
            multiplier = int(counter)
            dice = int(dice[1:])
            for i in range(multiplier):
                result = random.randint(1, dice)
                breakdown_rolls.append(str(result))
                custom_dice.append(result)
            breakdown_dice.append(f"{multiplier}d{dice}")

    modifier = self.findChild(QPushButton, "MOD_count").text()
    if modifier != "":
        custom_dice.append(int(modifier))
        breakdown_dice.append(modifier)
        breakdown_rolls.append(modifier)
    result = sum(custom_dice)

    breakdown_roll_dice = "+".join(breakdown_dice)
    breakdown_roll_result = "+".join(breakdown_rolls)   

    breakdown_dict = {"hit_dice":"","hit_results":"", "roll_dice":breakdown_roll_dice, "roll_results": breakdown_roll_result,}

    CombatLog(dictionary).set_entry("Beasttoe", action_type="Roll", action_name=breakdown_dict["roll_dice"], hit_desc="", roll_desc="Custom", hit="", roll=result, breakdown=breakdown_dict)
    clear_rolls(self)

def clear_rolls(self):
    for objectname in ["d4","d6","d8","d10","d12","d20","MOD"]:
        widget = self.findChild(QPushButton, objectname)
        counter = self.findChild(QPushButton, f"{objectname}_count")
        counter.setText("")
        counter.setHidden(True)
        widget.setStyleSheet(style.DICE_TRAY)
    roll_button(self, shown=False)

def dice_reroll(self, dictionary, objectname):
    roll_widget = self.findChild(QPushButton, objectname)
    if "hit" in objectname:
        rerolls = roll_widget.property("hit_dice").split("+")
    else:
        rerolls = roll_widget.property("roll_dice").split("+")	
    new_rolls = []
    print(new_rolls)
    if rerolls != [""]:
        for r in rerolls:
            if "d" in r:
                dice = r.split("d")
                for modifier in range(int(dice[0])):
                    new_rolls.append(random.randint(1,int(dice[1])))
            else:
                print(r)
                new_rolls.append(int(r))

        print(sum(new_rolls))
        roll_widget.setText(f"{roll_widget.text().split(' ')[0]} {sum(new_rolls)}")
        if "hit" in objectname:
            roll_widget.setStyleSheet(style.COMBAT_BUTTON_1_REROLL)
        else:
            roll_widget.setStyleSheet(style.COMBAT_BUTTON_2_REROLL)