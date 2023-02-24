import os
import json
for i in os.listdir("./.items"):
    if "2_" in i:
        json_file = json.load(open(os.path.join("./.items", i), "r"))
        description_json = {}
        for test in json_file:
            
            for key, value in json_file[test].items():
                description_json[test] = json_file[test]["description"]
            json.dump(description_json, open(os.path.join("./.descriptions", i), "w"), indent=4)

        