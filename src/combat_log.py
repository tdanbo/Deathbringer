from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

from qt_thread_updater import get_updater

import pymongo
import os
import constants as cons
from datetime import datetime
from bson import json_util
import json
import threading
import stylesheet as style

class CombatLog:
    def __init__(
        self,
        combat_log_gui
    ):
        self.combat_log_gui = combat_log_gui
        self.client = pymongo.MongoClient(cons.CONNECT)
        self.db = self.client ["dnd"]
        self.collection = self.db["combatlog"]
        self.entry = {}

    def get_log(self):
        doc = self.collection.find().sort([("_id", -1)]).limit(21)
        json_doc = json.loads(json_util.dumps(doc))
        return list(json_doc)
        
    def set_entry(
        self,
        character, 
        action_name, 
        action_dice,
        # hit
        first_hit,
        second_hit, 
        desc_hit, 
        double_breakdown,
        # roll
        first_roll,
        second_roll,
        roll_desc, 
        single_breakdown
    ):

        entry = {
            "character": character,
            "action name": action_name,
            "action dice": action_dice,
            "first hit": first_hit,
            "second hit": second_hit,
            "desc hit": desc_hit,
            "double breakdown": double_breakdown,
            "first roll": first_roll,
            "second roll": second_roll,
            "desc roll": roll_desc,
            "single breakdown": single_breakdown,
            "time": datetime.now().strftime("%H:%M:%S"),
            "show reroll hit": False,
            "show reroll roll": False
        }

        self.collection.insert_one(entry)

    def get_collection(self):
        return self.collection

    def start_watching(self):
        self.running = True
        thread = threading.Thread(target=self.watch_collection) 
        thread.start()

    def stop_watching(self):
        self.running = False
        
    def watch_collection(self):
        while self.running:
            with self.collection.watch() as change_stream:
                print("Watching collection")
                for update_doc in change_stream:
                    self.update_combat_log()
        
    def update_combat_log(self):
        print("Updating combat log")
        combat_log = self.get_log()
        for count,entry in enumerate(combat_log):
            character = self.combat_log_gui.findChild(QLabel,"character"+str(count))
            icon = self.combat_log_gui.findChild(QLabel,"icon"+str(count))
            action_name = self.combat_log_gui.findChild(QLabel,"action name"+str(count))
            action_dice = self.combat_log_gui.findChild(QLabel,"action dice"+str(count))

            first_hit = self.combat_log_gui.findChild(QLabel,"first hit"+str(count))
            second_hit = self.combat_log_gui.findChild(QLabel,"second hit"+str(count))
            desc_hit = self.combat_log_gui.findChild(QPushButton,"desc hit"+str(count))

            first_roll = self.combat_log_gui.findChild(QLabel,"first roll"+str(count))
            second_roll = self.combat_log_gui.findChild(QLabel,"second roll"+str(count))
            desc_roll = self.combat_log_gui.findChild(QPushButton,"desc roll"+str(count))

            time = self.combat_log_gui.findChild(QLabel,"time"+str(count))

            single_breakdown = entry["single breakdown"]
            double_breakdown = entry["double breakdown"]

            character.setText(entry["character"].capitalize())
            IconImage = QIcon()
            pixmap = QPixmap(os.path.join(cons.ICONS,entry["character"]+".png"))
            icon.setPixmap(pixmap)
            icon.setScaledContents(True)
            action_name.setText(str(entry["action name"]).upper())
            action_dice.setText(single_breakdown["first"]["dice breakdown"])

            first_hit.setText(str(entry["first hit"]))
            first_hit.setToolTip(double_breakdown["first"]["result breakdown"])

            desc_hit.setText(entry["desc hit"].upper())

            first_roll.setText(str(entry["first roll"]))
            first_roll.setToolTip(single_breakdown["first"]["result breakdown"])

            desc_roll.setText(entry["desc roll"].upper())

            # SET THE REROLL TEXT IF REROLL IS TRUE!
            if entry["show reroll hit"] == True:
                second_hit.setText(str(entry["second hit"]))
                second_hit.setToolTip(double_breakdown["second"]["result breakdown"])
            else:
                second_hit.setText("")
                second_hit.setToolTip("")

            if entry["show reroll roll"] == True:
                second_roll.setText(str(entry["second roll"]))
                second_roll.setToolTip(single_breakdown["second"]["result breakdown"])
            else:
                second_roll.setText("")
                second_roll.setToolTip("")

            time.setText(entry["time"])

            if entry["desc roll"].upper() == "DAMAGE":
                get_updater().call_latest(desc_roll.setStyleSheet, style.COMBAT_LABEL_DAMAGE)
            elif entry["desc roll"].upper() == "HEALING":
                get_updater().call_latest(desc_roll.setStyleSheet, style.COMBAT_LABEL_HEALING)
            elif entry["desc roll"].upper() == "CUSTOM":
                get_updater().call_latest(desc_roll.setStyleSheet, style.COMBAT_LABEL_CUSTOM)
            elif entry["desc roll"].upper() == "CHECK":
                get_updater().call_latest(desc_roll.setStyleSheet, style.COMBAT_LABEL_CHECK)
            elif "EVOKE" in entry["desc roll"].upper():
                get_updater().call_latest(desc_roll.setStyleSheet, style.COMBAT_LABEL_EVOKE)
            else:
                get_updater().call_latest(desc_roll.setStyleSheet, style.COMBAT_LABEL)
