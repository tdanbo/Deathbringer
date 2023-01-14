class CharacterSheet:
    def __init__(self, character_dictionary = {}):
        print("Creating character sheet")
        self.character_dictionary = character_dictionary

    def update(self):
        print("Updating character sheet")
        CharacterSheetGUI.character_ac_widget.widget().setText("10")