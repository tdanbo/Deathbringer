import pymongo
import constants as cons
from datetime import datetime
from bson import json_util
import json

class CombatLog:
    def __init__(
        self,
    ):
        self.client = pymongo.MongoClient(cons.CONNECT)
        self.db = self.client ["combat"]
        self.collection = self.db["log"]
        self.entry = {}

    def get_log(self):
        doc = self.collection.find().sort([("_id", -1)]).limit(11)
        json_doc = json.loads(json_util.dumps(doc))
        return list(reversed(json_doc))

    def set_entry(self, character, roll, rolltype="Custom"):
        print(f"Adding entry to combat log: {character} rolled {roll}")
        now = datetime.now()
        entry = {
            "character": character,
            "roll": roll,
            "type": rolltype,
            "time": now.strftime("%d/%m/%Y %H:%M")
        }
        self.collection.insert_one(entry)