def sum_of_digits(x):
    string_temp = str(x)
    sum = 0
    if not string_temp:
        return sum
    if string_temp[-1].isdigit():
        sum += int(string_temp[-1])
    sum += sum_of_digits(string_temp[:-1])
    return sum

print(sum_of_digits(1.234))
print(sum_of_digits(-4.321))