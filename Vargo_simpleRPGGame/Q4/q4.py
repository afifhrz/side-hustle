#Configuration

import random

minimarket_item_info = {
    'petal':"""You can use Petal to increase Hero's Health""",
    'tesseract':"""You can use Petal to increase Hero's Power""",
    'mjolnir':"""You can use Petal to increase Hero's Attack""",
    'delta':"""You can use Petal to increase Hero's Defend"""
}

npc_sentence = {
    'lounge':["""New Comer: \"I don't remember there is person like you here!\"""", 
    """Stranger: \"Do you hear the tremble over Labazard?\"""",
    """Mr. Smith: \"I think you should try to buy some weapons at Blacksmith!\"""",
    """Ms. Flower: \"Never empty your pocket with Petal, it will helps you a lot\"""",
    """Athlete: \"Use your special attack only when you need most!\""""],
    'forest':["""Guard: \"There are many strange creatures lives in here! Watch your step!\"""", 
    """Guard: \"Why are you here? Don't you go to school?\"""",
    """Guard: \"There is no easy sweet victory!\"""",
    """Guard: \"Have you found what you are looking for?\"""",
    """Guard: \"Use your special attack only when you need most!\""""],
    'labazard':["""The scientist: \"The lab turned out to be an illegal lab that conducted experiments on wild animals in a very sadistic way.\"""", 
    """The scientist: \"Help us please!\"""",
    """The scientist: \"Over time, it turns out that many Groniche are very wild and dangerous alias has lost consciousness\"""",
    """The scientist: \"The chief lab did experiment on his own body!\"""",
    """The scientist: \"Please, be alive and save us!\""""]
}

#Class Section
class Game:

    def __init__(self):
        print("""---Welcome to Dekakary City!---
The city is full of happiness.
But wait, what are those strange animals?
It's called Groniche Monster.
""")
        self.name = input("Anyway, let's begin our journey by introducing yourself. What is your name?\n")
        self.name = self.name.title()
        if self.name.isalpha():
            print(f"Nice to meet you, {self.name}!")
        else:
            print("Hey Cyborg! That's a cool name you have!")

        self.labazard_floor = {
            2:False,
            3:False
        }

    def choosing_hero(self):
        fighter_option = {  
    'heinz':{
        'atk':100,
        'def':2,
        'special':'fireball'
        },
    'genesis':{
        'atk':15,
        'def':5,
        'special':'laser'
        },
    'hydroxia':{
        'atk':10,
        'def':10,
        'special':'tsunami'
        }
    }
        print(f"""{self.name}, choose your fighter!""")
        for name, attribute in fighter_option.items():
            print(f"""\n~{name.title()}~
        These are {name} attributes:""")
            for key, atr in attribute.items():
                print(f"""{key.upper()}:{atr}""")
        character_choice = input("What character that you gonna use?\n")
        character_choice = character_choice.lower()

        while character_choice.lower() not in fighter_option.keys():
            print(f"""\nI don't understand. These are the options:""")
            for fighter in fighter_option.keys():
                print(fighter.title())
            print("")
            character_choice = input("What character that you gonna use?\n")

        print(f"""\nWow {character_choice.title()}, that's great choice!""")
        
        character_choice = character_choice.lower()
        attack = fighter_option[character_choice]['atk']
        defend = fighter_option[character_choice]['def']
        special = fighter_option[character_choice]['special']

        return Hero(character_choice.title(), attack, defend, special)

    def validating_userold(self):
        self.age = input("""By the way, How old are you?\n""")

        while not self.age.isnumeric():
            print("Input your age, please!")
            self.age = input("""How old are you?\n""")

        #Line ---- requires only numeric response. No alphabets, symbols, etc.
        self.age = int(self.age)
        if self.age > 60:
            print("It seems like you're pretty old, but gamer never die!")
        elif self.age > 40:
            print("You are a great and a strong, crush the challenge!")
        elif self.age > 14:
            print("I think you're Spiderman's friend aren't you?")
        elif self.age < 15:
            print("Keep your head up kid!")

    def continue_act(self):
        input("""\n---press enter to continue---\n""")

    def dekakary_welcome(self):
        print(f"""Hello {self.name}, your task is to explore Dekakary City!
Find the odd of the city and have fun!""")

    def how_to_play(self):
        print("""How to play!
There are the four options to play: Attack, Defense, or Special Attack.
Attack will using the attack point
Defend wouldn't attack but might increase some power points.
Special attack would deal high damage! But be aware of the limits allowed.""")
    
    def forest_info(self):
        print("""
This is a forbidden forest
This forest contains Groniche Monster that the Town Hall residents managed to throw away.
Many of the Groniche here start from harmless monsters to become very dangerous crazy monsters.
""")

    def labazard_info(self):
        print("""
Labazard consists of 3 floors
You have to finish each floor
(If you lose, you must repeat to the last floor passed).

Each floor has a different level of monsters
The lab chief who has turned into a Super Groniche is on the 3rd floor
""")

    def labazard_first_floor(self):
        print("""
This is the First Floor of Labazard!
Your task here are to eliminated every mutated monster.
Be Safe and Be Alive!
""")

    def labazard_second_floor(self):
        print("""
The monsters are very dangerous in this Second Floor of Labazard!
Your task here are to eliminated every mutated monster.
Prepare yourself!
""")

    def labazard_third_floor(self):
        print("""
There is no more that i can say that is the insane chief's lab!
Be ready!
""")

