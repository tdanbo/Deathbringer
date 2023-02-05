from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import pymongo
import constants as cons

import math
import constants as cons
import os
import functions as func

import random
import stylesheet as style

import copy

class CharacterSheet():
    def __init__(self, csheet):
        print("Character Sheet Created")

        self.csheet = csheet
        self.stat_button = None

        self.character = ""
        self.level = csheet.findChild(QPushButton, "level")
        self.coins = ""

        self.ac = csheet.findChild(QPushButton, "ac")
        self.initiative = csheet.findChild(QPushButton, "initiative")

        #morale
        self.max_morale = csheet.findChild(QPushButton, "max_morale")
        self.current_morale = csheet.findChild(QPushButton, "current_morale")

        #hp
        self.max_hp = csheet.findChild(QPushButton, "max_hp")
        self.current_hp = csheet.findChild(QPushButton, "current_hp")
        self.hp_adjuster = csheet.findChild(QLineEdit, "hp_adjuster")

        #feats
        self.feat1 = csheet.findChild(QToolButton, "feat1")
        self.feat2 = csheet.findChild(QToolButton, "feat2")
        self.feat3 = csheet.findChild(QToolButton, "feat3")

        #stats
        self.STR = int(csheet.findChild(QPushButton, "STR").text())
        self.DEX = int(csheet.findChild(QPushButton, "DEX").text())
        self.CON = int(csheet.findChild(QPushButton, "CON").text())
        self.INT = int(csheet.findChild(QPushButton, "INT").text())
        self.WIS = int(csheet.findChild(QPushButton, "WIS").text())
        self.CHA = int(csheet.findChild(QPushButton, "CHA").text())
        
        self.max_slots = int(self.CON)+cons.START_SLOTS

        #stats dictionary
        self.stats_dict = {"":"","AC":1,"STR": self.STR, "DEX": self.DEX, "CON": self.CON, "INT": self.INT, "WIS": self.WIS, "CHA": self.CHA}

        #all inventory slots
        self.inventory1 = csheet.findChild(QLineEdit, "inventory1")
        self.inventory2 = csheet.findChild(QLineEdit, "inventory2")
        self.inventory3 = csheet.findChild(QLineEdit, "inventory3")
        self.inventory4 = csheet.findChild(QLineEdit, "inventory4")
        self.inventory5 = csheet.findChild(QLineEdit, "inventory5")
        self.inventory6 = csheet.findChild(QLineEdit, "inventory6")
        self.inventory7 = csheet.findChild(QLineEdit, "inventory7")
        self.inventory8 = csheet.findChild(QLineEdit, "inventory8")
        self.inventory9 = csheet.findChild(QLineEdit, "inventory9")
        self.inventory10 = csheet.findChild(QLineEdit, "inventory10")
        self.inventory11 = csheet.findChild(QLineEdit, "inventory11")
        self.inventory12 = csheet.findChild(QLineEdit, "inventory12")
        self.inventory13 = csheet.findChild(QLineEdit, "inventory13")
        self.inventory14 = csheet.findChild(QLineEdit, "inventory14")
        self.inventory15 = csheet.findChild(QLineEdit, "inventory15")
        self.inventory16 = csheet.findChild(QLineEdit, "inventory16")
        self.inventory17 = csheet.findChild(QLineEdit, "inventory17")
        self.inventory18 = csheet.findChild(QLineEdit, "inventory18")
        self.inventory19 = csheet.findChild(QLineEdit, "inventory19")
        self.inventory20 = csheet.findChild(QLineEdit, "inventory20")

        #all hero dice slots
        self.herodice1 = csheet.findChild(QToolButton, "herodice1")
        self.herodice2 = csheet.findChild(QToolButton, "herodice2")
        self.herodice3 = csheet.findChild(QToolButton, "herodice3")
        self.herodice4 = csheet.findChild(QToolButton, "herodice4")
        self.herodice5 = csheet.findChild(QToolButton, "herodice5")
        self.herodice6 = csheet.findChild(QToolButton, "herodice6")
        self.herodice7 = csheet.findChild(QToolButton, "herodice7")
        self.herodice8 = csheet.findChild(QToolButton, "herodice8")
        self.herodice9 = csheet.findChild(QToolButton, "herodice9")
        self.herodice10 = csheet.findChild(QToolButton, "herodice10")

        #all corruption slots
        self.corruption1 = csheet.findChild(QToolButton, "corruption1")
        self.corruption2 = csheet.findChild(QToolButton, "corruption2")
        self.corruption3 = csheet.findChild(QToolButton, "corruption3")
        self.corruption4 = csheet.findChild(QToolButton, "corruption4")
        self.corruption5 = csheet.findChild(QToolButton, "corruption5")
        self.corruption6 = csheet.findChild(QToolButton, "corruption6")
        self.corruption7 = csheet.findChild(QToolButton, "corruption7")
        self.corruption8 = csheet.findChild(QToolButton, "corruption8")
        self.corruption9 = csheet.findChild(QToolButton, "corruption9")
        self.corruption10 = csheet.findChild(QToolButton, "corruption10")


        self.update_sheet()
        #updated_character_sheet = self.update_dictionary()
        #self.update_database(updated_character_sheet)

    def update_dictionary(self):
        print("---------------------------") 
        print("Updating Character Sheet Dictionary")    
        character_sheet_dictionary = {
            "character": self.character,
            "level": self.level,
            "coins": self.coins,
            "max hp": self.max_hp.text(),
            "current hp": self.current_hp.text(),
            "ac": self.ac.text(),
            "initiative": self.initiative.text(),
            "stats": {
                "str": self.STR,
                "dex": self.DEX,
                "con": self.CON,
                "int": self.INT,
                "wis": self.WIS,
                "cha": self.CHA,
            },
            "inventory": {
                "inventory1": self.inventory1.text(),
                "inventory2": self.inventory2.text(),
                "inventory3": self.inventory3.text(),
                "inventory4": self.inventory4.text(),
                "inventory5": self.inventory5.text(),
                "inventory6": self.inventory6.text(),
                "inventory7": self.inventory7.text(),
                "inventory8": self.inventory8.text(),
                "inventory9": self.inventory9.text(),
                "inventory10": self.inventory10.text(),
                "inventory11": self.inventory1.text(),
                "inventory12": self.inventory2.text(),
                "inventory13": self.inventory3.text(),
                "inventory14": self.inventory4.text(),
                "inventory15": self.inventory5.text(),
                "inventory16": self.inventory6.text(),
                "inventory17": self.inventory7.text(),
                "inventory18": self.inventory8.text(),
                "inventory19": self.inventory9.text(),
                "inventory20": self.inventory10.text(),
            },            
            "corruption": { 
                "corruption1": self.corruption1.isChecked(),
                "corruption2": self.corruption2.isChecked(),
                "corruption3": self.corruption3.isChecked(),
                "corruption4": self.corruption4.isChecked(),
                "corruption5": self.corruption5.isChecked(),
                "corruption6": self.corruption6.isChecked(),
                "corruption7": self.corruption7.isChecked(),
                "corruption8": self.corruption8.isChecked(),
                "corruption9": self.corruption9.isChecked(),
                "corruption10": self.corruption10.isChecked(),

            },
            "herodice": {
                "herodice1": self.herodice1.isChecked(),
                "herodice2": self.herodice2.isChecked(),
                "herodice3": self.herodice3.isChecked(),
                "herodice4": self.herodice4.isChecked(),
                "herodice5": self.herodice5.isChecked(),
                "herodice6": self.herodice6.isChecked(),
                "herodice7": self.herodice7.isChecked(),
                "herodice8": self.herodice8.isChecked(),
                "herodice9": self.herodice9.isChecked(),
                "herodice10": self.herodice10.isChecked(),
            },
        }        
        return character_sheet_dictionary
    
    def update_database(self, directory):
        self.client = pymongo.MongoClient(cons.CONNECT)
        self.db = self.client ["dnd"]
        self.collection = self.db["characters"]

        query = {"character": self.character.text()}
        document = self.collection.find_one(query)

        if document is not None:
            print("updating existing character")
            new_values = {"$set": directory}
            self.collection.update_one(query, new_values)
        else:
            print("inserting new character")
            self.collection.insert_one(directory)

    def update_sheet(self):
        #INVENTORY RULES
        self.strenght()
        self.dexterity()
        self.constitution()
        self.intelligence()
        self.wisdom()
        self.charisma()
        

        self.update_inventory()

    # ITERATE OVER ITEM JSON TO FIND ITEM
    def update_inventory(self):
        all_items = []
        print("updating inventory")

        self.empty_slot_dict = {"Hit":"","Evoke":"","Evoke Mod":["","",""],"Hit Mod":["","",""],"Roll":"","Roll Mod":["","",""]}
        for slot in range(1,cons.MAX_SLOTS+1):
            self.inventory_slot = self.csheet.findChild(QLineEdit, f"inventory{slot}")
            if self.inventory_slot.text() != "":
                all_items.append(self.inventory_slot.text())
            else:
                pass

        for slot in range(1,cons.MAX_SLOTS+1):
            self.update_item(slot, "", "", self.empty_slot_dict)

        print(all_items)
        misc_items = copy.deepcopy(all_items)
        self.armor_items = []
        slot = 1
        for item_type in os.listdir(cons.ITEMS):
            item_type_json = func.read_json(os.path.join(cons.ITEMS,item_type))
            for item in all_items:
                for item_key in item_type_json:
                    if item_key.lower() == item.lower():
                        this_item_type = item_type.split(".")[0].split("_")[1]
                        if this_item_type == "armor":
                            self.armor_items.append(item)
                        self.update_item(slot, item_key, this_item_type, item_type_json[item_key])
                        misc_items.remove(item)
                        slot += 1

        for item in misc_items:
            self.update_item(slot, item, "misc", self.empty_slot_dict)
            all_items.remove(item)
            slot += 1

        self.set_ac()
        self.set_morale()
        self.set_hp()
        self.set_feats()

    def update_item(self, slot, item, inventory_type, inventory_item):
        self.inventory_icon = self.csheet.findChild(QToolButton, f"icon{slot}")
        self.inventory_evoke = self.csheet.findChild(QPushButton, f"evoke{slot}")
        self.inventory_hit = self.csheet.findChild(QPushButton, f"hit_dc{slot}")
        self.inventory_roll = self.csheet.findChild(QPushButton, f"roll{slot}")
        self.inventory_slot = self.csheet.findChild(QLineEdit, f"inventory{slot}")

        self.inventory_icon_label = self.csheet.findChild(QLabel, f"icon_label{slot}")
        self.inventory_evoke_label = self.csheet.findChild(QLabel, f"evoke_label{slot}")
        self.inventory_hit_label = self.csheet.findChild(QLabel, f"hit_dc_label{slot}")
        self.inventory_roll_label = self.csheet.findChild(QLabel, f"roll_label{slot}")
        self.inventory_slot_label = self.csheet.findChild(QLabel, f"inventory_label{slot}")

        inventory_widgets = [self.inventory_icon,self.inventory_evoke,self.inventory_hit,self.inventory_roll,self.inventory_slot]
        inventory_labels = [self.inventory_icon_label,self.inventory_evoke_label,self.inventory_hit_label,self.inventory_roll_label,self.inventory_slot_label]
        func.set_icon(self.inventory_icon,f"{inventory_type}.png",cons.ICON_COLOR)

        self.inventory_evoke.setText("")
        self.inventory_evoke_label.setText("")
        self.inventory_hit.setText("")
        self.inventory_hit_label.setText("")
        self.inventory_roll.setText("")
        self.inventory_roll_label.setText("")   

        if "Evoke" in inventory_item:
            if inventory_item["Evoke"] != "":
                self.inventory_evoke.setText(self.get_action_modifier(inventory_item["Evoke"],inventory_item["Evoke Mod"]))
                self.inventory_evoke_label.setText(inventory_item["Evoke"])


        if "Hit" in inventory_item:
            if inventory_item["Hit"] != "":
                self.inventory_hit.setText(self.get_action_modifier(inventory_item["Hit"],inventory_item["Hit Mod"]))
                self.inventory_hit_label.setText(inventory_item["Hit"])

        if "Roll" in inventory_item:
            if inventory_item["Roll"] != "":
                self.inventory_roll.setText(self.get_roll(inventory_item["Roll Mod"],inventory_type))
                self.inventory_roll_label.setText(inventory_item["Roll"])
                
        self.inventory_slot.setText(item)

        if "level" in inventory_item:
            self.inventory_slot_label.setText(inventory_type.capitalize()+" "+inventory_item["level"])
        else:
            self.inventory_slot_label.setText(inventory_type.capitalize())

        if inventory_type == "damage":     
            [widget.setStyleSheet(style.INVENTORY_INJURY) for widget in inventory_widgets]
            [widget.setStyleSheet(style.INVENTORY_INJURY_LABELS) for widget in inventory_labels]
            func.set_icon(self.inventory_icon,f"{inventory_type}.png",style.INJURY_RED_BRIGHT)
        elif inventory_type != "":

            label_style = f"QLabel {{font: 10px; color:{style.TEXT_DARK_COLOR}; background-color: {cons.COLOR_LABEL[inventory_type]}; border: 0px; border-bottom: 1px solid {cons.COLOR_LABEL[inventory_type]};}}"
            label_style2 = f"QLabel {{font: 10px; color:{style.TEXT_DARK_COLOR}; background-color: {style.DARK_COLOR}; border: 0px; border-bottom: 1px solid {cons.COLOR_LABEL[inventory_type]};}}"\
                           f"QPushButton {{font: 10px; color:{style.TEXT_DARK_COLOR}; background-color: {style.DARK_COLOR}; border: 0px; border-bottom: 1px solid {cons.COLOR_LABEL[inventory_type]};}}"\

            self.inventory_icon_label.setStyleSheet(label_style)
            self.inventory_slot_label.setStyleSheet(label_style2)
            self.inventory_evoke_label.setStyleSheet(label_style2)
            self.inventory_hit_label.setStyleSheet(label_style2)
            self.inventory_roll_label.setStyleSheet(label_style2)

        else:
            [widget.setStyleSheet(style.INVENTORY) for widget in inventory_widgets]
            [widget.setStyleSheet(style.INVENTORY) for widget in inventory_labels]

        self.inventory_slot.clearFocus()        


    def get_roll(self, roll, type):
        if roll != ["","",""]:
            make_roll = []
            if roll[0] in self.stats_dict:
                make_roll.append(str(self.stats_dict[roll[0]]))
            else:
                make_roll.append(str(roll[0]))
            
            make_roll.append(str(roll[1]))

            if roll[2] != "":
                if roll[2] in self.stats_dict:
                    if type == "weapon":
                        roll_mod = math.floor(self.stats_dict[roll[2]]) #full damage
                        #roll_mod = math.floor(self.stats_dict[roll[2]]/2)
                    else:
                        roll_mod = math.floor(self.stats_dict[roll[2]])
                else:
                    roll_mod = roll[2]
                
                if int(roll_mod) > 0:
                    make_roll.append(f"+{roll_mod}")
                else:
                    pass

            final_roll = "".join(make_roll)
            return final_roll
        else:
            return ""


    def get_action_modifier(self, hit_type, hit_mod):
        if hit_mod != []:
            if hit_type == "Hit":
                mod_list = []
                for mod in hit_mod:
                    mod_list.append(self.stats_dict[mod])
                return f"+{sum(mod_list)}"
            elif "Evoke" in hit_type:
                mod_list = []
                for mod in hit_mod:
                    mod_list.append(self.stats_dict[mod])
                return f"+{sum(mod_list)}"
            elif "Save" in hit_type:
                mod_list = []
                for mod in hit_mod:
                    mod_list.append(self.stats_dict[mod])
                return(str(cons.BASE_SAVE+sum(mod_list)))
            else:
                return ""
        else:
            return ""

    def set_morale(self):
        self.max_morale.setText(f"{cons.BASE_MORALE+int(self.CHA)}")
        if self.level == 0:
            self.current_morale.setText(f"{cons.BASE_MORALE+int(self.CHA)}")

    def set_ac(self):
        ac = int(self.ac.text())
        ac += len(self.armor_items)
        self.ac.setText(str(ac))

    def set_hp(self):
        level = math.floor(float(self.level.text()))
        if level == 0:
            hp_formula = cons.HIT_DICE
            self.current_hp.setText(str(hp_formula))
        else:
            hp_formula = (cons.HIT_DICE*level) + self.CON
        self.max_hp.setText(str(hp_formula))
        

    def adjust_hp(self, state, value):
        print(state, value)
        current_hp = int(self.current_hp.text())
        self.current_hp.setStyleSheet(style.BUTTONS)
        for point in range(1,int(value)+1):
            if state == "minus":
                current_hp -= 1
                if current_hp < 0:
                    self.add_injury()
            else:  
                if current_hp < 0:
                    self.remove_injury()
                current_hp += 1


        if current_hp > int(self.max_hp.text()):
            self.current_hp.setText(self.max_hp.text())
        elif current_hp < -abs(self.max_slots):
            self.current_hp.setText(str(-abs(self.max_slots)))
        else:
            self.current_hp.setText(str(current_hp))   

        if current_hp >= 0:
            self.current_hp.setStyleSheet(style.BIG_BUTTONS)
        else:
            self.current_hp.setStyleSheet(style.BUTTONS_INJURY)

        self.update_dictionary()
        self.update_inventory()

    def remove_injury(self):
        print("remove injury")
        for slot in range(1,self.max_slots+1):
            widget_slot = self.csheet.findChild(QLineEdit, f"inventory{slot}")
            if widget_slot.text() == "Injury":
                self.update_item(slot, "", "", self.empty_slot_dict)
                return
            else:
                pass

    def add_injury(self):
        current_slots = int(self.CON)+cons.START_SLOTS
        free_slots = []
        for slot in range(1,current_slots+1):
            widget_slot = self.csheet.findChild(QLineEdit, f"inventory{slot}")
            if widget_slot.text() == "Injury":
                pass
            else:
                free_slots.append(slot)
        if free_slots == []:
            print("DEAD")
            return
        else:
            injury_slot = random.choice(free_slots)
            self.update_item(injury_slot, "Injury", "damage", self.empty_slot_dict)


    def strenght(self):
        pass 
    def dexterity(self):
        #ac_calculation = str(cons.BASE_AC+math.floor(int(self.DEX)/2))
        ac_calculation = str(cons.BASE_AC+math.floor(int(self.DEX)))
        self.ac.setText(ac_calculation)

    def constitution(self):
        for count in range(1,cons.MAX_SLOTS+1):
            for w in [(QToolButton,"icon"),(QPushButton,"evoke"),(QPushButton,"hit_dc"),(QPushButton,"roll"),(QLineEdit,"inventory"),(QLabel,"icon_label"),(QLabel,"inventory_label"),(QLabel,"evoke_label"),(QLabel,"hit_dc_label"),(QLabel,"roll_label")]:
                widget =  self.csheet.findChild(w[0], w[1]+str(count))
                if count <= self.CON+cons.START_SLOTS:
                    widget.setEnabled(True)
                else:
                    if w[1] != "icon_label":
                        widget.setText("")
                    widget.setEnabled(False)

    def intelligence(self):
        for count in range(1,11):
            for w in [(QToolButton,"herodice")]:
                widget =  self.csheet.findChild(w[0], w[1]+str(count))
                if count <= self.INT:
                    widget.setEnabled(True)
                else:
                    widget.setEnabled(False)

    def wisdom(self):
        for count in range(1,11):
            for w in [(QToolButton,"corruption")]:
                widget =  self.csheet.findChild(w[0], w[1]+str(count))
                if count <= self.WIS:
                    widget.setEnabled(True)
                else:
                    widget.setEnabled(False)

    def set_feats(self):
        current_level = math.floor(float(self.level.text()))
        if current_level < 3:
            self.feat1.setEnabled(False)
            self.feat2.setEnabled(False)
            self.feat3.setEnabled(False)
        if current_level == 3:
            self.feat1.setEnabled(True)
            self.feat2.setEnabled(False)
            self.feat3.setEnabled(False)
        elif current_level == 6:
            self.feat1.setEnabled(True)
            self.feat2.setEnabled(True)
            self.feat3.setEnabled(False)
        elif current_level == 9:
            self.feat1.setEnabled(True)
            self.feat2.setEnabled(True)
            self.feat3.setEnabled(True)


    def charisma(self):
        initiative_widget = self.csheet.findChild(QPushButton, "initiative")
        movement_widget = self.csheet.findChild(QPushButton, "movement")
        initiative_widget.setText(f"{self.CHA+10} init.")
        movement_widget.setText(f"{20+(self.CHA*5)} ft.")

    