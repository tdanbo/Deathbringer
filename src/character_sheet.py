from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import pymongo
import constants as cons

class CharacterSheet():
    def __init__(self, csheet):
        self.csheet = csheet

        self.character = ""
        self.level = ""
        self.coins = ""
        self.hp = csheet.findChild(QLineEdit, "hp")
        self.ac = csheet.findChild(QPushButton, "ac")
        self.initiative = csheet.findChild(QPushButton, "initiative")

        #all inventory slots
        self.inventory1 = csheet.findChild(QComboBox, "inventory1")
        self.inventory2 = csheet.findChild(QComboBox, "inventory2")
        self.inventory3 = csheet.findChild(QComboBox, "inventory3")
        self.inventory4 = csheet.findChild(QComboBox, "inventory4")
        self.inventory5 = csheet.findChild(QComboBox, "inventory5")
        self.inventory6 = csheet.findChild(QComboBox, "inventory6")
        self.inventory7 = csheet.findChild(QComboBox, "inventory7")
        self.inventory8 = csheet.findChild(QComboBox, "inventory8")
        self.inventory9 = csheet.findChild(QComboBox, "inventory9")
        self.inventory10 = csheet.findChild(QComboBox, "inventory10")
        self.inventory11 = csheet.findChild(QComboBox, "inventory11")
        self.inventory12 = csheet.findChild(QComboBox, "inventory12")
        self.inventory13 = csheet.findChild(QComboBox, "inventory13")
        self.inventory14 = csheet.findChild(QComboBox, "inventory14")
        self.inventory15 = csheet.findChild(QComboBox, "inventory15")
        self.inventory16 = csheet.findChild(QComboBox, "inventory16")
        self.inventory17 = csheet.findChild(QComboBox, "inventory17")
        self.inventory18 = csheet.findChild(QComboBox, "inventory18")
        self.inventory19 = csheet.findChild(QComboBox, "inventory19")
        self.inventory20 = csheet.findChild(QComboBox, "inventory20")

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

        #stats
        self.str = csheet.findChild(QSpinBox, "STR")
        self.dex = csheet.findChild(QSpinBox, "DEX")
        self.con = csheet.findChild(QSpinBox, "CON")
        self.int = csheet.findChild(QSpinBox, "INT")
        self.wis = csheet.findChild(QSpinBox, "WIS")
        self.cha = csheet.findChild(QSpinBox, "CHA")

        updated_character_sheet = self.update_dictionary()

        #self.update_database(updated_character_sheet)
        self.update_sheet()

    def update_dictionary(self):    
        character_sheet_dictionary = {
            "character": self.character,
            "level": self.level,
            "coins": self.coins,
            "hp": self.hp.text(),
            "ac": self.ac.text(),
            "initiative": self.initiative.text(),
            "stats": {
                "str": self.str.value(),
                "dex": self.dex.value(),
                "con": self.con.value(),
                "int": self.int.value(),
                "wis": self.wis.value(),
                "cha": self.cha.value(),
            },
            "inventory": {
                "inventory1": self.inventory1.currentText(),
                "inventory2": self.inventory2.currentText(),
                "inventory3": self.inventory3.currentText(),
                "inventory4": self.inventory4.currentText(),
                "inventory5": self.inventory5.currentText(),
                "inventory6": self.inventory6.currentText(),
                "inventory7": self.inventory7.currentText(),
                "inventory8": self.inventory8.currentText(),
                "inventory9": self.inventory9.currentText(),
                "inventory10": self.inventory10.currentText(),
                "inventory11": self.inventory1.currentText(),
                "inventory12": self.inventory2.currentText(),
                "inventory13": self.inventory3.currentText(),
                "inventory14": self.inventory4.currentText(),
                "inventory15": self.inventory5.currentText(),
                "inventory16": self.inventory6.currentText(),
                "inventory17": self.inventory7.currentText(),
                "inventory18": self.inventory8.currentText(),
                "inventory19": self.inventory9.currentText(),
                "inventory20": self.inventory10.currentText(),
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
        self.strenght(self.str.value())
        self.dexterity(self.dex.value())
        self.constitution(self.con.value())
        self.intelligence(self.int.value())
        self.wisdom(self.wis.value())
        self.charisma(self.cha.value())
        
    def strenght(self, stat_value):
        pass
    def dexterity(self, stat_value):
        pass
    def constitution(self, stat_value):
        for count in range(1,21):
            for w in [(QPushButton,"selector"),(QPushButton,"action"),(QLineEdit,"modifier"),(QComboBox,"inventory")]:#
                print(w)
                widget =  self.csheet.findChild(w[0], w[1]+str(count))
                if count <= stat_value+10:
                    widget.setEnabled(True)
                else:
                    widget.setEnabled(False)

    def intelligence(self, stat_value):
        for count in range(1,11):
            for w in [(QToolButton,"corruption")]:
                widget =  self.csheet.findChild(w[0], w[1]+str(count))
                if count <= stat_value:
                    widget.setEnabled(True)
                else:
                    widget.setEnabled(False)

    def wisdom(self, stat_value):
        for count in range(1,11):
            for w in [(QToolButton,"herodice")]:
                widget =  self.csheet.findChild(w[0], w[1]+str(count))
                if count <= stat_value:
                    widget.setEnabled(True)
                else:
                    widget.setEnabled(False)

    def charisma(self, stat_value):
        initiative_widget = self.csheet.findChild(QPushButton, "initiative")
        initiative_widget.setText(str(stat_value+10))

    