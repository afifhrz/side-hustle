from constants import *

# Write your functions here
#5.1.1-------------HOURS
hours = 126
print("Hours:", float(hours))

#5.1.2-------------GET RECIPE NAME
def get_recipe_name(recipe: tuple[str, str]) -> str:
    '''GET RECIPE NAME'''
    get_recipe_name = recipe[0]
    return get_recipe_name

#5.1.3--------------GET RAW INGREDIENT
def parse_ingredient(raw_ingredient_detail: str) -> tuple[float, str, str]:
    '''GET RAW INGREDIENT'''
    split = raw_ingredient_detail.split(" ", maxsplit=2)
    result = float(split[0]), str(split[1]), str(split[2])
    return result

#5.1.4--------------CREATE RECIPE 
def create_recipe() -> tuple[str, str]:
    '''CREAT RECIPE'''
    create_recipe = input('Please enter the recipe name: ')
    ingredient = True
    save_ingredient = []
    while ingredient:
        ingredient_name = input('Please enter an ingredient: ')
        if (len(ingredient_name)) == 0:
            convert = tuple(save_ingredient)
            break
        save_ingredient.append(ingredient_name)
    return create_recipe, ','.join(tuple(save_ingredient))
       

#5.1.5--------------RECIPE INGREDIENTS 
def recipe_ingredients(recipe: tuple[str,str]) -> tuple[tuple[float,str,str]]:
    '''RECIPE INGREDIENTS'''
    split = recipe[1].split(",")
    result = []
    for a in split:
        temp = a.split(" ")
        temp[0] = float(temp[0])
        if len(temp) == 4:
            temp[2] = temp[2] + " " + temp[3]
            temp.pop(3)
        result.append(tuple(temp))
    return tuple(result)

#5.1.6--------------ADD RECIPE - failed
def add_recipe(new_recipe: tuple[str, str], recipes: list[tuple[str, str]]) -> None:
    '''ADD RECIPE'''
    recipes.append(tuple(new_recipe))
    return recipes

#5.1.7-------------FIND RECIPE - try again kacau
def find_recipe(recipe_name: str, recipes: list[tuple[str, str]]) -> tuple[str, str] | None:
    '''FIND RECIPE'''
    for i in recipes:
        print(i)
        if recipe_name == i[0]:
            return i
    return None

#5.1.8----------REMOVE RECIPE -  try again
def remove_recipe(name: str, recipes: list[tuple[str, str]]) -> None:
    '''REMOVE RECIPE'''
    for i, recipe in enumerate(recipes):
        if recipe[0] == name:
            del recipes[i]
            break
    return recipes


#5.1.9------GET INGREDIENT AMOUNTS -  try again CHECK!!!
def get_ingredient_amount(ingredient: str, recipe: tuple[str, str]) -> tuple[float,str] | None:
    '''GET INGREDIENT AMOUNTS'''
    ingredients = recipe[1].split(',')
    for i in ingredients:
        if ingredient in i:
            number, word = i.split()[:2]
            return float(number), word
        return None

#5.1.10------ADD SHOPPING LIST
def add_to_shopping_list(ingredient_details: tuple[float, str, str], shopping_list: list[tuple[float, str, str] | None]) -> None:
    '''ADD TO SHOPPING LIST'''
    status_append = False
    for i in range(0, len(shopping_list)):
        if ingredient_details[2] == shopping_list[i][2]:
            count = ingredient_details[0] + shopping_list[i][0]
            update = (count, ingredient_details[1], ingredient_details[2])
            shopping_list[i] = update
            status_append = True
    if len(shopping_list) == 0:
        status_append = True
        shopping_list.append(ingredient_details)
    if not status_append:
        shopping_list.append(ingredient_details)
    return shopping_list

