import numpy as np
import math
import random
import json 
import pymongo
import constants as cons

class Encounter:
    def __init__(self, level=1, creatures=[]):
        
        #If no creatures are passed, return
        if creatures == []:
            print("No creatures to fight")
            return

        self.creatures = [creature for creature in creatures if creature[1] != "Player"]
        self.players = [creature for creature in creatures if creature[1] == "Player"]
        self.level = level
        self.level_adjustment()
        
        self.creature_stats = []
        self.player_stats = []

        self.update_dict()

        self.hp_pool = self.get_hp_pool()
        self.ac_pool = self.get_ac_pool()
        self.spell_save_pool = self.get_spell_save_pool()
        self.damage_pool = self.get_damage_pool()
        self.hit_pool = self.get_hit_pool()
        self.attack_pool = self.get_attack_pool()


        self.divide_hp()
        self.divide_ac()
        self.divide_spell_save()
        self.divide_passives()
        self.divide_attacks()
        self.divide_hit()
        self.divide_damage()
        self.divide_stats()
        self.divide_movement()

        self.create_attack()

        self.round_stats()

        self.set_player_stats()

    def set_player_stats(self):
        self.client = pymongo.MongoClient(cons.CONNECT)
        self.db = self.client ["dnd"]
        self.collection = self.db["characters"]

        for p in self.player_stats:
            query = {"character": p["type"]}
            character_dict = self.collection.find_one(query)
            print(character_dict)
            p["init"] = int(character_dict["init"])
            p["speed"] = character_dict["speed"]
            p["max hp"] = character_dict["max hp"]
            p["hp"] = character_dict["current hp"]
            p["ac"] = character_dict["ac"]
            p["stats"] = character_dict["stats"]

    def level_adjustment(self):
        self.start_level = self.level
        self.level_max = math.ceil(self.level*0.5)
        if "Leader" in self.creatures:
            self.level += self.level_max
            print(f"This level {self.start_level} fight is adjusted +{self.level_max} ({self.start_level+self.level_max})")    
        else:
            self.level_adjuster = random.randint(0, self.level_max)
            self.level += self.level_adjuster
            print(f"This level {self.start_level} fight is adjusted +{self.level_adjuster} ({self.start_level+self.level_adjuster})")  

    def create_attack(self):

        '''
        The functions below divide all the different attack modifiers on all the creatures. Remember to iterrate over them for the attacks, hit and damage.
        '''

        attack_system = {
            1: {1.0},
            2: {0.75, 0.25},
            3: {0.25, 0.25, 0.50}
        }

        for c in self.creature_stats:
            creature_type = c["type"]
            creature_json = json.load(open(f".creatures/{creature_type.lower()}.json", "r"))
            creature_attacks = c["attacks"]
            creature_damage = c["damage"]
            creature_hit = c["hit"]
            creature_damage_type = c["damage type"]

            attack_distribution = attack_system[creature_attacks]

            print(attack_distribution)

            for attack,multiplier in enumerate(attack_distribution):
                print(attack)

                single_attack_damage = round(creature_damage*multiplier)

                if attack == 0:
                    attack_modifier = random.sample(creature_json["Basic Mod"], k=1)  
                    single_action = {}
                    apply_static = True
                    if attack_modifier == ["Hybrid"]:
                        physical_damage = single_attack_damage*0.25
                        elemental_damage = single_attack_damage*0.75
                        single_action["Primary Type"] = "Physical"
                        single_action["Primary Damage"] = self.damage_convert(physical_damage, static=True)
                        single_action["Secondary Type"] = creature_damage_type
                        single_action["Secondary Damage"] = self.damage_convert(elemental_damage, static=False)
                        single_action["Modifiers"] = attack_modifier
                    else:
                        single_action["Primary Type"] = "Physical"
                        single_action["Primary Damage"] = self.damage_convert(single_attack_damage, static=True)
                        single_action["Secondary Type"] = ""
                        single_action["Secondary Damage"] = ""
                        single_action["Modifiers"] = []

                    c["actions"].append(single_action)

                if attack == 1:
                    single_action = {}
                    attack_modifier = random.sample(creature_json["Elemental Mod"], k=1)

                    single_action["Primary Type"] = creature_damage_type
                    single_action["Primary Damage"] = self.damage_convert(single_attack_damage, static=False)
                    single_action["Secondary Type"] = ""
                    single_action["Secondary Damage"] = ""
                    single_action["Modifiers"] = attack_modifier

                    c["actions"].append(single_action)

                if attack == 2:
                    single_action = {}
                    attack_modifier = random.sample(creature_json["Elemental Mod"], k=2)

                    single_action["Primary Type"] = creature_damage_type
                    single_action["Primary Damage"] = self.damage_convert(single_attack_damage, static=False)
                    single_action["Secondary Type"] = ""
                    single_action["Secondary Damage"] = ""
                    single_action["Modifiers"] = attack_modifier

                    c["actions"].append(single_action)
                
                c["hit"] = creature_hit

    # This function convers average damage numbers in to dice notations. And add their static damage value.
    # Static can be set to False. This will make the attack completely based on dice.
    def damage_convert(self, damage, static=True):
        random_value = int(damage)

        custom_static = 0
        if static == True:
            custom_static = random_value*0.10 # This is just to up the static damage value a bit
            random_value -= round(custom_static)

        while True:
            for dice in [12,10,8,6,4]:
                average = sum(range(0,dice+1))/dice
                division = random_value/average
                if division > 1:
                    if static == False:
                        if division % 1 == 0:
                            dice_count = math.floor(division)
                            static_value = random_value - (dice_count*average)
                            return f"{dice_count}d{dice}"
                    else:
                        if division % 1 > 0.50:                       
                            dice_count = math.floor(division)
                            static_value = random_value - (dice_count*average)
                            return f"{dice_count}d{dice}+{math.floor(static_value+custom_static)}"

            random_value += 0.5    

    def divide_stats(self):
        for c in self.creature_stats:
            stats = {
                "STR":0,
                "DEX":0,
                "CON":0,
                "INT":0,
                "WIS":0,
                "CHA":0,
            }

            creature_type = c["type"]
            creature_json = json.load(open(f".creatures/{creature_type.lower()}.json", "r"))
            stat_pool = self.level*2
            stat_ceil = math.ceil(self.level / 3)

            while stat_pool > 0:
                stat = random.choice(list(stats.keys()))
                if stats[stat] < stat_ceil:
                    stats[stat] += 1
                    stat_pool -= 1

            for weight in creature_json["stats"]:
                stats[weight] += creature_json["stats"][weight]

            c["stats"] = stats
            c["init"] = 10+stats["CHA"]


    def divide_passives(self):
        for c in self.creature_stats:
            creature_type = c["type"]
            creature_json = json.load(open(f".creatures/{creature_type.lower()}.json", "r"))
            if random.choice([True, False]):
                creature_passives = random.sample(list(creature_json["Passives"].keys()), k=1)
                c["passive"] = creature_passives[0]
            else:
                pass

    def divide_attacks(self):
        for c in self.creature_stats:
            attacks = self.attack_pool+random.randint(-1, 1)
            if attacks < 1:
                attacks = 1
            elif attacks > 3:
                attacks = 3
            c["attacks"] = attacks

    def divide_hp(self):
        random_pool = self.hp_pool*0.1

        distribution = {
            "Leader": 1.0,
            "Brute": 1.0,
            "Fighter": 0.50,
            "Specialist": 0.40,            
            "Rogue": 0.30,
            "Ranger": 0.30,
            "Caster": 0.30
        }

        while self.hp_pool > 0:
            for c in self.creature_stats:
                if c["rank"] == "Leader":
                    self.hp_pool -= distribution["Leader"]
                    c["hp"] += distribution["Leader"]
                else:
                    self.hp_pool -= distribution[c["type"]]
                    c["hp"] += distribution[c["type"]]

        while random_pool > 0:
            # Select two random keys
            for c in self.creature_stats:
                random_c = random.choice(self.creature_stats)
                c["hp"] -= 1
                random_c['hp'] += 1
                random_pool -= 1

        for c in self.creature_stats:
            c["max hp"] = c["hp"]

    def divide_damage(self):
        random_pool = self.damage_pool*0.1
        distribution = {
            "Leader": 1.0,
            "Caster": 0.90,
            "Ranger": 0.90,
            "Rogue": 0.80,
            "Fighter": 0.70,
            "Specialist": 0.70,   
            "Brute": 0.60
        }

        while self.damage_pool > 0:
            for c in self.creature_stats:
                if c["rank"] == "Leader":
                    self.damage_pool -= distribution["Leader"]
                    c["damage"] += distribution["Leader"]
                else:
                    self.damage_pool -= distribution[c["type"]]
                    c["damage"] += distribution[c["type"]]

        while random_pool > 0:
            # Select two random keys
            for c in self.creature_stats:
                random_c = random.choice(self.creature_stats)
                c["damage"] -= 1
                random_c['damage'] += 1
                random_pool -= 1

    def divide_ac(self):
        distribution = {
            "Leader": 2,
            "Fighter": 1,
            "Specialist": 0,  
            "Brute": 0,
            "Ranger": -1,
            "Rogue": -2,
            "Caster": -2,
        }

        for c in self.creature_stats:
            if c["rank"] == "Leader":
                dist_stat = distribution["Leader"]
            else:
                dist_stat = distribution[c["type"]]

            if dist_stat > 0:
                modifier = random.randint(0, dist_stat)
            else:
                modifier = random.randint(dist_stat, 0)

            c["ac"] += self.ac_pool+modifier

    def divide_movement(self):
        distribution = {
            "Leader": 40,
            "Rogue": 40,
            "Ranger": 35,
            "Caster": 30,
            "Fighter": 30,
            "Specialist": 25,  
            "Brute": 25   
        }

        base_speed = 30

        for c in self.creature_stats:
            if c["rank"] == "Leader":
                stat = distribution["Leader"]
            else:
                stat = distribution[c["type"]]

            c["speed"] = f"{stat} ft."      

    def divide_spell_save(self):
        distribution = {
            "Leader": 2,
            "Caster": 2,
            "Specialist": 1,  
            "Ranger": 0,
            "Rogue": 0,
            "Fighter": -1,
            "Brute": -2,

        }

        for c in self.creature_stats:
            if c["rank"] == "Leader":
                dist_stat = distribution["Leader"]
            else:
                dist_stat = distribution[c["type"]]

            if dist_stat > 0:
                modifier = random.randint(0, dist_stat)
            else:
                modifier = random.randint(dist_stat, 0)

            c["spell save"] += self.spell_save_pool+modifier      

    def divide_hit(self):
        distribution = {
            "Leader": 2,
            "Specialist": 2,  
            "Rogue": 1,
            "Ranger": 1,       
            "Fighter": 0,
            "Brute": -1,
            "Caster": -2,
        }

        for c in self.creature_stats:
            if c["rank"] == "Leader":
                dist_stat = distribution["Leader"]
            else:
                dist_stat = distribution[c["type"]]

            if dist_stat > 0:
                modifier = random.randint(0, dist_stat)
            else:
                modifier = random.randint(dist_stat, 0)

            c["hit"] += self.hit_pool+modifier    


    def round_stats(self):
        for c in self.creature_stats:
            for key, value in c.items():
                if isinstance(value, float):
                    c[key] = round(value)
        
    def update_dict(self):
        for creature in self.creatures:
            self.creature_stats.append({"icon":creature[0], "init":0, "speed":0, "type":creature[0], "rank":creature[1], "damage type":creature[2] , "passive":"", "stats": {}, "spell save":0, "max hp":0, "hp":0, "ac":0, "damage":0, "hit":0, "attacks":0, "actions": []})

        for player in self.players:
            self.player_stats.append({"icon":player[0], "init":0, "speed":0, "type":player[0], "max hp": 0, "hp":0, "ac":0, "stats": {}, "actions": []})

    '''
    These are all the important scales to adjust the balance of the game. They are all based on a 1-10 scale based on the encounter level.
    '''

    def get_attack_pool(self):
        return self.get_pool(1, 3)

    def get_hp_pool(self):
        return self.get_pool(40, 145)

    def get_damage_pool(self):
        return self.get_pool(15, 75)
    
    def get_ac_pool(self):
        return self.get_pool(14, 16)

    def get_spell_save_pool(self):
        return self.get_pool(10, 18)

    def get_hit_pool(self):
        return self.get_pool(3, 7)

    def get_pool(self, start, end):
        x1, y1 = 1, start
        x19, y19 = 10, end

        m = (y19 - y1) / (x19 - x1)
        b = y1 - m * x1

        x_values = np.arange(0, 25)
        y_values = m * x_values + b
        pool = y_values[self.level]
        return round(pool)
    
    def get_encounter(self):
        combined_stats = self.creature_stats + self.player_stats
        sorted_by_init = sorted(combined_stats, key=lambda x: x['init'], reverse=True)
        return sorted_by_init
