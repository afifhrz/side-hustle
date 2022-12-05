# a = [1]

# a[:]=[]
# b = []

# print(a == b)

# a = [1,2,3,4,5,6]
# print(a)
# a[:]=[]
# # a = []
# print(a)

# def mult(lst, n):
#     lst = n * lst
    
# a = [1,2,3]
# mult(a,3)
# print(a)

# def mult(lst, n):
#     return n * lst
    
# a = [1,2,3]
# a = mult(a,3)
# print(a)

# def reverse(lst, parity):
#     even_list = lst[1::2].copy()
#     odd_list = lst[::2].copy()
    
#     if parity == 'odd':
#         odd_list.reverse()
#     elif parity == 'even':
#         even_list.reverse()
#     else:
#         print('Error: Unknown Parity')
    
#     result = []
#     for i in range(len(even_list)):
#         result.append(odd_list[i])
#         result.append(even_list[i])
        
#     return result

# a = list(range(1,11))
# print(a)

# a = reverse(a, 'even')
# print(a)

# a = reverse(a, 'odd')
# print(a)

# a = reverse(a, 'even')
# print(a)

# a = reverse(a, 'odd')
# print(a)

# a = reverse(a, 'neither')
# print(a)

# def factors(n):
#     result = []
    
#     if n < 0:
#         n = -1*n
        
#     for i in range(1,n+1):
#         if n%i == 0:
#             result.append(i)
#     return result

# print(factors(10))
# print(factors(100))
# print(factors(-25))

# def remove_specified_value(lst, target):
#     while target in lst:
#         lst.remove(target)
#     return lst

# a = [1, 2, 3, 1, 1, 2, 5, 4]
# print(remove_specified_value(a,1))

# b = [ 4 , 5 , [ 1 , 2 ] , [ 1 , 3 ] , [ 1 , 2 ] ]
# print(remove_specified_value(b,[1,2]))

# c = [2,2,2,2]
# print(remove_specified_value(c,1))
# print(remove_specified_value(c,2))

# def remove_specified_value(lst, target):
#     for item in lst:
#         if item == target :
#             lst.remove (item)
#     return lst
            
# a = [1,1]
# print(remove_specified_value(a,1))

# def remove_specified_value(lst, target):
#     for item in target:
#         while item in lst:
#             lst.remove(item)
#     return lst

# a = [ 1 , 2 , 3 , 1 , 2 , 3 , 4 , 3 , 1]
# print(remove_specified_value(a,[1,3]))

# b = [ [ 1 , 2 ] , [ [ 1 , 2 ] ] , [ 1 , 2 ] , 3 , [ 1 , 2 ] , 4]
# print(remove_specified_value(b,[[1,2],3]))

# def g(lst):
#     result = []
#     temp = []
#     for item in lst:
#         temp.append(item)
#         result.append(temp.copy())
#     return result

# print(g([1,2]))
# print(g(['a',[1,2],3]))

def rotate(lst, step=1):
    if step>=0:
        temp_list = lst[:step].copy()
        del lst[:step]
        
        for item in temp_list:
            lst.append(item)
    else:
        temp_list = lst[step:].copy()
        del lst[step:]
        
        for item in range(1,1+len(temp_list)):
            lst.insert(0,temp_list[-item])
    return lst

a = list(range(1,8))
print(rotate(a))
print(rotate(a, 4))
print(rotate(a, -4))
print(rotate(a, -1))
print(rotate(a, 0))