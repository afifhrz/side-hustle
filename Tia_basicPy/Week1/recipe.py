# sequence data type
# list -> a = [0, 1, 2, 3] , a[0]
# tuple -> a = (0, 1, 2, 3) , a[0]
# string -> a = "aku dan kamu", a[0] = "a"

split = ["300 g peanuts", "0.5 tsp salt", "2 tsp oil"]
result = []
for a in range(len(split)):
    temp = split[a].split(" ")
    temp[0] = float(temp[0])
    result.append(tuple(temp))

for a in split:
    temp = a.split(" ")
    temp[0] = float(temp[0])
    result.append(tuple(temp))

namaku = "abcdefghijkl"

# for loop_num in range(len(namaku)):
#     print(namaku[loop_num])
    
# for loop_num in namaku:
#     print(loop_num)

print(list(range(10)))