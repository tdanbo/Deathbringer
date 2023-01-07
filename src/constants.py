
import functions as func
import os




SCRIPT_NAME = "Deathbringer App"
LOCAL_DIRECTORY = os.path.join(os.getenv("APPDATA"), SCRIPT_NAME)
VERSION = "0.0.1"
USER = "test-user"
PASSWORD = "7kHYdt9kna9d9w3t" 
CONNECT = f"mongodb+srv://{USER}:{PASSWORD}@cluster0.2oqhlud.mongodb.net/?retryWrites=true&w=majority"
SETTINGS = os.path.join(LOCAL_DIRECTORY, "settings.json")

func.create_folder(LOCAL_DIRECTORY)
