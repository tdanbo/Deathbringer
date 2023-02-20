from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import constants as cons

import pymongo

def character_database_collection():
    client = pymongo.MongoClient(cons.CONNECT)
    db = client ["dnd"]
    collection = db["characters"]
    return collection

def character_database_document(character):
    collection = character_database_collection()
    document = collection.find_one({"character": character})
    return document

def character_gui_update(character):
    document = character_database_document(character.get_name())
    character.set_creature_stats(document)



    
