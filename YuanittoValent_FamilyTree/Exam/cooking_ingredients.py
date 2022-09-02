def get_dishes(cook_string):

    cook_dict = {
        'P':[2,1,1,1],
        'D':[2,2,2,2],
        'C':[1,3,0,0],
    }
    
    #check how many dishes
    number_of_dishes = 0
    index_store = []
    code_dish = []
    for index, letter in enumerate(cook_string):
        if letter == 'P' or letter == 'D' or letter == 'C':
            number_of_dishes += 1
            code_dish.append(letter)
            index_store.append(index)

    #store the composition
    dish_composition = []
    for dish in range(number_of_dishes):
        if dish == 0:
            dish_composition.append(cook_string[0:index_store[0]])
        else:
            dish_composition.append(cook_string[index_store[dish-1]+1:index_store[dish]])
    
    #convert the composisition
    dish_dict = []
    for dish in range(number_of_dishes):
        eggs = 0
        milks = 0
        flour = 0
        sugar = 0
        for letter in dish_composition[dish]:
            if letter == 'E':
                eggs += 1
            elif letter == 'M':
                milks += 1
            elif letter == 'F':
                flour += 1
            elif letter == 'S':
                sugar += 1
        dish_dict.append([eggs,milks,flour,sugar])

    #check the dish
    result = [0]*4
    for dish in range(number_of_dishes):
        value = True
        for index, recipe in enumerate(dish_dict[dish]):
            if cook_dict[code_dish[dish]][index] > dish_dict[dish][index]:
                value = False
        if value:
            if code_dish[dish] == 'P':
                result[0]+=1
            elif code_dish[dish] == 'D':
                result[1]+=1
            if code_dish[dish] == 'C':
                result[2]+=1
        else:
            result[3]+=1
    
    return result