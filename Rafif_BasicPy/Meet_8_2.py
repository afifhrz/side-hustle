def sum_of_digits(x):
    string_temp = str(x)
    sum = 0
    for char in string_temp:
        if char.isdigit():
            sum += int(char)
    return sum

print(sum_of_digits(1.234))
print(sum_of_digits(-4.321))