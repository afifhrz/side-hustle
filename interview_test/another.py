from copy import deepcopy
def merge_two_list(first, second):
    result = []
    lenLoop = len(first) + len(second)
    checkIndex = 0
    firstCondition = True
    lastIndex = 0
    index = 0
    while checkIndex < lenLoop:
        if firstCondition:
            # if first[index] <= second[lastIndex]:
            #     result.append(first[index])
            #     if index + 1 < len(first):
            #         index += 1
            #     else:
            #         firstCondition = False
            #         temp = lastIndex 
            #         lastIndex = index
            #         index = temp
            # else:
            #     firstCondition = False
            #     temp = lastIndex 
            #     lastIndex = index
            #     index = temp
        else:
            # if first[lastIndex] <= second[index]:
            #     result.append(second[index])
            #     index += 1
            # else:
            #     firstCondition = True
            #     temp = lastIndex 
            #     lastIndex = index
            #     index = temp
        
        checkIndex += 1
    return result
        
        

first_list = [1,2,3]
second = [1,5,6]    

print(merge_two_list(first_list,second))