#5.1.11------REMOVE FROM SHOPPING LIST
def remove_from_shopping_list(ingredient_name: str, amount: float, shopping_list: list) -> None:
    '''REMOVE FROM SHOPPING LIST'''
    #print(shopping_list[2][2])
    for i in range(0, len(shopping_list)):
        #print(i)
        if ingredient_name == shopping_list[i][2]:
            count = shopping_list[i][0] - amount
            if count <= 0:
                shopping_list.pop(i)
            else:
                update = (count, shopping_list[i][1], shopping_list[i][2])
                shopping_list[i] = update
            break
    return shopping_list
         
#5.1.12------GENERATE SHOPPING LIST
def generate_shopping_list(recipes):
    '''GENERATE SHOPPING LIST'''
    shopping_list = []
    temp = []
    for a in recipes:
        temp.append(recipe_ingredients(a))
    for b in temp:
        for ingr in b:
            list_item = []
            for item in shopping_list:
                if item[2]:
                    list_item.append(item[2])
            if ingr[2] in list_item:
                indexNum = list_item.index(ingr[2])
                shopping_list[indexNum][0] += ingr[0]
            else:
                shopping_list.append(list(ingr))
    
    for index,item in enumerate(shopping_list):
        shopping_list[index] = tuple(shopping_list[index])
    return shopping_list

