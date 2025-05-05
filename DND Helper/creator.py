import random
from data import classes, backgrounds, species, language_options
from builder import DnDCharacterBuilder

class CharacterCreator:
    def __init__(self, builder):
        self.builder = builder
        self.classes = classes
        self.backgrounds = backgrounds
        self.species = species
        self.language_options = [lang for lang in language_options if lang != "Common"]  

    def show_main_menu(self):
        while True:
            print("\n=== D&D CHARACTER CREATOR ===")
            print("1. New Character")
            print("2. Edit Character")
            print("3. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.create_new_character()
            elif choice == "2":
                print("Edit functionality not implemented yet.")
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def create_new_character(self):
        print("\n=== CREATE NEW CHARACTER ===")
        
        # 1. Name Selection
        name = input("\nEnter your character's name: ")
        self.builder.set_name(name)
        
        # 2. Class Selection
        print("\nChoose a class:")
        for key, cls in self.classes.items():
            print(f"{key}. {cls['name']} - {cls['primary_ability']} primary, HD: {cls['hit_die']}")
        
        class_choice = input("Enter your choice: ")
        while class_choice not in self.classes:
            print("Invalid choice. Please try again.")
            class_choice = input("Enter your choice: ")
        
        self.builder.set_class(self.classes[class_choice])
        
        # 3. Background Selection
        print("\nChoose a background:")
        for key, bg in self.backgrounds.items():
            print(f"{key}. {bg['name']} - {', '.join(bg['abilities'])} abilities")
        
        bg_choice = input("Enter your choice: ")
        while bg_choice not in self.backgrounds:
            print("Invalid choice. Please try again.")
            bg_choice = input("Enter your choice: ")
        
        self.builder.set_background(self.backgrounds[bg_choice])
        
        # 4. Species Selection
        print("\nChoose a species:")
        for key, sp in self.species.items():
            traits = ', '.join([t.split('(')[0].strip() for t in sp['traits'][:2]])
            print(f"{key}. {sp['name']} - {sp['size']}, {sp['speed']}ft, {traits}")
        
        sp_choice = input("Enter your choice: ")
        while sp_choice not in self.species:
            print("Invalid choice. Please try again.")
            sp_choice = input("Enter your choice: ")
        
        self.builder.set_species(self.species[sp_choice])
        
        # 5. Language Selection
        print("\n=== LANGUAGES ===")
        print("You automatically know Common.")
        print("Choose 2 additional languages:")
        
        for i, lang in enumerate(self.language_options, 1):
            print(f"{i}. {lang}")
        
        languages = ["Common"]
        while len(languages) < 3:
            try:
                choice = int(input(f"Choose language {len(languages)} (1-{len(self.language_options)}): "))
                if 1 <= choice <= len(self.language_options):
                    selected_lang = self.language_options[choice-1]
                    if selected_lang not in languages:
                        languages.append(selected_lang)
                    else:
                        print("You already chose that language!")
                else:
                    print(f"Please enter a number between 1 and {len(self.language_options)}")
            except ValueError:
                print("Please enter a number!")
        
        self.builder.set_languages(languages)
        
        # 6. Ability Scores
        print("\n=== ABILITY SCORES ===")
        print("1. Roll for stats")
        print("2. Manual entry")
        
        ability_choice = input("Enter your choice: ")
        while ability_choice not in ["1", "2"]:
            print("Invalid choice. Please try again.")
            ability_choice = input("Enter your choice: ")
        
        ability_scores = {
            "Strength": 10,
            "Dexterity": 10,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 10,
            "Charisma": 10
        }
        
        if ability_choice == "1":
            # Roll stats
            rolls = sorted([random.randint(3, 18) for _ in range(6)], reverse=True)
            print(f"\nYou rolled: {rolls}")
            
            temp_scores = ability_scores.copy()
            abilities = list(temp_scores.keys())
            
            for i, roll in enumerate(rolls):
                print(f"\nAssign roll {roll} to:")
                for j, ability in enumerate(abilities, 1):
                    print(f"{j}. {ability} (current: {temp_scores[ability]})")
                
                choice = input("Enter your choice: ")
                while not choice.isdigit() or int(choice) < 1 or int(choice) > len(abilities):
                    print("Invalid choice. Please try again.")
                    choice = input("Enter your choice: ")
                
                chosen_ability = abilities[int(choice)-1]
                temp_scores[chosen_ability] = roll
            
            ability_scores = temp_scores
        else:
            # Manual entry
            print("\nEnter ability scores (3-18):")
            for ability in ability_scores:
                while True:
                    try:
                        score = int(input(f"{ability}: "))
                        if 3 <= score <= 18:
                            ability_scores[ability] = score
                            break
                        else:
                            print("Score must be between 3 and 18.")
                    except ValueError:
                        print("Please enter a number.")
        
        # 7. Background Ability Adjustments (2and1 system)
        print("\nAdjust ability scores based on your background:")
        bg_abilities = self.backgrounds[bg_choice]["abilities"]
        print(f"Your background allows you to increase these abilities: {', '.join(bg_abilities)}")
        print("Options:")
        print("1. Increase one ability by 2 and another by 1")
        print("2. Increase all three abilities by 1")
        
        adjust_choice = input("Enter your choice: ")
        while adjust_choice not in ["1", "2"]:
            print("Invalid choice. Please try again.")
            adjust_choice = input("Enter your choice: ")
        
        if adjust_choice == "1":
            print("\nChoose one ability to increase by 2:")
            for i, ability in enumerate(bg_abilities, 1):
                print(f"{i}. {ability} (current: {ability_scores[ability]})")
            
            choice = input("Enter your choice: ")
            while not choice.isdigit() or int(choice) < 1 or int(choice) > len(bg_abilities):
                print("Invalid choice. Please try again.")
                choice = input("Enter your choice: ")
            
            ability1 = bg_abilities[int(choice)-1]
            ability_scores[ability1] = min(20, ability_scores[ability1] + 2)
            
            remaining_abilities = [a for a in bg_abilities if a != ability1]
            print("\nChoose one ability to increase by 1:")
            for i, ability in enumerate(remaining_abilities, 1):
                print(f"{i}. {ability} (current: {ability_scores[ability]})")
            
            choice = input("Enter your choice: ")
            while not choice.isdigit() or int(choice) < 1 or int(choice) > len(remaining_abilities):
                print("Invalid choice. Please try again.")
                choice = input("Enter your choice: ")
            
            ability2 = remaining_abilities[int(choice)-1]
            ability_scores[ability2] = min(20, ability_scores[ability2] + 1)
        else:
            for ability in bg_abilities:
                ability_scores[ability] = min(20, ability_scores[ability] + 1)
        
        self.builder.set_ability_scores(ability_scores)
        
        # 8. Appearance & Personality
        print("\n=== CHARACTER DESCRIPTION ===")
        appearance = input("Describe your character's appearance: ")
        personality = input("Describe your character's personality: ")
        self.builder.set_appearance(appearance).set_personality(personality)
        
        # 9. Finalize Character
        character = self.builder.get_character()
        character.display_character_sheet()
        
        # 10. Save Option
        save = input("\nWould you like to save this character? (yes/no): ").lower()
        if save == 'yes':
            filename = input("Enter a filename to save your character (without extension): ") + ".json"
            character.save_to_file(filename)