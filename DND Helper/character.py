import json
from abc import ABC, abstractmethod

PROFICIENCY_BONUS = 2

class BaseCharacter(ABC):
    """Abstraction and Inheritance Pillar"""
    @abstractmethod
    def display_character_sheet(self):
        pass

    @abstractmethod
    def save_to_file(self, filename):
        pass

class DnDCharacter(BaseCharacter):
    """Complete implementation with all property decorators"""
    def __init__(self):
        self._name = ""
        self._character_class = None
        self._background = None
        self._species = None
        self._ability_scores = {
            "Strength": 10, "Dexterity": 10, "Constitution": 10,
            "Intelligence": 10, "Wisdom": 10, "Charisma": 10
        }
        self._ability_modifiers = {k: 0 for k in self._ability_scores}
        self._skill_proficiencies = []
        self._skill_bonuses = {
            "Acrobatics": 0, "Animal Handling": 0, "Arcana": 0,
            "Athletics": 0, "Deception": 0, "History": 0,
            "Insight": 0, "Intimidation": 0, "Investigation": 0,
            "Medicine": 0, "Nature": 0, "Perception": 0,
            "Performance": 0, "Persuasion": 0, "Religion": 0,
            "Sleight of Hand": 0, "Stealth": 0, "Survival": 0
        }
        self._appearance = ""
        self._personality = ""
        self._languages = ["Common"]
        self._inventory = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def character_class(self):
        return self._character_class

    @character_class.setter
    def character_class(self, value):
        self._character_class = value
        self._calculate_skill_bonuses()

    @property
    def background(self):
        return self._background

    @background.setter
    def background(self, value):
        self._background = value
        self._calculate_skill_bonuses()

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        self._species = value

    @property
    def ability_scores(self):
        return self._ability_scores.copy()  

    @ability_scores.setter
    def ability_scores(self, value):
        if all(3 <= v <= 30 for v in value.values()):
            self._ability_scores = value.copy()
            self._calculate_modifiers()
            self._calculate_skill_bonuses()
        else:
            raise ValueError("Ability scores must be between 3-30")

    @property
    def appearance(self):
        return self._appearance

    @appearance.setter
    def appearance(self, value):
        self._appearance = value

    @property
    def personality(self):
        return self._personality

    @personality.setter
    def personality(self, value):
        self._personality = value

    @property
    def languages(self):
        return self._languages.copy()

    @languages.setter
    def languages(self, value):
        if not isinstance(value, list):
            raise ValueError("Languages must be a list")
        if "Common" not in value:
            value.insert(0, "Common")  
        self._languages = value.copy()

    def _calculate_modifiers(self):
        for ability, score in self._ability_scores.items():
            self._ability_modifiers[ability] = (score - 10) // 2

    def _calculate_skill_bonuses(self):
        if not self._character_class or not self._background:
            return

        self._skill_proficiencies = list(
            set(self._character_class['skill_proficiencies'] + 
                self._background['skill_proficiencies'])
        )

        skill_ability_map = {
            "Acrobatics": "Dexterity", "Animal Handling": "Wisdom",
            "Arcana": "Intelligence", "Athletics": "Strength",
            "Deception": "Charisma", "History": "Intelligence",
            "Insight": "Wisdom", "Intimidation": "Charisma",
            "Investigation": "Intelligence", "Medicine": "Wisdom",
            "Nature": "Intelligence", "Perception": "Wisdom",
            "Performance": "Charisma", "Persuasion": "Charisma",
            "Religion": "Intelligence", "Sleight of Hand": "Dexterity",
            "Stealth": "Dexterity", "Survival": "Wisdom"
        }

        for skill, ability in skill_ability_map.items():
            base_bonus = self._ability_modifiers[ability]
            self._skill_bonuses[skill] = base_bonus + (
                PROFICIENCY_BONUS if skill in self._skill_proficiencies else 0
            )

    def display_character_sheet(self):
        """IDENTICAL to your original display method"""
        print("\n=== D&D CHARACTER SHEET ===")
        print(f"\nNAME: {self._name}")
        print(f"CLASS: {self._character_class['name']} (Level 1)")
        print(f"BACKGROUND: {self._background['name']}")
        print(f"SPECIES: {self._species['name']}")
        
        print("\n=== ABILITY SCORES ===")
        for ability, score in self._ability_scores.items():
            modifier = self._ability_modifiers[ability]
            print(f"{ability}: {score} ({'+' if modifier >= 0 else ''}{modifier})")
        
        print("\n=== PROFICIENCIES ===")
        print(f"Proficiency Bonus: +{PROFICIENCY_BONUS}")
        print("\nSaving Throws:")
        for st in self._character_class['saving_throws']:
            print(f" - {st} ({'+' if self._ability_modifiers[st] >= 0 else ''}{self._ability_modifiers[st] + PROFICIENCY_BONUS})")
        
        print("\nSkills:")
        for skill, bonus in self._skill_bonuses.items():
            proficient = "✓" if skill in self._skill_proficiencies else " "
            print(f" [{proficient}] {skill}: {'+' if bonus >= 0 else ''}{bonus}")
        
        print("\nWeapons:", ", ".join(self._character_class['weapon_proficiencies']))
        print("Armor:", ", ".join(self._character_class['armor_training']))
        if self._background['tool_proficiency']:
            print("Tools:", ", ".join(self._background['tool_proficiency']))
        
        print("\n=== FEATURES & TRAITS ===")
        print(f"Background Feature: {self._background['feat']}")
        print("Species Traits:")
        for trait in self._species['traits']:
            print(f" - {trait}")
        if self._species['lineage']:
            print("Lineage Options:", ", ".join(self._species['lineage']))
        
        print("\n=== EQUIPMENT ===")
        print("Class Equipment:")
        for item in self._character_class['starting_equipment']:
            print(f" - {item}")
        print("Background Equipment:")
        for item in self._background['equipment']:
            print(f" - {item}")
        
        print("\n=== LANGUAGES ===")
        print(", ".join(self._languages))
        
        print("\n=== CHARACTER DETAILS ===")
        print(f"Size: {self._species['size']}")
        print(f"Speed: {self._species['speed']} ft")
        print(f"\nAPPEARANCE: {self._appearance}")
        print(f"PERSONALITY: {self._personality}")

    def save_to_file(self, filename):
        """IDENTICAL to your original save method"""
        character_data = {
            "Name": self._name,
            "Class": self._character_class['name'],
            "Background": self._background['name'],
            "Species": self._species['name'],
            "Ability Scores": self._ability_scores,
            "Ability Modifiers": self._ability_modifiers,
            "Skill Proficiencies": self._skill_proficiencies,
            "Skill Bonuses": self._skill_bonuses,
            "Saving Throw Proficiencies": self._character_class['saving_throws'],
            "Weapon Proficiencies": self._character_class['weapon_proficiencies'],
            "Armor Proficiencies": self._character_class['armor_training'],
            "Tool Proficiencies": self._background['tool_proficiency'],
            "Features": {
                "Background": self._background['feat'],
                "Species": self._species['traits']
            },
            "Equipment": {
                "Class": self._character_class['starting_equipment'],
                "Background": self._background['equipment']
            },
            "Languages": self._languages,
            "Size": self._species['size'],
            "Speed": self._species['speed'],
            "Appearance": self._appearance,
            "Personality": self._personality
        }
        
        with open(filename, 'w') as f:
            json.dump(character_data, f, indent=4)
        
        print(f"\nCharacter saved to {filename}")

    def add_to_inventory(self, item):
        """Composition example"""
        self._inventory.append(item)


__all__ = ['DnDCharacter', 'BaseCharacter']  