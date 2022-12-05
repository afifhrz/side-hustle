# # def spam(divideBy):
# #     return 42 / divideBy

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

# spam(0)

# import time, sys
# indent = 0 # How many spaces to indent.
# indentIncreasing = True # Whether the indentation is increasing or not.

# try:
#     while True: # The main program loop.
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1) # Pause for 1/10 of a second.

#         if indentIncreasing:
#             # Increase the number of spaces:
#             indent = indent + 1
#             if indent == 20:
#                 # Change direction:
#                 indentIncreasing = False

#         else:
#             # Decrease the number of spaces:
#             indent = indent - 1
#             if indent == 0:
#                 # Change direction:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()

# spam = ['cat', 'bat', 'rat', 'elephant']

# print(spam[1])

# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for i in range(len(supplies)):
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for item in supplies:
#     print('Index  in supplies is: ' + item)

# supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
# for index, item in enumerate(supplies):
#     print('Index ' + str(index) + ' in supplies is: ' + item)

# print(list(enumerate(supplies)))

# spam = ['hello', 'hi', 'hi', 'heyas']

# print(spam[0])
# print(spam.index('hi'))

spam = ['cat', 'bat', 'rat', 'bat']
spam.remove('bat')

print(spam)