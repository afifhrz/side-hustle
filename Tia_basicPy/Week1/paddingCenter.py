def display_ingredients(splitted_recipe):
    
    # get max character
    qMax = 0
    sizeMax = 0
    itemMax = 0
    
    sort = sorted(splitted_recipe, key=lambda x: x[2])
    print(sort)
    
    for item in sort:
        if qMax < len(str(item[0])):
            qMax = len(str(item[0]))
        
        if sizeMax < len(str(item[1])) and len(str(item[1]))%2==1:
            sizeMax = len(str(item[1]))
            
        if itemMax < len(str(item[2])):
            itemMax = len(str(item[2]))
    
    sizeMax += 4
    
    # padding
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

display_ingredients([
    (1.0, 'large', 'banana'),
    (2.0, 'tbsp', 'peanut butter'),
    (2.0, 'pitted', 'dates'),
    (1.0, 'tbsp', 'cacao powder'),
    (240.0, 'ml', 'almond milk'),
    (570.0, 'g', 'Nuttelex'),
    (0.5, 'cup', 'ice'),
    (1.0, 'tbsp', 'cocao nibs'),
    (1.0, 'tbsp', 'flax seed'),
    (1.0, 'tbsp', 'flax seed yeast'),
    ])