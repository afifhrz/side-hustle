recipes = [
    ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil'), 
    ('cinnamon rolls', '480 ml almond milk,115 g Nuttelex,50 g sugar,7 g active dry yeast,5.5 cup flour,1 tsp salt,170 g Nuttelex,165 g brown sugar,2 tbsp cinnamon,160 g powdered sugar,30 ml almond milk,0.5 tsp vanilla extract')
    ]

def find_recipe(recipe_name, recipes):
    '''FIND RECIPE'''
    for i in recipes:
        if recipe_name == i[0]:
            return i
    return None

print(find_recipe('cinnamon rolls', recipes))