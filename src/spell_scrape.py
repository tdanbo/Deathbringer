import requests
import json

import constants as cons
import os
import re
from bs4 import BeautifulSoup

'''
This file is not used in the program, but as a seperate scraper. For the spell list
'''

def run_scrape():
    url = 'https://www.aidedd.org/dnd-filters/spells-5e.php'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    spell_table = soup.find('table', {'id': 'liste'})
    rows = spell_table.find_all('tr')

    # Create an empty dictionary to store the spells by school
    spell_schools = ['Abjuration', 'Conjuration', 'Divination', 'Enchantment', 'Evocation', 'Illusion', 'Necromancy', 'Transmutation']
    spell_list = {}

    # Iterate through the rows of the spell table
    for row in rows:
        cells = row.find_all('td')
        if cells:
            spell_name = cells[1].text
            spell_level = cells[2].text
            spell_school = cells[3].text

            # Add the spell to the dictionary, grouping them by school
            if int(spell_level) < 6:           
                spell_list[spell_name] = spell_scrape(spell_name,spell_level,spell_school)

    for school in spell_schools:
        school_list = {}
        for key, value in spell_list.items():
            if value['school'].lower() == school.lower():
                school_list[key] = value

        sorted_data = dict(sorted(school_list.items(), key=lambda item: int(item[1]['level'])))

        with open(os.path.join(cons.ITEMS,f'2_{school.lower()}.json'), 'w') as file:
            json.dump(sorted_data, file, indent=4)

def spell_scrape(spell, level, school):
    spell_name = spell.replace(' ', '-').replace("/", "-").replace("'", "-")
    url = f"https://www.aidedd.org/dnd/sorts.php?vo={spell_name}"

    print(url)

    # Make a request to the website and retrieve the HTML content
    response = requests.get(url)
    html_content = response.content

    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(html_content, "html.parser")

    casting_time = soup.select_one("body > div > div.content > div > div:nth-child(4)").text.strip()
    range = soup.select_one("body > div > div.content > div > div:nth-child(5)").text.strip()
    duration = soup.select_one("body > div > div.content > div > div:nth-child(7)").text.strip()
    description = soup.select_one(".description").text.strip()
    description_clean = description.split("At Higher Levels.")[0]
    description_clean2 = description_clean.split("This spell's damage increase")[0]

    spell_info_dict = spell_info(description_clean2)

    # Print the information
    print(casting_time)
    print(range)
    print(duration)
    print(description_clean2)

    spell_dict = {
        "level": int(level),
        "school": school,
        "casting": casting_time,
        "duration": duration,
        "description": description_clean,
        "Evoke": f"Evoke {10+(int(level)*2)}",
        "Evoke Mod": [
            "INT",
            "WIS"
        ],
        "Hit": spell_info_dict["Hit"],
        "Hit Mod": spell_info_dict["Hit Mod"],
        "Roll": spell_info_dict["Roll"],
        "Roll Mod": spell_info_dict["Roll Mod"]
    }

    return spell_dict

def spell_info(desc):
    print(desc)
    attack_or_save = 'saving throw' if re.search(r'\bsaving throw\b', desc) else 'spell attack' if re.search(r'\bspell attack\b', desc) else ""
    
    saving_throw_types = {
        'Strength': 'STR Save',
        'Dexterity': 'DEX Save',
        'Intellect': 'INT Save',
        'Wisdom': 'WIS Save',
        'Charisma': 'CHA Save',
        'Constitution': 'CON Save'
    }
    
    if attack_or_save == 'saving throw':
        hit_type = next((saving_throw_types[saving_throw] for saving_throw in saving_throw_types if saving_throw in desc), "")
        hit_mod = ["INT"]
    elif attack_or_save == 'spell attack':
        hit_type = "Hit"
        hit_mod = ["INT"]
    else:
        hit_type = ""
        hit_mod = ["", ""]

    type_of_spell = 'Healing' if 'healing' in desc else 'Damage' if 'damage' in desc else ""

    match = re.search(r'\b(\d+)d(\d+)([+-]\d+)?\b', desc)
    if match:
        dice = [match.group(1), "d" + match.group(2), match.group(3)[1:] if match.group(3) else '']
    else:
        dice =  ["","",""]

    return {"Hit":hit_type,"Hit Mod":hit_mod,"Roll":type_of_spell,"Roll Mod":dice}

run_scrape()