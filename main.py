# Ben
import archetypes
import character_creation
import time
import func
import stor

# Start Message
print("--------------------------")
print("Welcome to Text-Based RPG!")
print("--------------------------\n")

time.sleep(.5) # Delay by half a second

# Initialize Character Parameters
# Prompts the user to choose a name for the character
name  = input("Enter Your Character's Name: \n")
# Confirmation for name
print("\n", end="")
name = func.confirm(name, "Are you sure you want to name your character {}?", "Enter Your Character's Name: ")

# Prompts the user to choose an archetype
archetype = func.user_input("Choose your archetype", stor.archetype_names)
archetype = func.confirm(archetype, "Are you sure you want to choose {}?", "Choose your archetype: ",
                         stor.archetype_names, archetypes.dict1)
func.prompt1()

# Initializes the character and prints its attributes to the screen
character1 = character_creation.Character(name, archetypes.Archetypes(archetype))
print(character1)
