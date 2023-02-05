import constants as cons

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import stylesheet as style
import random

from character_sheet import CharacterSheet
from combat_log import CombatLog

from pymongo import MongoClient
from bson.objectid import ObjectId

def show_reroll(self,dictionary,slot_type,slot):
    print("Rerolling")
    print(slot)

    combat_log = CombatLog(dictionary)

    entry = combat_log.get_log()[slot]
    collection = combat_log.get_collection()

    oid = ObjectId(entry["_id"]['$oid'])

    if slot_type == "hit":     
        update_result = collection.update_one({"_id": oid}, {"$set": {"show reroll hit": True}})
    else:
        update_result = collection.update_one({"_id": oid}, {"$set": {"show reroll roll": True}})

    combat_log.update_combat_log()