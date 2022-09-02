class Hero:

    # CLASS ATTRIBUTES
    def __init__(self, name, health, money, role, armor, weapons, items): 
        self.name = name
        self.health = health
        self.money = money
        self.role = role
        self.armor = armor 
        self.weapons = weapons # Instances will use a list to hold more than one weapon 
        self.items = items # Instances will use a list to hold more than one item

    # CLASS METHOD/ACTION
    def attack (self):

        print("You have the following weapons:")
        weaponoptions = [] # List of Dictionaries to store dictionary versions of hero1 weapon instances (ie wand, dagger, shortsword)
        
        for weapon in self.weapons: # weapon is temporary for the loop and replaces the instance name of weapons (ie wand.name becomes weapon.name)
            print(f"- {weapon.name} does {weapon.damage} damage")
            weapon_dictionary = weapon.__dict__ # Converts the weapon instances into dictionaries
            weaponoptions.append(weapon_dictionary) # Adds each weapon dictionary into the weaponoptions list 

        selection = True  # Flag to ensure the user has the weapon they select
        while selection:
            selectweapon = input("\nWhich weapon will you use to attack: ")

            for weapon in weaponoptions: # Loop to make sure selectweapon is one of the weapon options
                
                if weapon["name"] == selectweapon.title(): # Looks in each weapon's name key to see if it matches selectweapon input
                    monster1.health = monster1.health - weapon["damage"] # Subtracts the weapon damage from monster1
                    print(f"Your", weapon["name"], "did" , weapon["damage"], "damage.")
                    print(f"The {monster1.name} now has {monster1.health} health remaining.")
                    break               

            if monster1.health <= 0:
                print(f"Nice work! You defeated the {monster1.name}.")
                break

class Monster:

    # CLASS ATTRIBUTES
    def __init__(self, name, health, money, armor, weapons, items): 
        self.name = name
        self.health = health
        self.money = money
        self.armor = armor 
        self.weapons = weapons # Uses a list to hold more than one
        self.items = items # Uses a list to hold more than one


class Weapon:

    # CLASS ATTRIBUTES
    def __init__(self, name, value, damage): 
        self.name = name
        self.value = value
        self.damage = damage


# INSTANCE CREATION
wand = Weapon("Fire Wand", 20, 7)
dagger = Weapon("Basic Dagger", 10, 2)
shortsword = Weapon("Short Sword", 15, 5)

hero1 = Hero("Gandalf", 50, 100, "Wizard", "Robe", [dagger, wand], ["Diamond", "Key"])
hero1.weapons.append(shortsword) # Adds the shortsword instance to the hero's weapons attribute
monster1 = Monster("Goblin", 20, 5, "None", [dagger, shortsword], ["Necklace", "Ring"])

# RUNNING THE PROGRAM
print(f"You are a {hero1.role} named {hero1.name} and you are fighting a {monster1.name}.")
hero1.attack() # The hero1 attack method/action is executed