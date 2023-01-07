import pymongo
import constants as cons

client = pymongo.MongoClient(cons.CONNECT)
db = client["combat"]
collection = db["log"]

dictionary = {"name": "Tobias", "age": 34, "country": "Denmark", "pervert": True}

collection.insert_one(dictionary)

print(collection)