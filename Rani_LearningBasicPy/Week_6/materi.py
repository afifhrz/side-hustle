data = [
    [0, 1, 2],
    [3, 5, 6]
]

# print(data[0][2])

# first_col = []
# for rani in data:
#     print(rani)
#     first_col.append(rani[1])
# 

# print(first_col)

first_col = [ rani[0] for rani in data ]

print(first_col)