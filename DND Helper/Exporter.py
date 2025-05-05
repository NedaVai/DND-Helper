import json
import csv
from abc import ABC, abstractmethod

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

def export_character(character):
    """Factory Method Pattern"""
    print("\nChoose export format:")
    print("1. JSON")
    print("2. CSV")
    choice = input("Enter your choice: ")
    
    filename = input("Enter filename (without extension): ")
    
    if choice == "1":
        exporter = JSONExporter()
        exporter.export(character, filename + ".json")
    elif choice == "2":
        exporter = CSVExporter()
        exporter.export(character, filename + ".csv")
    else:
        print("Invalid choice")