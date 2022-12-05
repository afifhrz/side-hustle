# name = ''

# # while name != 'your name':
# #     print('Please type your name.')
# #     name = input()

# while True:
#     print('Please type your name.')
#     name = input()
#     if name == 'your name':
#         break

# print('Thank you!')

# name = "rafif"
# list_name = ['ra', 'fif', 'fi']
# dict_name = {}

# for word in name:
#     if word == "f":
#         break
#     print(word)

# for word in list_name:
#     print(word)

# import random
# # print(list(range(5)))
# for i in range(5):
#     print(random.randint(1, 10))

# i=0
# while i<5:
#     print(random.randint(1, 10))
#     i+=1

# astuti(x) = x**2

# astuti(2) = 2**2

# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there.')

# hello()

# def hello(name):
#     print('Hello, ' + name)

# hello('asafsf')

# def penjumlahan(a,b):
#     return a+b

# def perkaliann(a,b):
#     return a*b

# def pembagian(a,b):
#     return a/b

# def big_calculation(a,b):
#     c = penjumlahan(a, b)
#     print(c)
#     d = perkaliann(a, c)
#     print(d)
#     e = pembagian(a, d)
#     print(e)

# big_calculation(5, 3)

# def spam():
#     eggs = 31337
#     print(eggs)

# spam()
# eggs = 1
# print(eggs)

# def inipake_global():
#     eggs = 2
#     print(eggs)

# inipake_global()

# import math

# error = float(input("Enter an error bound :"))
# S0 = 4
# Sn = S0
# pola = 1
# pi = math.pi
# n = 1

# while abs(Sn-pi) >= error:
#     # do something
#     pola = pola + ((-1)**n)*(1/(2*n+1))
#     Sn = S0 * pola
#     n += 1

# print(Sn)

def pohon_faktor(number):   
    result = []
    for i in range(number//2):
        if i != 0 and number % i == 0:
            tuple_list = (i,number//i)
            result.append(tuple_list)
    return result
            
def minimal_sum(tuple_list):
    result = []
    for index, pasangan in enumerate(tuple_list):
        # print(index)
        # print(pasangan)
        sum = pasangan[0] + pasangan[1]
        result.append((sum,index))
    # print(result)
    return min(result)

def print_to_console(number):
    result = pohon_faktor(number)
    hasil = minimal_sum(result)
    
    # print(hasil)
    # print(hasil[1])
    # print(result)
    # print(result[hasil[1]])

    factor = result[hasil[1]]

    print(f"The pair of factors are {factor[0]} and {factor[1]}, giving the smallest sum {hasil[0]}.")

print_to_console(36)
# print_to_console(45)
# print_to_console(345)