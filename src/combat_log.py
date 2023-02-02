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
        log_widget_dictionary,
    ):
        self.client = pymongo.MongoClient(cons.CONNECT)
        self.db = self.client ["dnd"]
        self.collection = self.db["combatlog"]
        self.entry = {}

        self.log_widget_dictionary = log_widget_dictionary

    def get_log(self):
        doc = self.collection.find().sort([("_id", -1)]).limit(21)
        json_doc = json.loads(json_util.dumps(doc))
        return list(reversed(json_doc))

    def set_entry(self, character, action_type="", action_name="", hit_desc="", roll_desc="", hit="", roll="", breakdown=""):
        print(f"Adding entry to combat log: {character} rolled {roll}")
        
        self.character = character
        self.action_type = action_type
        self.action_name = action_name
        self.hit_desc = hit_desc
        self.roll_desc = roll_desc
        self.hit = hit
        self.roll = roll
        self.breakdown = breakdown
        self.time = datetime.now()

        entry = {
            "character": self.character,
            "type": self.action_type,
            "name": self.action_name,
            "hit desc": self.hit_desc,
            "roll desc": self.roll_desc,
            "hit": self.hit,
            "roll": self.roll,
            "breakdown": self.breakdown,
            "time": self.time.strftime("%H:%M:%S")
        }

        self.collection.insert_one(entry)

    def start_watching(self):
        self.running = True
        thread = threading.Thread(target=self.watch_collection) 
        thread.start()

    def stop_watching(self):
        self.running = False
        print("Stopped watching combat log")
        
    def watch_collection(self):
        while self.running:
            with self.collection.watch() as change_stream:
                print("Watching collection")
                for update_doc in change_stream:
                    print(update_doc)
                    self.update_combat_log()
        
    def update_combat_log(self):
        print("Updating combat log")
        combat_log = self.get_log()
        for count,entry in enumerate(combat_log):
            character = self.log_widget_dictionary[count]["character"]
            icon = self.log_widget_dictionary[count]["icon"]
            type = self.log_widget_dictionary[count]["type"]
            name = self.log_widget_dictionary[count]["name"]
            hit_desc = self.log_widget_dictionary[count]["hit desc"]
            roll_desc = self.log_widget_dictionary[count]["roll desc"]
            hit = self.log_widget_dictionary[count]["hit"]
            roll = self.log_widget_dictionary[count]["roll"]
            time = self.log_widget_dictionary[count]["time"]
            #breakdown = self.log_widget_dictionary[count]["breakdown"]

            character.setText(entry["character"].capitalize())
            IconImage = QIcon()
            pixmap = QPixmap(os.path.join(cons.ICONS,entry["character"]+".png"))
            icon.setPixmap(pixmap)
            icon.setScaledContents(True)
            type.setText(entry["type"].upper())
            name.setText(entry["name"].upper())
            hit_desc.setText(entry["hit desc"].upper())
            roll_desc.setText(entry["roll desc"].upper())
            hit.setText(str(entry["hit"]))
            roll.setText(str(entry["roll"]))
            time.setText(entry["time"])

            if entry["roll desc"].upper() == "DAMAGE":
                get_updater().call_latest(roll_desc.setStyleSheet, style.COMBAT_LABEL_DAMAGE)
            elif entry["roll desc"].upper() == "HEALING":
                get_updater().call_latest(roll_desc.setStyleSheet, style.COMBAT_LABEL_HEALING)
            elif entry["roll desc"].upper() == "EVOKE":
                get_updater().call_latest(roll_desc.setStyleSheet, style.COMBAT_LABEL_EVOKE)
            else:
                get_updater().call_latest(roll_desc.setStyleSheet, style.COMBAT_LABEL)

            #breakdown.setText(entry["breakdown"])