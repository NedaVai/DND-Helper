import unittest
from character import DnDCharacter
from data import classes, backgrounds

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = DnDCharacter()
        self.character.character_class = classes['1']  
        self.character.background = backgrounds['1']   
        self.character.ability_scores = {
            "Strength": 16,
            "Dexterity": 12,
            "Constitution": 14,
            "Intelligence": 10,
            "Wisdom": 12,
            "Charisma": 8
        }

    def test_class_assignment(self):
        self.assertEqual(self.character.character_class['name'], "Barbarian")
        self.assertEqual(self.character.character_class['hit_die'], "d12")

    def test_background_assignment(self):
        self.assertEqual(self.character.background['name'], "Acolyte")
        self.assertIn("Calligrapher's Supplies", self.character.background['tool_proficiency'])

    def test_ability_score_storage(self):
        self.assertEqual(self.character.ability_scores["Strength"], 16)
        self.assertEqual(self.character.ability_scores["Charisma"], 8)

    def test_inventory_management(self):
        initial_count = len(self.character._inventory)
        self.character.add_to_inventory("Greataxe")
        self.assertEqual(len(self.character._inventory), initial_count + 1)
        self.assertIn("Greataxe", self.character._inventory)

if __name__ == '__main__':
    unittest.main()