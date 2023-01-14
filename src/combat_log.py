from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import pymongo
import os
import constants as cons
from datetime import datetime
from bson import json_util
import json
import threading

class CombatLog:
    def __init__(
        self,
        log_widget_dictionary,
    ):
        self.client = pymongo.MongoClient(cons.CONNECT)
        self.db = self.client ["combat"]
        self.collection = self.db["log"]
        self.entry = {}

        self.log_widget_dictionary = log_widget_dictionary

    def get_log(self):
        doc = self.collection.find().sort([("_id", -1)]).limit(21)
        json_doc = json.loads(json_util.dumps(doc))
        return list(reversed(json_doc))

    def set_entry(self, character, roll, roll_type, roll_breakdown):
        print(f"Adding entry to combat log: {character} rolled {roll}")
        now = datetime.now()
        entry = {
            "character": character,
            "roll": roll,
            "type": roll_type,
            "breakdown": roll_breakdown,
            "time": now.strftime("%d/%m/%Y %H:%M")
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
            breakdown = self.log_widget_dictionary[count]["breakdown"]
            roll = self.log_widget_dictionary[count]["roll"]
            time = self.log_widget_dictionary[count]["time"]

            character.setText(entry["character"].capitalize())
            IconImage = QIcon(os.path.join(cons.ICONS,entry["character"]+".png"))
            icon.setIcon(IconImage)
            icon.setIconSize(QSize(40, 40))
            type.setText(entry["type"].upper())
            breakdown.setText(entry["breakdown"])
            roll.setText(str(entry["roll"]))
            time.setText(entry["time"])