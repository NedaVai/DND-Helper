from builder import DnDCharacterBuilder
from creator import CharacterCreator

if __name__ == "__main__":
    print("=== D&D Character Creator ===")
    builder = DnDCharacterBuilder()  
    creator = CharacterCreator(builder)
    creator.show_main_menu()