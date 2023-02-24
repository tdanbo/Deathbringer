import PyPDF2
import re
import os
import json
# Open the PDF file
def read_pdf():
    pdf_file = open('./.files/all_spells2.pdf', 'rb')


    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    line_list = []
    for page in pdf_reader.pages:
        lines = page.extract_text()

        sections = re.split(r'([A-Z]\n\d{3})', lines)

        # Remove empty strings and None values from the list
        sections = [s for s in sections if s is not None and s != '']

        # Print the resulting sections
        for section in sections:
            line = section.strip()
            split = line.split("\n")
            if len(split) in [8,9]:
                if len(split) == 8:
                    split.insert(0, "0")
                line_list.append(split)

    spell_dict = {}
    for line in line_list:
        if int(line[0]) < 6:
            spell_dict[line[1]] = {
            "level": int(line[0]),
            "description": clean_description(line[2]),
            "save": line[3],
            "school": line[4],
            "casting": line[5],
            "range": line[6],
            "duration": line[8],
            "Evoke": f"Evoke {10+(int(int(line[0]))*2)}",
            "Evoke Mod": [
                "INT",
                "WIS"
            ]}

    sorted_data = dict(sorted(spell_dict.items(), key=lambda item: int(item[1]['level'])))
    with open(os.path.join('2_spells.json'), 'w') as file:
        json.dump(sorted_data, file, indent=4)

def clean_description(description):

    char_to_replace = {
        'crea': 'creature', 
        'bns a': 'bonus action', 
        'atk': 'attack',
        "wea": "weapon",
        "/SL": "",
        "creatureture": "creature",
        "weaponpon": "weapon",
    }

    # Iterate over all key-value pairs in dictionary 
    for key, value in char_to_replace.items():
        # Replace key character with value character in string
        description = description.replace(key, value)

    remove_cl = description.split(";")
    new_string = []
    
    for i in remove_cl:
        if "CL" in i:
            pass
        else:
            new_string.append(i)

    joined_string = ';'.join(new_string)

    words = joined_string.split()

    for i in range(len(words)):
        if "+" in words[i]:

            split_word = words[i].split("+")
            if len(split_word) > 2:
                print(words)
                split_word[:-1]
                words[i] = "".join(split_word)
            else:
                pass


    new_s = " ".join(words)
    return new_s

read_pdf()

