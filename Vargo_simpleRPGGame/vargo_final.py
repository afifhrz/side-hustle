#Setup
#This section contains all the initial settings of the game

yes_no = ['yes']
fighter_option = {  'zhongli':{'hp':100,'atk':33,'def':7,'pow':2,'special':'fireball'},
                    'ganyu':{'hp':100,'atk':30,'def':10,'pow':2,'special':'laser'},
                    'albedo':{'hp':100,'atk':27,'def':8,'pow':3,'special':'tsunami'}
                    }
fight_act = ['atk', 'def', 'item']
random_place = ['Davinci Bank', 'BNI Bank', 'Permata Bank', 'BCA Bank']
death = False
item = {
    'petal':0,
    'tesseract':0,
    'mjolnir':0,
    'delta':0
}
item_list = item.keys()

def add_item(input_text):
    if input_text == 'petal':
        item['petal']+=1
    elif input_text == 'tesseract':
        item['tesseract']+=1
    elif input_text == 'mjolnir':
        item['mjolnir']+=1
    elif input_text == 'delta':
        item['delta']+=1

#Introductory text paragraph

start_word = input("""Welcome to the Sudirman City!
The city is full of criminals. 
Here we need a hero who can help the police to uphold justice!
Are you willing to join us? (Yes/No)
""")

#Section contains questions want to play or not
start_condition = True
while start_condition:
    if start_word.lower() == 'yes':
        print("")
        print("That's great! Let's Go!")
        start_condition = False
    elif start_word.lower() == 'no':
        print("Closing the Game!")
        exit()
        break
    else:
        start_word = input("I don't understand. Could you answer by \"Yes\" or \"No\", please?\n")

#Validate username input
user_name = input("""Let's begin our journey by introducing yourself. What is your name?\n""")
while not user_name:
    print("Input your name, please!")
    user_name = input("""What is your name?\n""")
user_name = user_name.title()
print("")

#Initial greeting to game users
if user_name.isalpha():
    print(f"Nice to meet you, {user_name}!")
else:
    print("Hey Cyborg! That's a cool name you have!")

#Validate userold input
user_old = input("""By the way, How old are you?\n""")
while not user_old:
    print("Input your age, please!")
    user_old = input("""How old are you?\n""")
user_old = int(user_old)
if user_old > 60:
    print("It seems you're pretty old, but superheroes never die!")
elif user_old > 40:
    print("You are a great and strong superhero, crush the enemies!")
elif user_old > 14:
    print("I think you're Spiderman's friend aren't you?")
elif user_old < 15:
    print("Keep your head up kid!")
print("")

#Initial greeting to game users
if user_name.isalpha():
    print(f"Nice to meet you, {user_name}!")
else:
    print("Hey Cyborg! That's a cool name you have!")

continue_act = input("""\n---press enter to continue---\n""")

#The victory conditions first part
print(f"""Hello {user_name}, your task is to eradicate the criminals scattered in Sudirman City!
You must eradicate all of them by maintaining your Health Points.
Keep the HP you have so that it is always above 0.
Win all missions and if you can complete with remaining HP above 50 then you will get an honorary title.""")
continue_act = input("""\n---press enter to continue---\n""")

#Choose the hero that will be used to eradicate the enemy
print(f"""{user_name}, choose your fighter!""")
for name, attribute in fighter_option.items():
    print(f"""\n~{name.title()}~
These are {name} attributes:""")
    for key, atr in attribute.items():
        print(f"""{key.upper()}:{atr}""")
user_fighter = input("\nWhat character that you gonna use?\n")
user_fighter = user_fighter.lower()

#Validate user hero choice
while user_fighter not in fighter_option.keys():
    print(f"""\nI don't understand. These are the options:""")
    for fighter in fighter_option.keys():
        print(fighter.title())
    print("")
    user_fighter = input("What character that you gonna use?\n")

print(f"""\nWow {user_fighter.title()}, that's great choice!\n""")
character_choice = fighter_option[user_fighter]

#Added special attack to the fight act setting
fight_act.append(character_choice['special'])

#Main Story Section

#Using random library to generate random number of enemies and random scene
import random
random_number_rob = random.randint(6,8)
place = random_place[random.randint(0,len(random_place)-1)]

#Initial scene gameplay
print("""-------------------------
Biiip...
Biiip...
Biiip...""")
continue_act = input("""\n---press enter to continue---\n""")

print(f"""Headquarter Report:
Hellooo, {user_name.title()}!
There is an emergency, there are {random_number_rob} people doing a bank robbery at {place}.
All units are on duty, only you are left.
Please, help us!""")
continue_act = input("""\n---press enter to continue---\n""")

