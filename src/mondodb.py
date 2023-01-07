import pymongo
import constants as cons

client = pymongo.MongoClient(cons.CONNECT)
db = client["combat"]
collection = db["log"]

dictionary = {"name": "John", "age": 36, "country": "Norway"}

collection.insert_one(dictionary)

print(collection)