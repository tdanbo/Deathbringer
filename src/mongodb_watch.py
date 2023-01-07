import pymongo
import constants as cons

def watch_collection(client, database_name, collection_name):
    # Select the database and collection
    db = client[database_name]
    collection = db[collection_name]

    # Set up the change stream
    change_stream = collection.watch()

    # Iterate over the change stream indefinitely
    while True:
        for change in change_stream:
            print(change)

# Connect to the database
client = pymongo.MongoClient(cons.CONNECT)

# Start watching the collection
watch_collection(client, "combat", "log")