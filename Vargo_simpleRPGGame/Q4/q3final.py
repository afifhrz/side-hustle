#SETUP
yes_no = ['yes']
fighter_option = {  'heinz':{'hp':100,'atk':33,'def':7,'pow':2,'special':'fireball'},
                    'genesis':{'hp':100,'atk':30,'def':10,'pow':2,'special':'laser'},
                    'hydroxia':{'hp':100,'atk':27,'def':8,'pow':3,'special':'tsunami'}
                    }
#Above shows a dictionary inside a dictionary for each heroes
fight_act = ['atk', 'def', 'item']
random_place = ['Davinci Bank', 'BNI Bank', 'Permata Bank', 'BCA Bank']
death = False
item = {
    'petal':0,
    'tesseract':0,
    'mjolnir':0,
    'delta':0,
    'back' :0
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
#Above shows item function
#PRE-STORY
start_word = input("""Welcome to the Sudirman City!
The city is full of criminals. 
Here we need a hero who can help the police to uphold justice!
Are you willing to join us? (Yes/No)
""")
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

user_name = input("""Let's begin our journey by introducing yourself. What is your name?\n""")
user_name = user_name.title()
print("")
#Line 54-57 shows how responses that includes anything beside alphabets, will print "Hey Cyborg!"
if user_name.isalpha():
    print(f"Nice to meet you, {user_name}!")
else:
    print("Hey Cyborg! That's a cool name you have!")

#Validate userold input
user_old = input("""By the way, How old are you?\n""")

while not user_old.isnumeric():
    print("Input your age, please!")
    user_old = input("""How old are you?\n""")
#Line 62-64 requires only numeric response. No alphabets, symbols, etc.
user_old = int(user_old)
if user_old > 60:
    print("It seems like you're pretty old, but superheroes never die!")
elif user_old > 40:
    print("You are a great and a strong superhero, crush the enemies!")
elif user_old > 14:
    print("I think you're Spiderman's friend aren't you?")
elif user_old < 15:
    print("Keep your head up kid!")

continue_act = input("""\n---press enter to continue---\n""")

print(f"""Hello {user_name}, your task is to eradicate the criminals scattered in Sudirman City!
You must eradicate all of them by maintaining your health points.
Keep the HP you have so that it would always be above 0.
Win all missions with your remaining HP above 50 to get a honorary title.""")
continue_act = input("""\n---press enter to continue---\n""")

print(f"""{user_name}, choose your fighter!""")
for name, attribute in fighter_option.items():
    print(f"""\n~{name.title()}~
These are {name} attributes:""")
    for key, atr in attribute.items():
        print(f"""{key.upper()}:{atr}""")

user_fighter = input("What character that you gonna use?\n")
user_fighter = user_fighter.lower()

while user_fighter not in fighter_option.keys():
    print(f"""\nI don't understand. These are the options:""")
    for fighter in fighter_option.keys():
        print(fighter.title())
    print("")
    user_fighter = input("What character that you gonna use?\n")

print(f"""\nWow {user_fighter.title()}, that's great choice!\n""")

character_choice = fighter_option[user_fighter]
fight_act.append(character_choice['special'])

#MAIN STORY
import random
random_number_rob = random.randint(6,8)
place = random_place[random.randint(0,len(random_place)-1)]
#Above shows the ability for random banks for every game
print("""-------------------------
Biiip...
Biiip...
Biiip...
HQ : "Anyone there???""")
continue_act = input("""Your response here:\n""")

#Intentional theme: A superhero who intends to help the wrecked city filled with criminals, which they are attacking a bank right now. 
#The setting is dark and gloomy as smoke arrises from bombs and fire attacks among the police. Moreover, narrator seems to be persuasive.
print(f"""Oh thank goodness you're still there.
There is an emergency, there are {random_number_rob} people doing a bank robbery at {place}.
The sky is gloomy and most of the police forces has struggle to kill the boss inside the vault.
Time is ticking, hurry up! All units are on duty, only you are left.
{user_name.title()}! Please, help and answer if you are willing!""")
continue_act = input("""Your response here:\n""")
print(f"\n---{user_name.title()} On The Move!---\n")

print("""How to play!
There are the three options to play: fight, attack, defense, or special attack.
Base attack will not consume power.
Defend wouldn't attack but might increase some power points.
Special attack would deal high damage! But be aware of the limits allowed.""")
continue_act = input("""\n---press enter to continue---\n""")

enemy_status = random_number_rob
enemy_loop = 1

while enemy_status>0:
    
    if enemy_loop < random_number_rob-2:
        if enemy_loop == 1:
            continue_act = input(f"""Report from HQ:
In front of the {place} building, there are {random_number_rob-3} people who guards the bank entree.
Defeat them to get into the building and catch the gang of robbers!!!
Press Enter!\n""")
#Above shows further intentional theme
        enemy_hp = random.randint(20, 50)
        enemy_def= random.randint(5, 10)
        enemy_atk= random.randint(10, 18)
#Above shows the easy level enemy's random attributes 
        print(f"""        Beware!
        Enemy type: Scout
        Difficulty: Easy
        Enemy attributes:
        HP : {enemy_hp}
        ATK: {enemy_atk}
        DEF: {enemy_def}""")

    elif random_number_rob - 3 < enemy_loop and enemy_loop < random_number_rob - 1:
        if enemy_loop == random_number_rob - 2:
            continue_act = input(f"""HQ Report:
Great job, {user_name.title()}!
You have succeed the first stage!
As you enter the building with the police forces, the captain flanks you from behind wounding the officers!
The boss is now aware that you have entered the bank, and he's not going to stay for long. Hurry!
Press Enter!\n""")

        enemy_hp = random.randint(40, 60)
        enemy_def= random.randint(10, 15)
        enemy_atk= random.randint(15, 23)
#Above shows the medium level enemy's random attributes 
        print(f"""        Watch out!
        Enemy type: The Captain
        Difficulty: Moderate
        Enemy attributes:
        HP : {enemy_hp}
        ATK: {enemy_atk}
        DEF: {enemy_def}""")

    elif random_number_rob - 2 < enemy_loop and enemy_loop < random_number_rob:
        if enemy_loop == random_number_rob - 1:
            continue_act = input(f"""HQ Call...
Hello, {user_name.title()}!
The captain is dead, good! 
As you went down the stairs, you recognize this famous and astonishing face you remember.
She is a well known criminal, everyone knows no one has every won against her.
She is secretary. Beware of her high damage and think wise!
Fight her to proceed.
Press Enter!\n""")
#Above shows further intentional theme and storyline of the game
        enemy_hp = random.randint(50, 65)
        enemy_def= random.randint(15, 20)
        enemy_atk= random.randint(20, 23)
#Above shows the hard level enemy's random attributes 
        print(f"""        No more mistakes!
        Enemy type: The Secretary
        Difficulty: Hard
        Enemy attributes:
        HP : {enemy_hp}
        ATK: {enemy_atk}
        DEF: {enemy_def}""")        
    else:
        if enemy_loop == random_number_rob:
            continue_act = input(f"""HQ:
Unbelievable! You killed the infamous secretary.
As you enter the vault, all the gold has been removed and you found no one there.
You then heard a gold bar banging on the ground as if it drops.
You went out the vault and saw someone carrying a huge bag filled with gold bars. The bag is partially ripped as it carries the heavy gold.
Wait, oh no! That actually is the boss! The boss is on the run, catch em'!
Press Enter\n""")

        enemy_hp = random.randint(65, 70)
        enemy_def= random.randint(15, 20)
        enemy_atk= random.randint(20, 25)
#Above shows the hardest level enemy's random attributes 
        print(f"""        No EXCUSE!!!
        Enemy type: The Boss
        Difficulty: Deadly
        Enemy attributes:
        HP : {enemy_hp}
        ATK: {enemy_atk}
        DEF: {enemy_def}""")        

    fight_status = True
    while fight_status:
        if character_choice['hp'] > 0:
            act_choice = input(f"""
What is your act?
\'ATK\' for basic attack
\'DEF\' for defend
\'{character_choice['special'].upper()}\' for special attack
\'ITEM\' for check inventory\n""")
            if character_choice['pow']>=1:
                while act_choice.lower() not in fight_act:
                    print(f"""\nI don't understand. These are the options:""")
                    for fighter in fight_act:
                        print(fighter)
                    act_choice = input("""What is your act?\n""")
            else:
                while act_choice.lower() not in fight_act[:3]:
                    if act_choice.lower() == character_choice['special']:
                        print("""Sorry, you have no special powers left. Collect a tesseract to regain!""")
                        print(f"Your Remaining Power {character_choice['pow']}")
                    else:
                        print("""\nI don't understand. These are the options:""")
                        for fighter in fight_act[:3]:
                            print(fighter.upper())
                    act_choice = input("""What is your act?\n""")

            if act_choice.lower() == 'atk':
                reduced_hp = character_choice['atk'] - enemy_def
                enemy_hp = enemy_hp - reduced_hp
                print(f"\nEnemy HP reduced by {reduced_hp}")
                print("The Enemy: Argh! It Hurts!")
                if enemy_hp > 0:
                    print(f"Remaining Enemy HP {enemy_hp}")
                    character_choice['hp'] = character_choice['hp'] - (enemy_atk - character_choice['def'])
                    print("\n---Enemy Attack---\n")
                    print(f"Your HP reduced by {enemy_atk - character_choice['def']}")
                    print(f"Your Remaining HP {character_choice['hp']}")
                    print(f"Your Remaining Power {character_choice['pow']}")
                else:
                    print(f'\nThe Enemy has been eliminated!\n')
                    item_keys = list(item.keys())
                    random_item = item_keys[random.randint(0,3)]
                    add_item(random_item)
                    if enemy_loop != random_number_rob:
                        print(f"You get a loot! It's a {random_item}")
                continue_act = input("""\n---press enter to continue---""")
            elif act_choice.lower() == 'def':
                reduced_my_hp = enemy_atk - (character_choice['def'] + character_choice['def']*random.random())
                if reduced_my_hp > 0:
                    character_choice['pow'] += 0.5
                    character_choice['hp'] = character_choice['hp'] - reduced_my_hp
                    print("\n---Enemy Attack---\n")
                    print(f"Your HP reduced by {reduced_my_hp}")
                    print(f"Your Remaining HP {character_choice['hp']}")                    
                    print(f"Your Remaining Power {character_choice['pow']}")
                else:
                    print("Enemy Attack has no effect!")
                    print(f"Your Remaining HP {character_choice['hp']}")                    
                    print(f"Your Remaining Power {character_choice['pow']}")
                continue_act = input("""\n---press enter to continue---""")
            elif act_choice.lower() == 'item':
                print("This is your items:")
                for name, bagpack in item.items():
                    if name == 'back':
                        print(f"""{name.title()}""")
                    else:
                        print(f"""{name.title()} : {bagpack}""")
                item_use = input("What item you will choose?")
                item_use_condition = True
                while item_use_condition:
                    for word in item_use.lower().split():
                        if word in item.keys():
                            item_use_condition = False
                            item_key = word
                    if item_use_condition:
                        print("I don't understand. Please, choose again!")
                        item_use = input("What item you will choose?\n")
                if item[item_key] == 0 and 'back' != item_key:
                    print("You don't have any!")
                elif 'petal' in item_use.lower():
#Below shows how user is able to apply more than 1 item at a time (305-319) (This code also applies to the rest of the items):
                    amount_use = input ("How many petal you will choose?\n")
                    amount_condition = True
                    while amount_condition:
                        if amount_use.isnumeric():
                            amount_use = int(amount_use)
                            if amount_use <= item['petal']:
                                item['petal']-= amount_use
                                character_choice['hp'] += 10*amount_use
                                print(f"Your HP has increased {10*amount_use} points!")
                                amount_condition = False
                            else:
                                print(f"You don't have enough item!")
                                amount_use = input ("How many petal you will choose?\n")
                        else:
                            amount_use = input ("How many petal you will choose? (Integer only)\n")
                elif 'tesseract' in item_use.lower():
                    amount_use = input ("How many tesseract you will choose?\n")
                    amount_condition = True
                    while amount_condition:
                        if amount_use.isnumeric():
                            amount_use = int(amount_use)
                            if amount_use <= item['tesseract']:
                                item['tesseract']-= amount_use
                                character_choice['pow'] += 1*amount_use
                                print(f"Your special power has increased {1*amount_use} points!")
                                amount_condition = False
                            else:
                                print(f"You don't have enough item!")
                                amount_use = input ("How many tesseract you will choose?\n")
                        else:
                            amount_use = input ("How many tesseract you will choose? (Integer only)\n")
                elif 'mjolnir' in item_use.lower():
                    amount_use = input ("How many mjolnir you will choose?\n")
                    amount_condition = True
                    while amount_condition:
                        if amount_use.isnumeric():
                            amount_use = int(amount_use)
                            if amount_use <= item['mjolnir']:
                                item['mjolnir']-= amount_use
                                character_choice['atk'] += 5*amount_use
                                print(f"Your attack has increased {10*amount_use} points!")
                                amount_condition = False
                            else:
                                print(f"You don't have enough item!")
                                amount_use = input ("How many mjolnir you will choose?\n")
                        else:
                            amount_use = input ("How many mjolnir you will choose? (Integer only)\n")
                elif 'delta' in item_use.lower():
                    amount_use = input ("How many delta you will choose?\n")
                    amount_condition = True
                    while amount_condition:
                        if amount_use.isnumeric():
                            amount_use = int(amount_use)
                            if amount_use <= item['delta']:
                                item['delta']-= amount_use
                                character_choice['def'] += 5*amount_use
                                print(f"Your defense has increased {10*amount_use} points!")
                                amount_condition = False
                            else:
                                print(f"You don't have enough item!")
                                amount_use = input ("How many delta you will choose?\n")
                        else:
                            amount_use = input ("How many delta you will choose? (Integer only)\n")
                elif 'back' in item_use.lower():
                    pass 

            else:
                reduced_hp = character_choice['atk'] + character_choice['atk']*random.random() - enemy_def
                enemy_hp = enemy_hp - reduced_hp
                character_choice['pow'] = character_choice['pow'] - 1
                print(f"\nEnemy HP reduced by {reduced_hp}")
                print("The Enemy: Argh! It Hurts!")
                if enemy_hp > 0:
                    print(f"Remaining Enemy HP {enemy_hp}")
                    character_choice['hp'] = character_choice['hp'] - (enemy_atk - character_choice['def'])
                    print("\n---Enemy Attack---")
                    print(f"Your HP reduced by {enemy_atk - character_choice['def']}")
                    print(f"Your Remaining HP {character_choice['hp']}")
                    print(f"Your Remaining Power {character_choice['pow']}")                                       
                else:
                    print(f'\nThe Enemy has been eliminated!\n')
                    item_keys = list(item.keys())
                    random_item = item_keys[random.randint(0,3)]
                    add_item(random_item)
                    if enemy_loop != random_number_rob:
                        print(f"You get a loot! It's a {random_item}")
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

#END OF STORY
#Winning conditions
if death:
    print("You suck as a hero!")
    print("---Game Over---")
else:
    if character_choice['hp']>50:
        print("We are proud for having you here. Please accept this reward! Thank You!")
        print("---Game Over---")
    else:
        print("Thank you for saving the day!")
        print("---Game Over---")
#Note: When trying to apply items, try to input more than 1 word. For example: "I want to use my tesseract"