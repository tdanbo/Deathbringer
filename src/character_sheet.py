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

import json
import copy

class CharacterSheet():
    def __init__(self, csheet):
        print("---------------------------") 
        print("Character Sheet Created")

        self.csheet = csheet
        self.stat_button = None

        self.character_icon = csheet.findChild(QLabel, "portrait")
        self.character = csheet.findChild(QComboBox, "name")
        self.level = csheet.findChild(QPushButton, "level")

        self.ac = csheet.findChild(QPushButton, "ac")
        self.initiative = csheet.findChild(QPushButton, "initiative")
        self.speed = csheet.findChild(QPushButton, "movement")

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
        self.STR = csheet.findChild(QPushButton, "STR")
        self.DEX = csheet.findChild(QPushButton, "DEX")
        self.CON = csheet.findChild(QPushButton, "CON")
        self.INT = csheet.findChild(QPushButton, "INT")
        self.WIS = csheet.findChild(QPushButton, "WIS")
        self.CHA = csheet.findChild(QPushButton, "CHA")
        
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
        self.focusdice1 = csheet.findChild(QToolButton, "focusdice1")
        self.focusdice2 = csheet.findChild(QToolButton, "focusdice2")
        self.focusdice3 = csheet.findChild(QToolButton, "focusdice3")
        self.focusdice4 = csheet.findChild(QToolButton, "focusdice4")
        self.focusdice5 = csheet.findChild(QToolButton, "focusdice5")
        self.focusdice6 = csheet.findChild(QToolButton, "focusdice6")
        self.focusdice7 = csheet.findChild(QToolButton, "focusdice7")
        self.focusdice8 = csheet.findChild(QToolButton, "focusdice8")
        self.focusdice9 = csheet.findChild(QToolButton, "focusdice9")
        self.focusdice10 = csheet.findChild(QToolButton, "focusdice10")

        #all spellslot slots
        self.spellslot1 = csheet.findChild(QToolButton, "spellslot1")
        self.spellslot2 = csheet.findChild(QToolButton, "spellslot2")
        self.spellslot3 = csheet.findChild(QToolButton, "spellslot3")
        self.spellslot4 = csheet.findChild(QToolButton, "spellslot4")
        self.spellslot5 = csheet.findChild(QToolButton, "spellslot5")
        self.spellslot6 = csheet.findChild(QToolButton, "spellslot6")
        self.spellslot7 = csheet.findChild(QToolButton, "spellslot7")
        self.spellslot8 = csheet.findChild(QToolButton, "spellslot8")
        self.spellslot9 = csheet.findChild(QToolButton, "spellslot9")
        self.spellslot10 = csheet.findChild(QToolButton, "spellslot10")

    def update_character_dropdown(self):
        print("Updating Character Dropdown")
        self.character.clear()
        self.client = pymongo.MongoClient(cons.CONNECT)
        self.db = self.client ["dnd"]
        self.collection = self.db["characters"]
        character_list = self.collection.distinct("character")
        self.character.addItems(character_list)

    def update_dictionary(self):
        print("Updating Character Sheet Dictionary")    
        character_sheet_dictionary = {
            "character": self.character.currentText(),
            "rank": "Player",
            "level": self.level.text(),
            "ac": self.ac.text(),
            "init": str(10+int(self.CHA.text())),
            "speed": self.speed.text(),
            "max hp": self.max_hp.text(),
            "current hp": self.current_hp.text(),
            "current morale": self.current_morale.text(),
            "stats": {
                "STR": int(self.STR.text()),
                "DEX": int(self.DEX.text()),
                "CON": int(self.CON.text()),
                "INT": int(self.INT.text()),
                "WIS": int(self.WIS.text()),
                "CHA": int(self.CHA.text())
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
                "inventory11": self.inventory11.text(),
                "inventory12": self.inventory12.text(),
                "inventory13": self.inventory13.text(),
                "inventory14": self.inventory14.text(),
                "inventory15": self.inventory15.text(),
                "inventory16": self.inventory16.text(),
            },            
            "spell slots": { 
                "spell1": self.spellslot1.isChecked(),
                "spell2": self.spellslot2.isChecked(),
                "spell3": self.spellslot3.isChecked(),
                "spell4": self.spellslot4.isChecked(),
                "spell5": self.spellslot5.isChecked(),
                "spell6": self.spellslot6.isChecked(),
                "spell7": self.spellslot7.isChecked(),
                "spell8": self.spellslot8.isChecked(),
                "spell9": self.spellslot9.isChecked(),
                "spell10": self.spellslot10.isChecked(),
            },
            "focus": {
                "focus1": self.focusdice1.isChecked(),
                "focus2": self.focusdice2.isChecked(),
                "focus3": self.focusdice3.isChecked(),
                "focus4": self.focusdice4.isChecked(),
                "focus5": self.focusdice5.isChecked(),
                "focus6": self.focusdice6.isChecked(),
                "focus7": self.focusdice7.isChecked(),
                "focus8": self.focusdice8.isChecked(),
                "focus9": self.focusdice9.isChecked(),
                "focus10": self.focusdice10.isChecked(),
            },
            "feats": {
                "feat1": self.feat1.property("feat"),
                "feat2": self.feat2.property("feat"),
                "feat3": self.feat3.property("feat"),
            }
        }        
        return character_sheet_dictionary
    
    def update_database(self, directory):
        self.client = pymongo.MongoClient(cons.CONNECT)
        self.db = self.client ["dnd"]
        self.collection = self.db["characters"]

        #print(self.character.currentText())

        query = {"character": self.character.currentText()}
        document = self.collection.find_one(query)

        if document is not None:
            new_values = {"$set": directory}
            self.collection.update_one(query, new_values)
        else:
            self.collection.insert_one(directory)

    def update_sheet(self):
        self.set_icon()

        self.check_stats()
        #INVENTORY RULES
        self.strenght()
        self.dexterity()
        self.constitution()
        self.intelligence()
        self.wisdom()
        self.charisma()
        

        self.update_inventory()

        updated_character_sheet = self.update_dictionary()
        self.update_database(updated_character_sheet)

    # ITERATE OVER ITEM JSON TO FIND ITEM
    def check_stats(self):
        #Sum the total stats the character have.
        current_level = self.level.text()
        available_stats = int(current_level) * cons.STATS_PER_LEVEL
        total_stats = int(self.STR.text()) + int(self.DEX.text()) + int(self.CON.text()) + int(self.INT.text()) + int(self.WIS.text()) + int(self.CHA.text())

        stats = available_stats - total_stats

        label = self.csheet.stat_layout.get_title()[1]    

        if stats == 0:
            stat_message = ""
            label.setText(stat_message)
        elif stats < 0:
            stat_message = f"Remove {stats} stat points."
            label.setText(stat_message)
        elif stats > 0:
            stat_message = f"{stats} remaining stat points."
            label.setText(stat_message)

    def update_inventory(self):
        all_items = []

        self.empty_slot_dict = {"Hit":"","Evoke":"","Evoke Mod":["","",""],"Hit Mod":["","",""],"Roll":"","Roll Mod":["","",""]}
        for slot in range(1,cons.MAX_SLOTS+1):
            self.inventory_slot = self.csheet.findChild(QLineEdit, f"inventory{slot}")
            if self.inventory_slot.text() != "":
                all_items.append(self.inventory_slot.text())
            else:
                pass

        for slot in range(1,cons.MAX_SLOTS+1):
            self.update_item(slot, "", "", self.empty_slot_dict)

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
        #stats dictionary
        self.stats_dict = {"":"","AC":1,"STR": int(self.STR.text()), "DEX": int(self.DEX.text()), "CON": int(self.CON.text()), "INT": int(self.INT.text()), "WIS": int(self.WIS.text()), "CHA": int(self.CHA.text())}
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
        #stats dictionary
        self.stats_dict = {"":"","AC":1,"STR": int(self.STR.text()), "DEX": int(self.DEX.text()), "CON": int(self.CON.text()), "INT": int(self.INT.text()), "WIS": int(self.WIS.text()), "CHA": int(self.CHA.text())}
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

    def set_icon(self):
        character_name = self.character.currentText().lower()
        PORTRAIT = f"QLabel {{background-image: url(.icons/{character_name}.png); background-position: center; background-repeat: no-repeat; background-color: {style.DARK_COLOR}; border: 1px solid {style.BORDER_COLOR_LIGHT}; border-radius: {style.RADIUS}}}"	
        self.character_icon.setStyleSheet(PORTRAIT)

    def set_morale(self):
        self.max_morale.setText(f"{cons.BASE_MORALE+int(self.CHA.text())}")
        if self.level == 0:
            self.current_morale.setText(f"{cons.BASE_MORALE+int(self.CHA.text())}")

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
            hp_formula = (cons.HIT_DICE*level) + int(self.CON.text())
        self.max_hp.setText(str(hp_formula))
        

    def adjust_hp(self, state, value):
        current_hp = int(self.current_hp.text())
        self.max_slots = int(self.CON.text())+cons.START_SLOTS

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

        self.update_sheet()

    def remove_injury(self):
        print("remove injury")
        self.empty_slot_dict = {"Hit":"","Evoke":"","Evoke Mod":["","",""],"Hit Mod":["","",""],"Roll":"","Roll Mod":["","",""]}
        self.max_slots = int(self.CON.text())+cons.START_SLOTS
        for slot in range(1,self.max_slots+1):
            widget_slot = self.csheet.findChild(QLineEdit, f"inventory{slot}")
            if widget_slot.text() == "Injury":
                self.update_item(slot, "", "", self.empty_slot_dict)
                return
            else:
                pass

    def add_injury(self):
        self.empty_slot_dict = {"Hit":"","Evoke":"","Evoke Mod":["","",""],"Hit Mod":["","",""],"Roll":"","Roll Mod":["","",""]}
        current_slots = int(self.CON.text())+cons.START_SLOTS
        free_slots = []
        for slot in range(1,current_slots+1):
            widget_slot = self.csheet.findChild(QLineEdit, f"inventory{slot}")
            if widget_slot.text() == "Injury":
                pass
            else:
                free_slots.append(slot)
        if free_slots == []:
            return
        else:
            injury_slot = random.choice(free_slots)
            self.update_item(injury_slot, "Injury", "damage", self.empty_slot_dict)


    def strenght(self):
        print("strenght")
        print(int(self.STR.text()))
        pass 
    def dexterity(self):
        #ac_calculation = str(cons.BASE_AC+math.floor(int(self.DEX)/2))
        ac_calculation = str(cons.BASE_AC+math.floor(int(self.DEX.text())))
        self.ac.setText(ac_calculation)

    def constitution(self):
        for count in range(1,cons.MAX_SLOTS+1):
            for w in [(QToolButton,"icon"),(QPushButton,"evoke"),(QPushButton,"hit_dc"),(QPushButton,"roll"),(QLineEdit,"inventory"),(QLabel,"icon_label"),(QLabel,"inventory_label"),(QLabel,"evoke_label"),(QLabel,"hit_dc_label"),(QLabel,"roll_label")]:
                widget =  self.csheet.findChild(w[0], w[1]+str(count))
                if count <= int(self.CON.text())+cons.START_SLOTS:
                    widget.setEnabled(True)
                else:
                    if w[1] != "icon_label":
                        widget.setText("")
                    widget.setEnabled(False)

    def intelligence(self):
        for count in range(1,11):
            for w in [(QToolButton,"focusdice")]:
                widget =  self.csheet.findChild(w[0], w[1]+str(count))
                if count <= int(self.INT.text()):
                    widget.setEnabled(True)
                else:
                    widget.setEnabled(False)

    def wisdom(self):
        for count in range(1,11):
            for w in [(QToolButton,"spellslot")]:
                widget =  self.csheet.findChild(w[0], w[1]+str(count))
                if count <= int(self.WIS.text()):
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
        self.initiative.setText(f"{int(self.CHA.text())+10} init.")
        self.speed.setText(f"{20+(int(self.CHA.text())*5)} ft.")

    def load_character(self):
        print(f"Loading {self.character.currentText()}")
        if self.character.currentText() == "":
            return
        self.client = pymongo.MongoClient(cons.CONNECT)
        self.db = self.client ["dnd"]
        self.collection = self.db["characters"]

        query = {"character": self.character.currentText()}
        document = self.collection.find_one(query)
        if document != None:
            print(document)
            self.level.setText(str(document["level"]))
            self.current_hp.setText(str(document["current hp"]))
            self.current_morale.setText(str(document["current morale"]))

            self.STR.setText(str(document["stats"]["STR"]))
            self.DEX.setText(str(document["stats"]["DEX"]))
            self.CON.setText(str(document["stats"]["CON"]))
            self.INT.setText(str(document["stats"]["INT"]))
            self.WIS.setText(str(document["stats"]["WIS"]))
            self.CHA.setText(str(document["stats"]["CHA"]))

            self.inventory1.setText(str(document["inventory"]["inventory1"]))
            self.inventory2.setText(str(document["inventory"]["inventory2"]))
            self.inventory3.setText(str(document["inventory"]["inventory3"]))
            self.inventory4.setText(str(document["inventory"]["inventory4"]))
            self.inventory5.setText(str(document["inventory"]["inventory5"]))
            self.inventory6.setText(str(document["inventory"]["inventory6"]))
            self.inventory7.setText(str(document["inventory"]["inventory7"]))
            self.inventory8.setText(str(document["inventory"]["inventory8"]))
            self.inventory9.setText(str(document["inventory"]["inventory9"]))
            self.inventory10.setText(str(document["inventory"]["inventory10"]))
            self.inventory11.setText(str(document["inventory"]["inventory11"]))
            self.inventory12.setText(str(document["inventory"]["inventory12"]))
            self.inventory13.setText(str(document["inventory"]["inventory13"]))
            self.inventory14.setText(str(document["inventory"]["inventory14"]))
            self.inventory15.setText(str(document["inventory"]["inventory15"]))
            self.inventory16.setText(str(document["inventory"]["inventory16"]))

            self.spellslot1.setChecked(document["spell slots"]["spell1"])
            self.spellslot2.setChecked(document["spell slots"]["spell2"])
            self.spellslot3.setChecked(document["spell slots"]["spell3"])
            self.spellslot4.setChecked(document["spell slots"]["spell4"])
            self.spellslot5.setChecked(document["spell slots"]["spell5"])
            self.spellslot6.setChecked(document["spell slots"]["spell6"])
            self.spellslot7.setChecked(document["spell slots"]["spell7"])
            self.spellslot8.setChecked(document["spell slots"]["spell8"])
            self.spellslot9.setChecked(document["spell slots"]["spell9"])
            self.spellslot10.setChecked(document["spell slots"]["spell10"])

            self.focusdice1.setChecked(document["focus"]["focus1"])
            self.focusdice2.setChecked(document["focus"]["focus2"])
            self.focusdice3.setChecked(document["focus"]["focus3"])
            self.focusdice4.setChecked(document["focus"]["focus4"])
            self.focusdice5.setChecked(document["focus"]["focus5"])
            self.focusdice6.setChecked(document["focus"]["focus6"])
            self.focusdice7.setChecked(document["focus"]["focus7"])
            self.focusdice8.setChecked(document["focus"]["focus8"])
            self.focusdice9.setChecked(document["focus"]["focus9"])
            self.focusdice10.setChecked(document["focus"]["focus10"])

            self.update_feat(document["feats"]["feat1"], self.feat1)
            self.update_feat(document["feats"]["feat2"], self.feat2)
            self.update_feat(document["feats"]["feat3"], self.feat3)

            if int(document["current hp"]) >= 0:
                self.current_hp.setStyleSheet(style.BIG_BUTTONS)
            else:
                self.current_hp.setStyleSheet(style.BUTTONS_INJURY)

            if int(document["current morale"]) >= 0:
                self.current_morale.setStyleSheet(style.BIG_BUTTONS)
            else:
                self.current_morale.setStyleSheet(style.BUTTONS_INJURY)

            self.update_sheet()

    def update_feat(self, selected_feat, widget):
        print(f"Updating {selected_feat} in {widget}")
        if selected_feat == "":
            func.set_icon(widget, "",cons.ICON_COLOR)
            widget.setToolTip("")
            widget.setText("")
            widget.setProperty("feat", "")
            return
        
        for feat_dict in os.listdir(cons.FEATURES):
            for feat in json.load(open(os.path.join(cons.FEATURES,feat_dict), "r")):
                if feat["name"] == selected_feat:
                    func.set_icon(widget, feat["icon"],cons.ICON_COLOR)
                    widget.setToolTip(feat["description"])
                    widget.setProperty("feat", feat["name"])
                    return
                
    def get_character(self):
        return self.character_name.get_widget().currentText()




    