class Hero:
    def __init__(self, name, attack, defend, special):
        
        self.name = name
        self.attack_point = attack
        self.defend_point = defend
        self.special_name = special
        
        self.health_point = 100
        self.power_point = 0.0
        self.money = 500
        self.items = {
            'Petal':0,
            'Tesseract':0,
            'Mjolnir':0,
            'Delta':0
        }
        self.weapons = []

    def attack(self, monster, using_special = False):
        
        if self.weapons != []:
            print("You have the following weapons:")
            weaponoptions = []
        
            for weapon in self.weapons:
                print(f"- {weapon.name} does {weapon.damage} damage")
                weapon_dictionary = weapon.__dict__ 
                weaponoptions.append(weapon_dictionary) 
                selectweapon = input("\nWhich weapon will you use to attack: ")

            for weapon in weaponoptions: # Loop to make sure selectweapon is one of the weapon options
                if weapon["name"] == selectweapon.title(): # Looks in each weapon's name key to see if it matches selectweapon input
                    if using_special:
                        reduction = weapon["damage"] + self.attack_point*1.5
                        monster.health = monster.health - reduction
                        print(f"Your", weapon["name"], "with special attack did" , reduction, "damage.")
                    else:
                        reduction = weapon["damage"] + self.attack_point
                        monster.health = monster.health - reduction
                        print(f"Your", weapon["name"], "did" , reduction, "damage.")
    
                    print(f"The {monster.name} now has {monster.health} health remaining.")
                    break
                else:
                    print("I don't understand which weapons!")
        else:
            if using_special:
                monster.health -= self.attack_point*1.5 
                print(f"Your special attack did" , self.attack_point*1.5, "damage.")
            else:
                monster.health -= self.attack_point
                print(f"Your attack did" , self.attack_point, "damage.")
            print(f"The {monster.name} now has {monster.health} health remaining.")
        user.continue_act()

    def defend(self, monster):
        reduced_my_hp = monster.attack- self.defend_point
        self.power_point += 0.1
        if reduced_my_hp > 0:
            self.health_point -= reduced_my_hp
            print("\n---Enemy Attack---\n")
            print(f"Your HP reduced by {reduced_my_hp}")
            print(f"Your Remaining HP {self.health_point}")                    
            print(f"Your Remaining Power {self.power_point}")
        else:
            print("Enemy Attack has no effect!")
            print(f"Your Remaining HP {self.health_point}")                    
            print(f"Your Remaining Power {self.power_point}")
        user.continue_act()

    def using_item(self):
        print("This is your items:")
        for name, bagpack in self.items.items():
            print(f"""{name.title()} : {bagpack}""")
        print("Back")
        options = list(self.items.keys())
        options.append('Back')
        
        item_use = input("\nWhat item you will choose? ")
        while item_use.title() not in options:
            print("I don't understand. Please, choose again!")            
            item_use = input("What item you will choose? ")
        if self.items[item_use.title()] == 0 and 'back' != item_use.lower():
            print("You don't have any!")
            self.using_item()
        
        while True:
            amount = input(f"How many {item_use.title()} you will choose? (Integer Only)\n")
            if not amount.isnumeric():
                print("Integer Only Please!")
            elif int(amount) > self.items[item_use.title()]:
                print(f"You don't have enough item!")
            else:
                break
        amount = int(amount)
        if 'petal' == item_use.lower():
            self.items[item_use.title()]-= amount
            self.health_point += 10*amount
            print(f"Your HP has increased {10*amount} points!")
        elif 'mjolnir' == item_use.lower():
            self.items[item_use.title()]-= amount
            self.attack_point += 5*amount
            print(f"Your Attack Point has increased {5*amount} points!")
        elif 'tesseract' == item_use.lower():
            self.items[item_use.title()]-= amount
            self.power_point += 1*amount
            print(f"Your Power Point has increased {1*amount} points!")
        elif 'delta' == item_use.lower():
            self.items[item_use.title()]-= amount
            self.defend_point += 5*amount
            print(f"Your DefendPoint has increased {5*amount} points!")
        elif 'back' in item_use.lower():
            pass

    def battle(self, monster):
        monster.status()

        while monster.health>0:
            if self.health_point > 0:
                self.status()
                act_choice = input(f"""
What is your act?
\'ATK\' for basic attack
\'DEF\' for defend
\'{self.special_name.upper()}\' for special attack
\'ITEM\' for check inventory\n""")
                if act_choice.lower() == 'atk':
                    self.attack(monster)
                elif act_choice.lower() == 'def':
                    self.defend(monster)
                elif act_choice.lower() == 'item':
                    self.using_item() 
                elif act_choice.lower() == self.special_name.lower():
                    if self.power_point >= 1:
                        self.attack(monster, using_special=True)
                    else:
                        print("You don't have enough Power Point!")
                else:
                    print("""I don't understand! Please re-input!""")

            else:
                print("You have died!")
                self.health_point = 100
                lounge()
        
        print(f"Nice work! You defeated the {monster.name}.")
        user.continue_act()
        self.loot_item(monster)

    def status(self):
        print(f"""Here are your hero status:
Health  : {self.health_point}
Attack  : {hero.attack_point}
Defend  : {hero.defend_point}
Power   : {hero.power_point}
Money   : ${hero.money}
Item    : {hero.items}""")
                 
    def loot_item(self, monster):
        item_keys = list(self.items.keys())

        if monster.type == 'easy':    
            random_item = item_keys[random.randint(0,0)]
            random_money = random.randint(0,5)
        elif monster.type == 'medium':
            random_item = item_keys[random.choice([0,2])]
            random_money = random.randint(0,10)
        elif monster.type == 'hard':
            random_item = item_keys[random.choice([0,2,3])]
            random_money = random.randint(5,15)
        elif monster.type == 'expert':
            random_item = item_keys[random.choice([0,1,2,3])]
            random_money = random.randint(15,20)

        self.items[random_item]+=1
        self.money += random_money
        print(f"You get a loot! It's a {random_item} and ${random_money}")

