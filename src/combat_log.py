import pymongo
import constants as cons
from bson import json_util
import json

class CombatLog:
    def __init__(self):
        self.client = pymongo.MongoClient(cons.CONNECT)
        self.db = self.client ["combat"]
        self.collective = self.db["log"]
        self.entry = {}

    def get_log(self):
        doc = self.collective.find_one()
        json_doc = json.loads(json_util.dumps(doc))
        return json_doc

    def write_entry(self):
        collection.insert_one(self.entry)