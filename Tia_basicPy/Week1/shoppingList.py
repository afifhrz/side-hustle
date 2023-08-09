CHOCOLATE_PEANUT_BUTTER_SHAKE = ('chocolate peanut butter banana shake', '1 large banana,2 tbsp peanut butter,2 pitted dates,1 tbsp cacao powder,240 ml almond milk,0.5 cup ice,1 tbsp cocao nibs,1 tbsp flax seed')
BROWNIE = ('chocolate brownies', '2 tbsp flaxseed,200 g dark chocolate,0.5 tsp coffee granules,80 g Nuttelex,125 g self-raising flour,70 g ground almonds,50 g cocoa powder,0.2 tsp baking powder,250 g sugar,1.5 tsp vanilla extract')
SEITAN = ('seitan','1 cup vital wheat gluten,0.20 cup chickpea flour,1 tsp onion powder,1 tsp garlic powder,0.5 tsp salt,0.75 cup water,6 cup broth,0.5 medium onion,1 large carrot,1 stalk celery,0.3 cup soy sauce')
CINNAMON_ROLLS = ('cinnamon rolls','480 ml almond milk,115 g Nuttelex,50 g sugar,7 g active dry yeast,5.5 cup flour,1 tsp salt,170 g Nuttelex,165 g brown sugar,2 tbsp cinnamon,160 g powdered sugar,30 ml almond milk,0.5 tsp vanilla extract')
PEANUT_BUTTER = ('peanut butter', '300 g peanuts,0.5 tsp salt,2 tsp oil')
MUNG_BEAN_OMELETTE = ('omelette','1 cup mung bean,0.5 tsp salt,0.75 tsp pink salt,0.25 tsp garlic powder,0.25 tsp onion powder,0.125 tsp pepper,0.25 tsp turmeric,1 tsp oil,1 cup soy milk')

def recipe_ingredients (recipe):
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
    
generate_shopping_list([PEANUT_BUTTER,PEANUT_BUTTER,MUNG_BEAN_OMELETTE])