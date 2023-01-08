import os
import random

def roll_dice(sides):
    print(f"Rolling a {sides} sided dice")
    result = random.randint(1, sides)
    print(result)
    return random.randint(1, sides)

def create_folder(dir_path):
    isExist = os.path.exists(dir_path)
    if not isExist:
        os.makedirs(dir_path)
