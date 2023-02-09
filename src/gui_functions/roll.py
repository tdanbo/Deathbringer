from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import random

from combat_log import CombatLog
import re
import constants as cons

from gui_log import CombatLogGUI

from gui_functions import custom_rolls

def check_prepare_roll(self,stat):
    stats = {"STR": "Strength", "DEX": "Dexterity", "CON": "Constitution", "INT": "Intelligence", "WIS": "Wisdom", "CHA": "Charisma"}
    roll = self.findChild(QPushButton, f"{stat}").text()
    roll = f"+{roll}"

    char_name = self.findChild(QComboBox, "name").currentText()
    make_roll(char_name, stats[stat], single = {"type":"Check","roll":roll})

def custom_prepare_roll(self,char_name,action):
    rolls = []
    for dice in ["d4","d6","d8","d10","d12","d20"]:
        counter = self.findChild(QPushButton, f"{dice}_count").text()
        if counter != "":
            rolls.append(f"{counter}{dice}")

    modifier = self.findChild(QPushButton, "MOD_count").text()

    roll = "_".join(rolls)+"+"+modifier

    print(roll)

    make_roll(char_name,"Roll", single = {"type":action,"roll":roll})
    custom_rolls.clear_rolls(self)

def inventory_prepare_double_roll(self,slot):
    name = self.findChild(QLineEdit, f"inventory{slot}").text()
    
    first_type = self.findChild(QLabel, f"roll_label{slot}").text()
    first_roll = self.findChild(QPushButton, f"roll{slot}").text()

    second_type = self.findChild(QLabel, f"hit_dc_label{slot}").text()
    second_roll = self.findChild(QPushButton, f"hit_dc{slot}").text()

    char_name = self.findChild(QComboBox, "name").currentText()
    make_roll(char_name, name, single = {"type":first_type,"roll":first_roll}, double = {"type":second_type,"roll":second_roll})

def inventory_prepare_roll(self,action,slot):
    name = self.findChild(QLineEdit, f"inventory{slot}").text()
    type = self.findChild(QLabel, f"{action}_label{slot}").text()
    roll = self.findChild(QPushButton, f"{action}{slot}").text()
    
    char_name = self.findChild(QComboBox, "name").currentText()
    make_roll(char_name, name, single = {"type":type,"roll":roll})

def make_roll(char_name, name, single = {"type":"","roll":""}, double = {"type":"","roll":""}): # the format of a roll dict is {"type":"Hit","roll":"1d20+5"}

    # In some cases we roll both hit and damage at the same time. This is the reason for the double_roll which will add two different rolls on one widget.
    single_roll = roll(single)
    double_roll = roll(double)

    CombatLog(CombatLogGUI).set_entry(
        character = char_name, 
        action_name=name, 
        action_dice=single_roll["first"]["dice breakdown"],
        # hit
        first_hit=double_roll["first"]["result"],
        second_hit=double_roll["second"]["result"], 
        desc_hit=double_roll["first"]["type"], 
        double_breakdown=double_roll,
        # roll
        first_roll=single_roll["first"]["result"],
        second_roll=single_roll["second"]["result"],
        roll_desc=single_roll["first"]["type"], 
        single_breakdown=single_roll,
    )

def roll(roll_dict):
    roll_type = roll_dict["type"]
    roll_string = roll_dict["roll"]
    # First we filter the string to convert it in to a useful format. Or return if it is just a flat number.

    full_roll = {}

    if roll_string.startswith("+"):
        roll_string = f"1d20{roll_string}"

    # Then we do two rolls, a primary roll and a secondary roll used for advantage and disadvantage.
    
    for dice_roll in ["first","second"]:  

        if roll_string.isdigit():
            roll_type = roll_type
            total_result = roll_string
            dice_breakdown = ""
            result_breakdown = ""
        else:
            # Then we split the string in to all the dice rolls 
            roll_list = roll_string.split("_")

            results = []
            dice_breakdown = []
            result_breakdown = []
            for roll in roll_list:
                result = [0, 0, 0]
                numbers = re.findall(r'\d+', roll)
                for i, number in enumerate(numbers):
                    result[i % 3] += int(number)

                roll_multiplier = result[0]
                roll_die = result[1]
                roll_modifier = result[2]

                # Then we roll the dice and add the modifier
                all_roll = []
                for i in range(roll_multiplier):
                    result = random.randint(1, roll_die)
                    all_roll.append(result)
                    result_breakdown.append(str(result))

                dice_breakdown.append(f"{roll_multiplier}d{roll_die}")
                results.append(sum(all_roll))

            dice_breakdown.append(f"{roll_modifier}")
            result_breakdown.append(f"{roll_modifier}")


            total_result = sum(results)+roll_modifier
            dice_breakdown = "+".join(dice_breakdown)
            result_breakdown = "+".join(result_breakdown)
            if total_result == 0:
                total_result = ""
                dice_breakdown = ""
                result_breakdown = ""

        full_roll[dice_roll] = {"type":roll_type,"result":total_result,"dice breakdown":dice_breakdown,"result breakdown":result_breakdown}

    return full_roll