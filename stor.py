# Ben
# Note that each dictionary should generally be created in such a way that:
#   The first key of the embedded dictionary corresponds to the name of the
#       indicated entity.
#   The second key of the embedded dictionary corresponds to the description
#       of the entity. If the entity does not have a description, then the
#       second key and beyond of the embedded dictionary can instead be the
#       attributes associated with the entity
#       (i.e. Strength, Dexterity, etc.)
#   Any key of the embedded list beyond the first two correspond to the
#       attributes associated with the entity (if not already used)

# This list stores a verification phrase with "yes" and "no" options
phr_verification = ["Yes", "No"]

# This list stores the names of all the archetypes
archetype_names = ["Warrior", "Thief"]

# This dictionary stores the attributes of all the archetypes
archetype_dict = {"Warrior": {"Archetype": "Warrior",
                      "Description": "A brawler archetype with a focus on getting up-close and personal",
                      "Health": 1000, "Strength": 200, "Dexterity": 10, "Agility": 10},
                  "Thief": {"Archetype": "Thief",
                      "Description": "A sneaky and nimble class that runs circles around its enemies",
                      "Health": 50, "Strength": 10, "Dexterity": 20, "Agility": 20}}

# These lists are all the lists that will be used in opening_scene
opening_scene_l1 = ["Open it","Throw it away"]
opening_scene_l2 = ["Yes, it's Questin' Time!!!","No, that sounds like too much work."]

# These lists are all the lists that wil be used in forest_scene
forest_scene_l1 = ["Go through the DARK EVIL FOREST","Return home and watch paint dry"]
forest_scene_l2 = ["Investigate the bushes","Ignore it"]
forest_scene_l3 = ["Short Sword","Boots"]
#All decisions in doom_mtn_and_end
fin_l1 =["Free Her","Leave her in the Cage","RUN!"]
store14=["Yes","Hell No"]
store13=["Yes","Hell No"]
store12=["Attack","Ignore and sneak into the castle"]
store11=["Fight through(STRENGTH)","Attempt to sneak past(AGILITY)"]
# This is the dictionary that will be used in forest_scene
forest_scene_dict1 = {"Short Sword": {"Name": "Short Sword",
                                "Description": "A doubled-edged sword designed for close-quarters \n"
                                               "combat and agile movements on the battlefield. The hilt\n"
                                               "is chipped at the edges and the handle is clearly\n"
                                               "worn and torn, yet the blade remains surprisingly\n"
                                               "sharp",
                                "Strength": "+15", "Dexterity": "+5", "Agility": "+5"},
                      "Boots": {"Name": "Boots",
                                "Description": "These boots were crafted from exquisite bison hide \n"
                                               "and enchanted by craftsmen to mold to the wearer's\n"
                                               "feet and grant gusts of speed. However, you find that \n"
                                               "many of its enchantments are old and fading such that \n"
                                               "its effects are no where near as prominent as before.",
                                "Agility": "+10", "Dexterity": "+10", "Health": "+20"}}

# These lists are all the lists that will be used in mustang_village
mustang_village_l1 = ["Yes, I am here to depose the tyrant","Shut up, geezer. Mind your own business."]
mustang_village_l2 = ["I long for a warm meal, surely the princess can wait a few more hours to be saved",
                      "Time is of the essence, I must continue on my quest."]
mustang_village_l3 = ["STEW","FISH"]
mustang_village_l4 = ["Of course! Come here little dude", "No, get away from me you flea-stained rodent",
                      "Slay the adorable creature?"]
mustang_village_l5=["HEAVY ARMOR","LIGHT ARMOR"]
# These are the dictionaries that will be used in mustang_village
mustang_village_dict1 = {"STEW": {"Name": "STEW",
                                  "Description": "A mystery concoction prepared by the innkeeper himself.\n"
                                                 "The menu doesn't tell you much except that it includes a...\n"
                                                 "mushroom with a red cap and white spots? It's reminiscent of a \n"
                                                 "certain power-up from a game you played long ago, but it's best\n"
                                                 "not to take your chances."},
                         "FISH": {"Name": "FISH",
                                  "Description": "A fish prepared by the innkeeper himself. Strange, I \n"
                                                 "don't remember there being any fishermen in this part \n"
                                                 "of town."}}
mustang_village_dict2={"HEAVY ARMOR": {"Name": "HEAVY ARMOR",
                                  "Description": "A Mythical Armor that is said to have been previously worn by JOE MAMA Himself!.\n"
                                                 "That's probably the reason it is so big!\n"
                                                 "Some say that the armor even imbues its wearers with JOE MAMA'S STRENGTH.\n"
                                                 "But due to its weight it slows any user down heavily.",
                                   "Health": "+40", "Strength": "+25", "Agility": "-20"},
                         "LIGHT ARMOR": {"Name": "LIGHT ARMOR",
                                  "Description": "Made with mythical materials from the far lands of WALMART. \n"
                                                 "This armor is sure to provide some sort of protection. \n"
                                                 "It also imbues the wearer with the speed of a Black Friday Walmart shopper.",
                                         "Health": "+10", "Agility": "+20"}}
