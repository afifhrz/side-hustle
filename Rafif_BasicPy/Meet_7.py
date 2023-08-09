f = open("twisted_numbers.txt", "r")
f = f.read()

d = eval(f)

def recover(list_keys):
    result = {}
    for key in list_keys:
        if str(key) in d.keys():
            result[key]=d[str(key)]
    return result

print(recover([-5, 1235, 4000.5]))
print(recover([]))
print(recover([100.6, 5001]))