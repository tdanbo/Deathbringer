import constants as cons

from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


from combat_log import CombatLog

from bson.objectid import ObjectId

def show_reroll(CombatLogGui,slot_type,slot):
    print("Rerolling")

    combat_log = CombatLog(CombatLogGui)

    entry = combat_log.get_log()[slot]
    collection = combat_log.get_collection()

    oid = ObjectId(entry["_id"]['$oid'])

    if slot_type == "hit":     
        update_result = collection.update_one({"_id": oid}, {"$set": {"show reroll hit": True}})
    else:
        update_result = collection.update_one({"_id": oid}, {"$set": {"show reroll roll": True}})

    combat_log.update_combat_log()