class Monster:
    def __init__(self, type):
        self.type = type.lower()
        if self.type == 'easy':
            self.name = 'Little Groniche'
            self.health=50
            self.attack=random.randint(1,5)
            self.defend=random.randint(1,5)
        elif self.type == 'medium':
            self.name = 'Gronicheee'
            self.health=75
            self.attack=random.randint(5,10)
            self.defend=random.randint(5,10)
        elif self.type == 'hard':
            self.name  = 'Big Gron'
            self.health=100
            self.attack=random.randint(10,15)
            self.defend=random.randint(10,15)
        elif self.type == 'expert':
            self.name = 'MassGron'
            self.health=125
            self.attack=random.randint(20,50)
            self.defend=random.randint(20,25)
        else:
            self.name = 'Boss'
            self.health=2000
            self.attack=random.randint(300,300)
            self.defend=random.randint(400,400)

    def status(self):
        print(f"""Here are your monster status:
Name    : {self.name}
Health  : {self.health}
Attack  : {self.attack}
Defend  : {self.defend}""")

class Weapon:
    def __init__(self, name, value, damage):
        self.name = name
        self.value = value
        self.damage = damage

class Item:
    def __init__(self, name, value, effect_point):
        self.name = name
        self.value = value
        self.effect_point = effect_point    

