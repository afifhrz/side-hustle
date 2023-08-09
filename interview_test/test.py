a = [3,1,4,1,2,5,2]

arr_size = len(a)
for i in range(arr_size):
    x = a[i] % arr_size
    a[x] = a[x] + arr_size
  
print("The repeating elements are : ")
for i in range(arr_size):
    if (a[i] >= arr_size*2):
        print(i, " ")