print(f"\n---{user_name.title()} On The Move!---\n")

#How To Play tutorial!
print("""How to play!
There are three options to fight!
1. Attack
2. Defense
3. Special Attack

Attack will not consume power.
Defense is not doing attack but can increase some power points
Special Attack consume power one point""")

continue_act = input("""\n---press enter to continue---\n""")

enemy_status = random_number_rob
enemy_loop = 1

#Main fighting scene
while enemy_status>0:
    
    #Conditioning of scene script prompt!
    if enemy_loop < random_number_rob-2:
        if enemy_loop == 1:
            continue_act = input(f"""Report from HQ:
In front of the {place} building, there are {random_number_rob-3} people who must be confronted first.
Defeat them to get into the building and catch the gang of robbers!!!
Press Enter!\n""")

        enemy_hp = random.randint(20, 50)
        enemy_def= random.randint(5, 10)
        enemy_atk= random.randint(10, 18)

        print(f"""        Beware!
        Enemy type: Scout!
        Enemy attributes:
        HP : {enemy_hp}
        ATK: {enemy_atk}
        DEF: {enemy_def}""")

    elif random_number_rob - 3 < enemy_loop and enemy_loop < random_number_rob - 1:
        if enemy_loop == random_number_rob - 2:
            continue_act = input(f"""HQ Report:
Great job, {user_name.title()}!
You have been successful in the first stage!
Enter the building and finish off The Captain!
Press Enter!\n""")

        enemy_hp = random.randint(40, 60)
        enemy_def= random.randint(10, 15)
        enemy_atk= random.randint(15, 23)
        
        print(f"""        Watch out!!!
        Enemy type: The Captain!
        Enemy attributes:
        HP : {enemy_hp}
        ATK: {enemy_atk}
        DEF: {enemy_def}""")

    elif random_number_rob - 2 < enemy_loop and enemy_loop < random_number_rob:
        if enemy_loop == random_number_rob - 1:
            continue_act = input(f"""HQ Call...
Hello, {user_name.title()}!
As you walk down the bank, you passed through one of the robbers, The Secretary.
Fight him to proceed.
Press Enter!\n""")

        enemy_hp = random.randint(50, 65)
        enemy_def= random.randint(15, 20)
        enemy_atk= random.randint(20, 23)
        
        print(f"""        No more mistakes!
        Enemy type: The Secretary!
        Enemy attributes:
        HP : {enemy_hp}
        ATK: {enemy_atk}
        DEF: {enemy_def}""")        
    else:
        if enemy_loop == random_number_rob:
            continue_act = input(f"""HQ:
THE LAST MAN, {user_name.title()}!
THAT IS THE BOSS!
Press Enter\n""")

        enemy_hp = random.randint(65, 70)
        enemy_def= random.randint(15, 20)
        enemy_atk= random.randint(20, 25)
        
        print(f"""        No EXCUSE!!!
        Enemy type: The Boss!
        Enemy attributes:
        HP : {enemy_hp}
        ATK: {enemy_atk}
        DEF: {enemy_def}""")        

    #Fight Act User Input
    fight_status = True
    while fight_status:
        if character_choice['hp'] > 0:
            act_choice = input(f"""
What is your act?
\'ATK\' for basic attack
\'DEF\' for defend
\'{character_choice['special'].upper()}\' for special attack
\'ITEM\' for check inventory\n""")
            
            #Condition if power still available or not
            if character_choice['pow']>=1:
                #Input Fight Act Validation
                while act_choice.lower() not in fight_act:
                    print(f"""\nI don't understand. These are the options:""")
                    for fighter in fight_act:
                        print(fighter)
                    act_choice = input("""What is your act?\n""")
            else:
                #Input Fight Act Validation
                while act_choice.lower() not in fight_act[:3]:
                    print(f"""\nI don't understand. These are the options:""")
                    for fighter in fight_act[:3]:
                        print(fighter.upper())
                    print(f"Your Remaining Power {character_choice['pow']}")
                    act_choice = input("""What is your act?\n""")

            #Follow up the fight act input
            if act_choice.lower() == 'atk':
                reduced_hp = character_choice['atk'] - enemy_def
                enemy_hp = enemy_hp - reduced_hp
                print(f"\nEnemy HP reduced by {reduced_hp}")
                print("The Enemy: Argh Its Hurt!")

                #Condition for enemy has died or not!
                if enemy_hp > 0:
                    print(f"Remaining Enemy HP {enemy_hp}")
                    character_choice['hp'] = character_choice['hp'] - (enemy_atk - character_choice['def'])
                    print("\n---Enemy Attack---\n")
                    print(f"Your HP reduced by {enemy_atk - character_choice['def']}")
                    if character_choice['hp'] <= 0:
                        print(f"Your Remaining HP 0")
                    else:
                        print(f"Your Remaining HP {character_choice['hp']}")
                        print(f"Your Remaining Power {character_choice['pow']}")
                else:
                    print(f'\nThe Enemy has been eliminated!\n')
                    item_keys = list(item.keys())
                    random_item = item_keys[random.randint(0,len(item.keys())-1)]
                    add_item(random_item)
                    if enemy_loop != random_number_rob:
                        print(f"You get a loot! It's {random_item}")
                continue_act = input("""\n---press enter to continue---""")
            elif act_choice.lower() == 'def':
                reduced_my_hp = enemy_atk - (character_choice['def'] + character_choice['def']*random.random())
                if reduced_my_hp > 0:
                    character_choice['pow'] += 0.5
                    character_choice['hp'] = character_choice['hp'] - reduced_my_hp
                    print("\n---Enemy Attack---\n")
                    print(f"Your HP reduced by {reduced_my_hp}")
                    if character_choice['hp'] <= 0:
                        print(f"Your Remaining HP 0")
                    else:
                        print(f"Your Remaining HP {character_choice['hp']}")
                        print(f"Your Remaining Power {character_choice['pow']}") 
                else:
                    print("Enemy Attack has no effect!")
                    print(f"Your Remaining HP {character_choice['hp']}")                    
                    print(f"Your Remaining Power {character_choice['pow']}")
                continue_act = input("""\n---press enter to continue---""")
            elif act_choice.lower() == 'item':
                print(f"{user_name.title()}'s items:")

                #Looping to print bagpack item!
                for name, bagpack in item.items():
                    print(f"""{name.title()} : {bagpack}""")
                item_use = input("What item you will choose?")
                
                #Validate item input!
                while item_use.lower() not in item.keys():
                    print("I don't understand. Please, choose again!")
                    item_use = input("What item you will choose?\n")
                if item[item_use.lower()] == 0:
                    print("You don't have any!")
                
                #Items effect and influence the game
                elif 'petal' in item_use.lower():
                    item['petal']-=1
                    character_choice['hp'] += 10
                    print("Your HP has increased 10 points!")
                elif 'tesseract' in item_use.lower():
                    item['tesseract']-=1
                    character_choice['pow'] += 1
                    print("You get one Power!")
                elif 'mjolnir' in item_use.lower():
                    item['mjolnir']-=1
                    character_choice['atk'] += 5
                    print("Your Attack has increased 5 points!")
                elif 'delta' in item_use.lower():
                    item['delta']-=1
                    character_choice['def'] += 5
                    print("Your Defense has increased 5 points!")
            else:
                reduced_hp = character_choice['atk'] + character_choice['atk']*random.random() - enemy_def
                enemy_hp = enemy_hp - reduced_hp
                character_choice['pow'] = character_choice['pow'] - 1
                print(f"\nEnemy HP reduced by {reduced_hp}")
                print("The Enemy: Argh Its Hurt!")

                #Condition for enemy has died or not!
                if enemy_hp > 0:
                    print(f"Remaining Enemy HP {enemy_hp}")
                    character_choice['hp'] = character_choice['hp'] - (enemy_atk - character_choice['def'])
                    print("\n---Enemy Attack---")
                    print(f"Your HP reduced by {enemy_atk - character_choice['def']}")
                    if character_choice['hp'] <= 0:
                        print(f"Your Remaining HP 0")
                    else:
                        print(f"Your Remaining HP {character_choice['hp']}")
                        print(f"Your Remaining Power {character_choice['pow']}")
                else:
                    print(f'\nThe Enemy has been eliminated!\n')
                    item_keys = list(item.keys())
                    random_item = item_keys[random.randint(0,len(item.keys())-1)]
                    add_item(random_item)
                    if enemy_loop != random_number_rob:
                        print(f"You get a loot! It's {random_item}")
                continue_act = input("""\n---press enter to continue---""")

            if enemy_hp < 0:
                fight_status = False
                enemy_loop += 1
                enemy_status -= 1
        else:
            print("You have died!")
            death = True
            enemy_status -= 1000
            break

#End of Story

#Appreciation Day!
if death:
    print("You are a suck hero!")
    print("---Game Over---")
else:
    if character_choice['hp']>50:
        print(f"We are proud for having you here. {user_name.title()}, Please accept this reward! Thank You!")
        print("---Game Over---")
    else:
        print("Thank you for saving the day!")
        print("---Game Over---")