#5.1.13-------DISPLAY INGREDIENT
def display_ingredients(shopping_list):
    '''DISPLAY INGREDIENT'''
    qMax = 0
    sizeMax = 0
    itemMax = 0

    sort = sorted(shopping_list, key=lambda x: x[2])
    #print(sort)

    for item in sort:
        if qMax < len(str(item[0])):
            qMax = len(str(item[0]))

        if sizeMax < len(str(item[1])) and len(str(item[1]))%2==1:
            sizeMax = len(str(item[1]))

        if itemMax < len(str(item[2])):
            itemMax = len(str(item[2]))
    
    sizeMax += 4

    for item in sort:
        first_item = "|"+str(item[0]).rjust(qMax+1)+" |"

        if len(str(item[1]))%2==1:
            spaceRest = sizeMax - len(str(item[1]))
            second_item = str(item[1]).rjust(len(str(item[1]))+(spaceRest//2)).ljust(len(str(item[1]))+(spaceRest))
        else:
            spaceRest = sizeMax - len(str(item[1]))
            second_item = str(item[1]).rjust(len(str(item[1]))+(spaceRest//2)).ljust(len(str(item[1]))+(spaceRest))

        third_item = "| "+str(item[2]).ljust(itemMax+2)+"|"
        print(first_item+second_item+third_item)
    
#5.1.14------SANITISE COMMAND
def sanitise_command(command: str) -> str:
    '''SANITISE COMMAND'''
    command = command.lower().strip()
    if command.split(" ")[0] == "rm" and command.split(" ")[1] == "-i":
        join =  ''.join(command)
    else:
        join =  ''.join(filter(lambda cek: not cek.isdigit(), command))
    return join


def main():
    """ Write your docstring """
    # cook book
    recipe_collection = [
        CHOCOLATE_PEANUT_BUTTER_SHAKE, 
        BROWNIE, 
        SEITAN, 
        CINNAMON_ROLLS, 
        PEANUT_BUTTER, 
        MUNG_BEAN_OMELETTE
    ]
    
    # Write the rest of your code here

    """Help, Quit, Shopping Cart List"""
    shopping_cart = []
    list_shopping = []
    user_input = sanitise_command(input("Please enter a command: "))
    while user_input != "q":
        if user_input == "h":
            print(HELP_TEXT)
        elif user_input == "ls":
            if shopping_cart: 
                print(shopping_cart)
            else:
                print("No recipe in meal plan yet.")
        elif user_input =="ls -a":
            for i in recipe_collection:
                print(get_recipe_name(i))


#=======add recipe
        elif user_input.split(" ")[0] == "add":
            getOption = []
            for item in recipe_collection:
                getOption.append(item[0])
            if user_input[4:] in getOption:
                getIndex = getOption.index(user_input[4:])
                shopping_cart = add_recipe(recipe_collection[getIndex], shopping_cart)
            else:
                print("Recipe does not exist in the cook book.\nUse the mkrec command to create a new recipe.")             

                
##        elif user_input.split(" ")[0] == "add":
##            if user_input == "add peanut butter":
##                shopping_cart = add_recipe(PEANUT_BUTTER, shopping_cart)
##            elif user_input == "add chocolate brownies":
##                shopping_cart = add_recipe(BROWNIE, shopping_cart)
##            elif user_input == "add seitan":
##                shopping_cart = add_recipe(SEITAN, shopping_cart)
##            elif user_input == "add cinnamon rolls":
##                shopping_cart = add_recipe(CINNAMON_ROLLS, shopping_cart)
##            elif user_input == "add omelette":
##                shopping_cart = add_recipe(MUNG_BEAN_OMELETTE, shopping_cart)
##            elif user_input == "add chocolate peanut butter shake":
##                shopping_cart = add_recipe(CHOCOLATE_PEANUT_BUTTER_SHAKE, shopping_cart)
##            else:
##                print("Recipe does not exist in the cook book.\nUse the mkrec command to creat a new recipe.")


#====remove ingredient from shopping list
        elif user_input.split(" ")[0] == "rm" and user_input.split(" ")[1] == "-i":
            ingredients = user_input.split(" ")[2]
            qty = user_input.split(" ")[3]
            for i in list_shopping:
                if ingredients == i[2]:
                    list_shopping = remove_from_shopping_list(ingredients, float(qty), list_shopping)
            
##         elif user_input.split(" ")[0] == "rm" and user_input.split(" ")[1] == "-i":
##                #print(user_input.split(" "))
##                ingredients = user_input.split(" ")[2]
##                qty = user_input.split(" ")[3]
##                #print(list_shopping)
##                for i in list_shopping:
##                    #print(list_shopping)
##                    if ingredients == i[2]:
##                        list_shopping = remove_from_shopping_list(ingredients, float(qty), list_shopping)

#====remove recipe
        elif user_input.split(" ")[0] == "rm":
            getopt = []
            #print(user_input[3:])
            for item in recipe_collection:
                getopt.append(item[0])
            if user_input[3:] in getopt:
                getOut = getopt.index(user_input[3:])
                #print(getOut)
                lis = remove_recipe(recipe_collection[getOut][0], shopping_cart)
            

        
##        elif user_input.split(" ")[0] == "rm":
##            if user_input == "rm peanut butter":
##                shopping_cart = remove_recipe(PEANUT_BUTTER[0], shopping_cart)
##            elif user_input == "rm chocolate brownies":
##                shopping_cart = remove_recipe(BROWNIE[0], shopping_cart)
##            elif user_input == "rm seitan":
##                shopping_cart = remove_recipe(SEITAN[0], shopping_cart)
##            elif user_input == "rm cinnamon rolls":
##                shopping_cart = remove_recipe(CINNAMON_ROLLS[0], shopping_cart)
##            elif user_input == "rm omelette":
##                shopping_cart = remove_recipe(MUNG_BEAN_OMELETTE[0], shopping_cart)
##            elif user_input == "rm chocolate peanut butter shake":
##                shopping_cart = remove_recipe(CHOCOLATE_PEANUT_BUTTER_SHAKE[0], shopping_cart)
                


#====generate a shopping list
        elif user_input == "g":
            temp = []
            for i in shopping_cart:
                #print(i)
                for item in recipe_ingredients(i):
                    temp = add_to_shopping_list(item,temp)
                   # print(item)
            display_ingredients(temp)
            list_shopping = temp

#====display shopping list
        elif user_input == "ls -s":
            display_ingredients(list_shopping)

#====create recipe
        elif user_input == "mkrec":
            recipe = create_recipe()
            #print(recipe)
            recipe_collection.append(recipe)

            
        user_input = sanitise_command(input("Please enter a command: "))



if __name__ == "__main__":
    main()