class Shop:
    
    def __init__(self, name, rack):
        self.name = name
        self.rack = rack

    def showing_rack(self):
        #showing options
        for item in self.rack:
            print(f"""{item.name}:${item.value}""")
        print("Back")

    def transaction(self):
        rackoptions = {}
        for rack_item in self.rack:
            rackoptions[rack_item.name]=rack_item.value
        rackoptions['Back']=''

        print(f"""Welcome to {self.name}!
We can provide what you need!
Here are our things!
""")
        print(f"Your money : ${hero.money}\n")
        self.showing_rack()

        #validating input
        item_input = input("What items do you need?")
        while item_input.title() not in rackoptions.keys():
            print("I don't understand. Please re-input!")
            item_input = input("What items do you need?")
        
        if item_input.title() != 'Back' and hero.money>rackoptions[item_input.title()]:
            hero.money -= rackoptions[item_input.title()]
            if self.name == 'Minimarket':
                hero.items[item_input.title()]+=1
            else:
                if item_input.title() == 'Dagger':
                    hero.weapons.append(dagger)
                elif item_input.title() == 'Gun':
                    hero.weapons.append(gun)
                elif item_input.title() == 'Sword':
                    hero.weapons.append(sword)
                elif item_input.title() == 'Beam':
                    hero.weapons.append(beam)    
            print("Thankyou for purchasing!")
        elif item_input.title() != 'Back' and hero.money<rackoptions[item_input.title()]:
            print("You don't have enough money to purchase!")
            self.transaction()
        else:
            print("Thankyou for visiting!")

#Function Section

def lounge():
    print("---You are in Town Hall!---")
    user.continue_act()
    print("""
--------------------------------
           TOWN HALL
--------------------------------

Here some options that you can afford:

1. Minimarket
2. Blacksmith
3. Forest
4. Labazard
5. Status
6. Talk to strangers
7. Exit Game
""")

    question = input("What you gonna do? [Type 1 - 7]\n")

    while question:
        if question.lower() == '1':
            minimarket.transaction()
            user.continue_act()
            lounge()
        elif question.lower() == '2':
            blacksmith.transaction()
            user.continue_act()
            lounge()
        elif question.lower() == '3':
            forest()
        elif question.lower() == '4':
            labazard()
        elif question.lower() == '5':
            hero.status()
            user.continue_act()
            lounge()
        elif question.lower() == '6':
            print(npc_sentence['lounge'][random.randint(0,len(npc_sentence['lounge'])-1)])
            user.continue_act()
            lounge()  
        elif question.lower() == '7':
            print("Closing the Game!")
            exit()
        else:
            print("\nSorry, I don't understand.\n")
            lounge()

def forest():
    print("---You are entering Dark Forest!---")
    user.continue_act()
    print("""
--------------------------------
           DARK FOREST
--------------------------------

Here some options that you can afford:

0. Forest Info
1. Find Buff
2. Using Item
3. Weapon
4. Status
5. Talk to guard
6. Back to Town Hall
7. Exit Game
""")

    question = input("What you gonna do? [Type 1 - 7]\n")

    if question.lower() == '0':
        user.forest_info()
        user.continue_act()
        forest()
    elif question.lower() == '1':
        question_2 = input("""What level do you choose?
Easy    : Monster level 1 - 20
Medium  : Monster level 20 - 40
Hard    : Monster level 40 - 50
Expert  : Monster level 50 - 100
""")    
        while True:
            if question_2.lower()=='easy' or question_2.lower()=='medium' or question_2.lower()=='hard' or question_2.lower()=='expert':
                break
            else:
                print("""I don't understand. Please re-input!""")
                question_2 = input("""What level do you choose?
Easy    : Monster level 1 - 10
Medium  : Monster level 20 - 40
Hard    : Monster level 40 - 50
Expert  : Monster level 50 - 100
""")    
        for loop in range(random.randint(3,10)):
            monster = Monster(question_2.lower())
            hero.battle(monster)

        print("You have finished your battle\nYou are quitting battlefield!")
        user.continue_act()

        forest()
    elif question.lower() == '2':
        hero.using_item()
        user.continue_act()
        forest()
    elif question.lower() == '3':
        if hero.weapons != []:
            print("You have the following weapons:")
            for weapon in hero.weapons:
                print(f"- {weapon.name} does {weapon.damage} damage")
        else:
            print("Buy the weapon, first!")
        user.continue_act()
        forest()
    elif question.lower() == '4':
        hero.status()
        user.continue_act()
        forest()
    elif question.lower() == '5':
        print(npc_sentence['forest'][random.randint(0,len(npc_sentence['forest'])-1)])
        user.continue_act()
        forest()
    elif question.lower() == '6':
        lounge()
    elif question.lower() == '7':
        exit()
    else:
        print("\nSorry, I don't understand.\n")
        forest()       

