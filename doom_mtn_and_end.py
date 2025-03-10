# Lukas
import sys
import time
import func
import stor
import battle_functions
import art_archive
import enemy_creation
import main
import mustang_village

overall_hp = main.character1.get_health()
skeleton1=enemy_creation.Enemy("Skeleton",20,10,10,10)
skeleton2=enemy_creation.Enemy("Skeleton",20,10,10,10)
skeleton3=enemy_creation.Enemy("Skeleton",20,10,10,10)
commander_skeleton=enemy_creation.Enemy("COMMANDER Bones",70,40,20,20)
JOE_MAMA=enemy_creation.Enemy("Dark Lord JOE MAMA",200,50,30,30)
if mustang_village.store_8=="I long for a warm meal, surely the princess can wait a few more hours to be saved":
    print("Now that your appetite is quenched, you are ready to begin your descent into the ")
    print("castle and save the princess! You are thinking about what you will do once you ")
    print("save the princess when a living skeleton appears in front of you!")
    print("It immediately tries to attack you! You notice the skeleton is relatively slow and brittle.")
    battle_functions.combat_loop(main.character1,skeleton1)
    func.prompt1()
    print("\"That was easy,\" you tell yourself.")
    print("When suddenly...")
    time.sleep(1)
    print("There is now another Skeleton!!")
    battle_functions.combat_loop(main.character1, skeleton2)
    func.prompt1()
    print("\"Two enemies in one level, that is unheard of!\" You tell yourself.")
    print("And then...")
    time.sleep(1.)
    print("There is another skeleton.")
    print("This is starting to get annoying.")
    battle_functions.combat_loop(main.character1, skeleton3)
    func.prompt1()
    print("After your encounter with the last skeleton you get to a clearing and see a clear way up to DOOM CASTLE.")
    print("But......")
    time.sleep(1)
    print("There is about 10000 skeletons between you and castle.")
    store11=func.user_input("Should you fight through all 10000 skeletons or attempt to sneak past them?",stor.store11)
    if store11=="Fight through(STRENGTH)":
        if battle_functions.percent_chance(main.character1.get_strength()) is True:
            print("You, a skillful warrior, mow through all 10,000 skeletons")
            print("You are now at the base of the castle.")
        else:
            new_hp=int(main.character1.get_health()*.60)
            main.character1.set_health(new_hp)
            print("You barely manage to get past the skeleton horde. ")
            print("That was a mistake")
            print("You are now very wounded.")
    else:
        if battle_functions.percent_chance(main.character1.get_dexterity()) is True:
            print("You stealthily sneak past the skeleton horde to the base of the castle!")
        else:
            new_hp = int(main.character1.get_health() * .40)
            main.character1.set_health(new_hp)
            print("While sneaking past the horde, you pathetically trip over yourself.")
            print("You fall directly in the skeleton horde!")
            print("By some sheer luck, you manage to make it to the castle.")
            print("You are now terribly wounded.")
    print("At the entrance, you spot an important looking skeleton.")
    print("Your MONKEY BRAIN tells you that the enemy must SURELY have some precious, precious, LOOT.")
    store12=func.user_input("Should you attack the important looking skeleton?",stor.store12)
    if store12=="Attack":
        print("You walk up to the mean looking skeleton and immediately attack him!")
        battle_functions.combat_loop(main.character1,commander_skeleton)
        func.prompt1()
        if commander_skeleton.get_health()==-10000:
            print("You question why you even tried to attack him as you run into the castle.")
        else:
            print("You stand over the former heap of bones called commander.")
            print("You notice Commander Bones elegant sword and some of his rations, you take both this time!")
            print("You got Commander Bones Sword!(+40 Strength)")
            new_strength=main.character1.get_strength()+40
            main.character1.set_strength(new_strength)
            main.character1.set_health(overall_hp)
            print("After eating Commander Bones BONE MEAL your health was restored to full HP.")
    func.prompt1()
    print("You enter DOOM CASTLE. Dread hangs in the air, you nearly wet your pants in fear.")
    print("At the center of the throne room, you spot him: DARK LORD JOE MAMA.")
    print("The dark lord opens his mouth to speak to you...")
    print("\"I have waited a long time for you dear adventurer...\"")
    print("\"Or should I say...\"")
    func.prompt1()
    print("\"MY CHILD\"")
    time.sleep(1)
    print("You are caught aghast.")
    print("\"Yes that is right {}, I AM YOUR FATHER\"".format(main.character1.get_name()))
    store13=func.user_input("Do you Believe the DARK LORD JOE MAMA?",stor.store13)
    if store13 == "Yes":
        print("You are moved to tears in this beautiful moment")
        print("You run to embrace your long lost DAD!")
        func.prompt1()
        print("Your DAD proceeds to run his sword through YOU!")
        print("You collapse to the floor in a pool of your own blood.")
        print("The Dark Lord looks down at you and says \"God, you're a DUMB ASS!\"")
        print("Your vision fades to black as the Dark Lord's laughter bellows through the castle.")
        func.prompt1()
        print(art_archive.player_death_img())
        print("Dont believe every stranger you meet")
        sys.exit()
    else:
        print("You see easily through the Dark Lord's lie.")
        print("The Dark Lord grins hideously at you.")
        print("\"Although you aren't a complete imbecile, you are still foolish to challenge me!\"")
        print("\"Prepare to die!\"")
        print("Due to JOE MAMA's impressive MASS, it will be hard to escape him")
        reduced_agility=int(main.character1.get_agility()*.6)
        main.character1.set_agility(reduced_agility)
        battle_functions.combat_loop(main.character1,JOE_MAMA)
        func.prompt1()
        if JOE_MAMA.get_health()==-10000:
            print("You proceed to JUKE out JOE MAMA.")
            func.prompt1()
            print("JOE MAMA is so embarrassed that he impales himself with his sword.")
            print("You now run toward the Princess.")
        else:
            print("The Dark Lord lies broken on the floor, gasping for air.")
            print("He croaks to you, \"It is not too late, help me up and we shall rule POLYLANDIA together!\"")
            store14=func.user_input("Do you accept the Dark Lords offer?",stor.store14)
            if store14=="Yes":
                print("You reach out a hand to help your new ALLY.")
                print("The dark lord reaches out his hand and proceeds to...")
                func.prompt1()
                print("Run his sword through your skull!")
                print("Your body falls to the ground slightly twitching.")
                print("The Dark lord cackles weakly before succumbing to his wounds")
                print(art_archive.player_death_img())
                print("This death was completely your fault. Be smarter next time!")
                sys.exit()
            print("You see through the Dark Lords OBVIOUS lie and walk past him.")
        fin_store=func.user_input("You spot the princess stuck in a cage. What should you do with her?",stor.fin_l1)
        if fin_store=="Free Her":
            print("You free the princess.")
            print("She thanks you and gives you a little bit of gold as a reward.")
            func.prompt1()
            print("She calls the guards and kicks you out of the palace.")
            print("That was a little bit rude... but whatever.")
            print("Using your reward money, you buy some paint so you can watch it dry for the")
            print("REST OF YOUR LIFE :)")
        elif fin_store=="RUN!":
            print("You are filled with utter dread at seeing a WOMAN, more than when fighting JOE MAMA!")
            print("You turn around and start to run out of the castle.")
            print("You can hear her begging you to let her out")
            print("You proceed to run all the way back to your hut")
            print("and live in fear for the rest of your life after seeing a woman")
        else:
            print("You walk up to Princess and show her the keys to her cage.")
            print("Her face lights up with glee and THEN...")
            func.prompt1()
            print("You proceed to snap the key in half")
            print("The Princess bursts into tears.")
            print("You walk past the princess, laughing maniacally, and sit down on the throne.")
            print("You smile as you plan on how you will rule your new KINGDOM.")
        print("THE END")









else:
    print("Due to not visiting the tavern in mustang village the descent was deadly!")
    print("Due to not eating anything for pretty much the entire day, you collapse from sheer exhaustion and starvation")
    print("Your final thoughts on this earth is how much you longed for some beans....")
    print(art_archive.player_death_img())
    sys.exit()

