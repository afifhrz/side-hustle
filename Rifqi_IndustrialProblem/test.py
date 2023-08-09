import math
feeder_array = [11, 7, 25, 5, 33, 14, 9]
result_poin_combination = []
index_combination = []

count = math.pow(2,len(feeder_array))

for i in range(0,int(count)):
    temp_poin=0
    index_temp=[]
    temp=''
    print("ini nilai i:", i)
    for j in range(0,len(feeder_array)):
        
        # print(i<<j)
        print(i & (1<<j))
        # print((i & (1<<j)) != 0)
        if ((i & (1<<j)) != 0):
            temp+=str(feeder_array[j])+' '
            temp_poin+=feeder_array[j]
            index_temp.append(feeder_array[j])

    result_poin_combination.append(temp_poin)
    # index_combination.append(index_temp)

for i in range(0,int(count)):
    temp_poin=0
    index_temp=[]
    temp=''
    print("ini nilai i:", i)
    for j in range(0,len(feeder_array)):
        
        # print(i<<j)
        print(i & (1<<j))
        # print((i & (1<<j)) != 0)
        if ((i & (1<<j)) != 0):
            temp+=str(feeder_array[j])+' '
            temp_poin+=feeder_array[j]
            index_temp.append(feeder_array[j])

    # result_poin_combination.append(temp_poin)
    index_combination.append(index_temp)
    # print(temp_poin)
    # print(temp)

# print('selesai')
# print(result_poin_combination)
# print()
# print(index_combination)

# print(result_poin_combination.index(50))
# print(index_combination[result_poin_combination.index(50)])