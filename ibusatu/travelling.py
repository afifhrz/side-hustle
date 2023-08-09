def costTravel(route):
    index = set()
    val_min = 0
    for i in range(len(route)):
        copyList = route[i].copy()
        min_ = min(route[i])
        copyIndex = route[i].index(min_)
        while True:
            if copyIndex not in index:
                index.add(copyIndex)
                val_min += min_
                break
            else:
                copyList.pop(copyIndex)
                min_ = min(copyList)
                copyIndex = route[i].index(min_)
            
    return val_min
    
T = int(input())
for i in range(T):
    M = int(input())
    route = []
    for j in range(M):
        input_text = input().split(" ")
        for item in range(len(input_text)):
            if input_text[item] == "0":
                input_text[item] = float('inf')
            else:
                input_text[item] = int(input_text[item])
        route.append(input_text)
    print(costTravel(route))
    
