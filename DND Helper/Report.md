# D&D Character Creator - Coursework Report  
**Author:** [Neda Vaitiekūnaitė]  
**Date:** [2025-05-05]  

---

## 1. Introduction  
### a. Application Overview  
The **D&D Character Helper** is a Python terminal application that automates character sheet creation for Dungeons & Dragons 5th Edition. It features:  

- **Rule-accurate character building** (classes, species, backgrounds.)  
- **Interactive CLI interface** with step-by-step guidance on how to create your character.
- **Data exporting** via JSON export.

**Key Components:**  
- Support for all the classes, species and backgrounds that are featured in the official 2024 Player's Handbook.
- Specific class features of a level one adventurer.
- Modifiers, accurate ability score and proficiencies information.

### b. How to Run  
1. Ensure Python is installed.
2. Download these files to a folder(Make sure they're all present):  
   - `main.py`  
   - `character.py`  
   - `builder.py`  
   - `exporter.py`
   - `creator.py`
   - `data/` folder  
3. Run in terminal:  
   ```bash
   python main.py

 ### c. How to Use.
 1. Navigate the main menu and follow the instructions that will be printed onto the terminal screen.
 2. You will choose a class, your species, a background andlanguages by inputing the number of the choice into the terminal, then will be allowed to roll for your ability scores and distribute them however you wish. 
 3. All the related information that was gathered based on your choices will be printed at the very end. You will be able to choose if you'd like the character to be saved on a JSON file.

## 2. Body/Analysis  
### a. OOP Implementation  

#### Polymorphism  
**Definition:** Single interface for multiple forms. 
**Implementation - Export System:**  
```python
class Exporter(ABC):
    @abstractmethod
    def export(self, character, filename):
        pass

class JSONExporter(Exporter):
    def export(self, character, filename):
        data = {
            "Name": character.name,
            "Class": character.character_class['name'],
            "Background": character.background['name'],
            "Species": character.species['name'],
            "Ability Scores": character.ability_scores,
            "Inventory": character._inventory
        }
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Character saved to {filename} (JSON)")

class CSVExporter(Exporter):
    def export(self, character, filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Field", "Value"])
            writer.writerow(["Name", character.name])
            writer.writerow(["Class", character.character_class['name']])
            writer.writerow(["Background", character.background['name']])
            writer.writerow(["Species", character.species['name']])
            for ability, score in character.ability_scores.items():
                writer.writerow([ability, score])
        print(f"Character saved to {filename} (CSV)")
```
#### Abstraction
**Definition:** Hiding complex implementation details, Simplified user interactions.
**Implementation:**
```python
print("\nChoose a background:")
for key, bg in self.backgrounds.items():
    print(f"{key}. {bg['name']} - {', '.join(bg['abilities'])} abilities")
```
#### Inheritance
**Definition:** Base character structure.
**Implementation:**
```python
class BaseCharacter(ABC):
    @abstractmethod
    def display_character_sheet(self): pass

class DnDCharacter(BaseCharacter):
    def display_character_sheet(self):
        print(f"\nNAME: {self.name}")
        print(f"CLASS: {self.character_class['name']}")
```
#### Encapsulation
**Definition:** Protecting internal data. 
**Implementation:**
```python
def __init__(self):
    self._ability_scores = {
        "Strength": 10,
        "Dexterity": 10,
        "Constitution": 10,
        "Intelligence": 10,
        "Wisdom": 10,
        "Charisma": 10
    }

@property
def strength(self):
    return self._ability_scores["Strength"]

@strength.setter
def strength(self, value):
    if 3 <= value <= 18:  
        self._ability_scores["Strength"] = value
```
### b. Design Patterns.
#### Builder Pattern Implementation:
```python
class DnDCharacterBuilder:
    def __init__(self):
        self.character = DnDCharacter()
    
    def set_class(self, character_class):
        self.character.character_class = character_class
        for item in character_class['starting_equipment']:
            if isinstance(item, str):
                self.character.add_to_inventory(item)
        return self
```
### c. Composition Example:
#### Inventory System:
```python
def __init__(self):
    self._inventory = []  
    
def add_to_inventory(self, item):
    if isinstance(item, str):  
        self._inventory.append(item)
    else:
        raise ValueError("Item must be a string")
```

### d. Key Calculations:
### Ability Score Assignment:
```python
rolls = sorted([random.randint(3, 18) for _ in range(6)], reverse=True)
print(f"\nYou rolled: {rolls}")

for i, roll in enumerate(rolls):
    print(f"\nAssign roll {roll} to:")
    for j, ability in enumerate(abilities, 1):
        print(f"{j}. {ability} (current: {temp_scores[ability]})")
    chosen_ability = abilities[int(input("Enter choice: "))-1]
    temp_scores[chosen_ability] = roll
```
### Background Ability Adjustment:
```python
if adjust_choice == "1":
    ability1 = bg_abilities[int(input("Choose +2 ability: "))-1]
    ability_scores[ability1] = min(20, ability_scores[ability1] + 2)
    ability2 = remaining_abilities[int(input("Choose +1 ability: "))-1]
    ability_scores[ability2] = min(20, ability_scores[ability2] + 1)
else:
    for ability in bg_abilities:
        ability_scores[ability] = min(20, ability_scores[ability] + 1)
```
## 3. Results and Summary  
### a. Results:
- Figuring out how to properly impliment all the OOP pillars.
- Picking which of the patterns should be used.
- Figuring out the general idea of DND Character creation and trying to replicate it in code.

### b. Conclusions:
- This project has helped me familiarize myself with the Python programming language and OOP specifically.
- The program can now be used as a helpful and rule accurate character creation tool.

### c. Possible future extensions:
- Add Spellcasting.
- Add Leveling up and all the diffrent class atributes that come with it.
- Add a Graphical UI.