def labazard():
    print("---You are entering Hazardous Labazard!---")
    user.continue_act()
    print("""
--------------------------------
             LABAZARD
--------------------------------

Here some options that you can afford:

0. Labazard Info
1. First Floor
2. Second Floor
3. Third Floor
4. Using Item
5. Weapon
6. Status
7. Talk to scientist
8. Minimarket
9. Blacksmith
10. Back to Town Hall
11. Exit Game
""")

    question = input("What you gonna do? [Type 1 - 11]\n")

    if question.lower() == '0':
        user.labazard_info()
        user.continue_act()
        labazard()
    elif question.lower() == '1':
        
        user.labazard_first_floor()
        user.continue_act()
        
        for loop in range(random.randint(5,10)):
            monster = Monster("hard")
            hero.battle(monster)

        print("You have finished the first floor of labazard!")
        user.labazard_floor[2] = True
        user.continue_act()
        labazard()
    elif question.lower() == '2':
        if user.labazard_floor[2]:

            user.labazard_second_floor()
            user.continue_act()
            for loop in range(random.randint(5,15)):
                monster = Monster("expert")
                hero.battle(monster)

            print("You have finished the second floor of labazard!")
            user.labazard_floor[3] = True
            user.continue_act()

            labazard()
        else:
            print("You need to finish the first floor!")
            user.continue_act()
            labazard()
    elif question.lower() == '3':
        if user.labazard_floor[3]:

            user.labazard_second_floor()
            user.continue_act()
            
            monster = Monster("boss")
            hero.battle(monster)
            print("Congratulations, The Labazard has destroyed!\nYou have helped the citizens a lot!")
            user.continue_act()

            labazard()
        else:
            print("You need to finish the second floor!")
            user.continue_act()
            labazard()
    elif question.lower() == '4':
        hero.using_item()
        user.continue_act()
        labazard()
    elif question.lower() == '5':
        if hero.weapons != []:
            print("You have the following weapons:")
            for weapon in hero.weapons:
                print(f"- {weapon.name} does {weapon.damage} damage")
        else:
            print("Buy the weapon, first!")
        user.continue_act()
        labazard()
    elif question.lower() == '6':
        hero.status()
        user.continue_act()
        labazard()
    elif question.lower() == '7':
        print(npc_sentence['labazard'][random.randint(0,len(npc_sentence['labazard'])-1)])
        user.continue_act()
        labazard()
    elif question.lower() == '8':
        minimarket.transaction()
        user.continue_act()
        labazard()
    elif question.lower() == '9':
        blacksmith.transaction()
        user.continue_act()
        labazard()
    elif question.lower() == '10':
        lounge()
    elif question.lower() == '11':
        exit()
    else:
        print("\nSorry, I don't understand.\n")
        labazard()

#Gaming Script#

#Creating Instances
petal = Item("Petal", 5, 10)
tesseract = Item("Tesseract", 20, 1)
mjolnir = Item("Mjolnir", 15, 5)
delta = Item("Delta", 10, 10)
petal = Item("Petal", 5, 10)
minimarket = Shop("Minimarket", [petal, tesseract, mjolnir, delta, petal])

dagger  = Weapon("Dagger", 20, 10)
sword   = Weapon("Sword", 36, 18)
gun  = Weapon("Gun", 56, 26)
beam  = Weapon("Beam", 60, 32)
dummy  = Weapon("Dummy", 20, 120)
blacksmith = Shop("Blacksmith", [dagger,sword,gun,beam,dummy])

user = Game()
user.validating_userold()
user.continue_act()
user.dekakary_welcome()
user.continue_act()

hero = user.choosing_hero()
user.continue_act()

user.how_to_play()
user.continue_act()

##Entering Town Hall --- Game Start!
lounge()

##Exit Game Conditioon
exit()