# write a script to find max value

# a = [1,2,3]
# temp = -99
# for i in range(len(a)):
#     if temp < a[i]:
#         temp = a[i]
        
# print(temp)

def mystery(x):
    print(x)
    if len(x) == 1:
        return x[0]
    else:
        
        y = mystery(x[1:])
        # y = mystery([2,1])
        # y = 2
        # x = [3,2,1]
        
        print(y)
        if x[0] < y:
            return y
        else:
            return x[0]
        
print("value akhir",mystery([6,5,4,3,2,1]))