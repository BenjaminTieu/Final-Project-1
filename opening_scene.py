#Lukas
import random
import time
import func
import stor
import art_archive
import character_creation
import enemy_creation
import archetypes
import main
starting_health=main.character1.get_health()
print(art_archive.hut())
print("You are sitting in your hut one day.")
print("When all of a sudden, you receive a letter...")
store=func.user_input("Do you want to open it or throw it away?", stor.opening_scene_l1)
if store=="Open it":
    print(art_archive.letter())
    print("If you kill Dark Lord Joe Mama, you would be a hero to the kingdom!")
    print("And might even get the princesses hand in marriage?")
    store_2=func.user_input("Should you go on a quest to save Polylandia from the dark lord Joe Mama?"
                            ,stor.opening_scene_l2)
    if store_2=="Yes, it's Questin' Time!!!":
        print("You decide its time to go save the kingdom!")
        print("You grab your old gear and set off to the capital of Polylandia, Mustang Village")
    else:
        print("You decide that going on a quest is too much work")
        print("You tell yourself, \"Why even quest when there are more interesting things to do...\"")
        print("like watching paint dry!")

else:
    print("You crumple up the letter")
    print("Probably some junk parchment you tell yourself")
    print("as you throw it into the fire.")
    print(art_archive.fire())
    print("Your journey ends just as quickly as it begun")
