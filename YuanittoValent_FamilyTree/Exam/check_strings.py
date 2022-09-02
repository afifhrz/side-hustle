
def count_letters(words):
    temp = 0
    if words != []:
        if len(words) != 1:
            count_letters(words)
        else:
            return len(words[0])
    return temp

print(count_letters([]))
print(count_letters(['Abby']))
print(count_letters(['abby']))
print(count_letters(['abby','Abby','flab']))