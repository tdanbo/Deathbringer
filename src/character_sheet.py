from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import pymongo
import constants as cons

import math
import constants as cons
import os
import functions as func

import copy

class CharacterSheet():
    def __init__(self, csheet):
        print("Character Sheet Created")

        self.csheet = csheet

        self.character = ""
        self.level = ""
        self.coins = ""

        self.ac = csheet.findChild(QPushButton, "ac")
        self.initiative = csheet.findChild(QPushButton, "initiative")

        #hp
        self.hp = csheet.findChild(QPushButton, "hp")

        #stats
        self.STR = int(csheet.findChild(QLineEdit, "STR").text())
        self.DEX = int(csheet.findChild(QLineEdit, "DEX").text())
        self.CON = int(csheet.findChild(QLineEdit, "CON").text())
        self.INT = int(csheet.findChild(QLineEdit, "INT").text())
        self.WIS = int(csheet.findChild(QLineEdit, "WIS").text())
        self.CHA = int(csheet.findChild(QLineEdit, "CHA").text())
        
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

        updated_character_sheet = self.update_dictionary()

        #self.update_database(updated_character_sheet)
        self.update_sheet()

    def update_dictionary(self):
        print("Updating Character Sheet Dictionary")    
        character_sheet_dictionary = {
            "character": self.character,
            "level": self.level,
            "coins": self.coins,
            "hp": self.hp.text(),
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
        
        self.set_level()
        self.update_inventory()

    # ITERATE OVER ITEM JSON TO FIND ITEM
    def update_inventory(self):
        all_items = []
        for slot in range(1,cons.MAX_SLOTS+1):
            self.inventory_slot = self.csheet.findChild(QLineEdit, f"inventory{slot}")
            if self.inventory_slot.text() != "":
                all_items.append(self.inventory_slot.text())
                self.update_item(slot, "", "", {"Action":"","Modifier":""})
            else:
                self.update_item(slot, "", "", {"Action":"","Modifier":""})

        misc_items = copy.deepcopy(all_items)
        slot = 1
        for item_type in os.listdir(cons.ITEMS):
            item_type_json = func.read_json(os.path.join(cons.ITEMS,item_type))
            for item in all_items:
                for item_key in item_type_json:
                    if item_key.lower() == item.lower():
                        self.update_item(slot, item_key, item_type.split(".")[0].split("_")[1], item_type_json[item_key])
                        misc_items.remove(item)
                        slot += 1

        print(misc_items)

        for item in misc_items:
            self.update_item(slot, item, "Misc", {"Action":"","Modifier":""})
            all_items.remove(item)
            slot += 1

    def update_item(self, slot, item, inventory_type, inventory_item):
        self.inventory_slot = self.csheet.findChild(QLineEdit, f"inventory{slot}")
        self.inventory_icon = self.csheet.findChild(QToolButton, f"icon{slot}")
        self.inventory_action = self.csheet.findChild(QPushButton, f"action{slot}")
        self.inventory_modifier = self.csheet.findChild(QLineEdit, f"modifier{slot}")

        func.set_icon(self.inventory_icon,f"{inventory_type}.png",cons.ICON_COLOR)
        self.inventory_action.setText(inventory_type.capitalize())
        self.inventory_modifier.setText(inventory_item["Modifier"])
        self.inventory_slot.setText(item)

    def set_level(self):
        widget =  self.csheet.stat_layout.get_label()
        ranks = {
            0: "Soul",
            1: "Squire",
            2: "Page",
            3: "Adventurer",
            4: "Explorer",
            5: "Soldier",
            6: "Warrior",
            7: "Vanquisher",
            8: "Champion",
            9: "Guardian",
            10: "Legend"
            }

        stats_per_level = 3
        all_stats = self.STR + self.DEX + self.CON + self.INT + self.WIS + self.CHA
        level = math.floor(all_stats//stats_per_level)
        widget.setText(f"{ranks[level]} - Level {level}".upper())
        self.current_level = level
        # THIS WILL HAPPEN WHEN A CHARACTER LEVELS UP
        self.set_hp()
        

    def set_hp(self):
        hp_formula = (3*self.current_level) + self.CON
        self.hp.setText(str(hp_formula))

    def strenght(self):
        pass 
    def dexterity(self):
        pass
    def constitution(self):
        for count in range(1,cons.MAX_SLOTS+1):
            for w in [(QToolButton,"icon"),(QPushButton,"action"),(QLineEdit,"modifier"),(QLineEdit,"inventory")]:#
                widget =  self.csheet.findChild(w[0], w[1]+str(count))
                if count <= self.CON+6:
                    widget.setEnabled(True)
                else:
                    widget.setEnabled(False)

    def intelligence(self):
        for count in range(1,11):
            for w in [(QToolButton,"corruption")]:
                widget =  self.csheet.findChild(w[0], w[1]+str(count))
                if count <= self.INT:
                    widget.setEnabled(True)
                else:
                    widget.setEnabled(False)

    def wisdom(self):
        for count in range(1,11):
            for w in [(QToolButton,"herodice")]:
                widget =  self.csheet.findChild(w[0], w[1]+str(count))
                if count <= self.WIS:
                    widget.setEnabled(True)
                else:
                    widget.setEnabled(False)

    def charisma(self):
        initiative_widget = self.csheet.findChild(QPushButton, "initiative")
        initiative_widget.setText(str(self.CHA+10))

    