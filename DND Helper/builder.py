from character import DnDCharacter  

class Inventory:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)

class DnDCharacterBuilder:
    def __init__(self):
        self._character = DnDCharacter()  
        self._inventory = Inventory()     

    def set_name(self, name):
        self._character.name = name
        return self
    
    def set_class(self, character_class):
        self._character.character_class = character_class
        # Add class equipment to inventory
        for item in character_class['starting_equipment']:
            self._character.add_to_inventory(item)
        return self

    def set_background(self, background):
        self._character.background = background
        # Add background equipment to inventory
        for item in background['equipment']:
            self._character.add_to_inventory(item)
        return self

    def set_species(self, species):
        self._character.species = species
        return self

    def set_ability_scores(self, ability_scores):
        self._character.ability_scores = ability_scores
        return self

    def set_appearance(self, appearance):
        self._character.appearance = appearance
        return self

    def set_personality(self, personality):
        self._character.personality = personality
        return self

    def add_custom_item(self, item):
        """Composition example"""
        self._character.add_to_inventory(item)
        return self

    def build(self):
        """Final build method"""
        return self._character
    
    def set_languages(self, languages):
        """Sets character's languages with validation"""
        if not isinstance(languages, list):
            raise ValueError("Languages must be a list")
        if "Common" not in languages:
            languages.insert(0, "Common")  
        self._character.languages = languages
        return self
    
    from character import DnDCharacter

class DnDCharacterBuilder:
    def __init__(self):
        self.character = DnDCharacter()  
        self.inventory = []

    def set_name(self, name):
        self.character.name = name
        return self
    
    def set_class(self, character_class):
        self.character.character_class = character_class
        return self
    
    def set_background(self, background):
        self.character.background = background
        return self
    
    def set_species(self, species):
        self.character.species = species
        return self
    
    def set_languages(self, languages):
        self.character.languages = languages
        return self
    
    def set_ability_scores(self, ability_scores):
        self.character.ability_scores = ability_scores
        return self
    
    def set_appearance(self, appearance):
        self.character.appearance = appearance
        return self
    
    def set_personality(self, personality):
        self.character.personality = personality
        return self
    
    def get_character(self):  
        return self.character
