import unittest
from builder import DnDCharacterBuilder
from data import classes, backgrounds

class TestBuilder(unittest.TestCase):
    def setUp(self):
        self.builder = DnDCharacterBuilder()
        self.barbarian = classes['1']
        self.acolyte = backgrounds['1']

    def test_barbarian_creation(self):
        character = (self.builder
                    .set_class(self.barbarian)
                    .set_background(self.acolyte)
                    .get_character())
        
        self.assertEqual(character.character_class['name'], "Barbarian")
        self.assertEqual(character.background['name'], "Acolyte")
        self.assertIn("Rage", character.character_class['class_features_lv1'])

    def test_equipment_selection(self):
        self.builder.set_class(self.barbarian)
        character = self.builder.get_character()

        self.assertTrue(any("Choose A or B" in item for item in character.character_class['starting_equipment']))
        self.assertTrue(any("Greataxe" in item for item in character.character_class['starting_equipment']))

    def test_background_features(self):
        character = (self.builder
                    .set_background(self.acolyte)
                    .get_character())
        
        self.assertEqual(character.background['feat'], "Magic Initiate")
        self.assertIn("Holy Symbol", character.background['equipment'])

if __name__ == '__main__':
    unittest.main()