## COMP1730/6730 S2 2022 - Homework 3
# Submission is due 09:00am, Monday the 29th of August, 2022.

## YOUR ANU ID: u9207147
## YOUR NAME: abx

## You should implement two functions number_to_string(m,n) and
## string_to_number(s). The `pass` statements are only a placeholder 
## which you should replace with your implementation. The first function,
## number_to_string(m,n) must return a string representing the rational
## number m/n; the second function, string_to_number(s), must return a pair
## of mutally prime positive integers m and n in a form of two-tuple (m,n)

def number_to_string(m, n):
    pass

def string_to_number(s):
    pass

def test_number_number_to_string():
    '''
    This function runs a number of tests of the number_to_string function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''
    assert number_to_string(1, 1) == ''
    assert type(number_to_string(1, 1)) == str
    assert number_to_string(2, 1) == 'R'
    assert type(number_to_string(2, 1)) == str
    assert number_to_string(3, 1) == 'RR'
    assert type(number_to_string(3, 1)) == str
    assert number_to_string(4, 1) == 'R'*3
    assert type(number_to_string(1, 4)) == str
    assert number_to_string(3,11) == 'LLLRL'
    assert type(number_to_string(89, 55)) == str
    assert number_to_string(89, 55) == 'RLRLRLRLR'
    assert type(number_to_string(8, 111)) == str
    assert number_to_string(144, 89) == 'RL' * 5
    print("all tests passed")

def test_string_to_number():
    '''
    This function runs a number of tests of the string_to_number function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''
    assert string_to_number('') == (1,1)
    assert type(string_to_number('')) == tuple
    assert string_to_number('L') == (1,2)
    assert type(string_to_number('R')) == tuple
    assert string_to_number('LR') == (2,3)
    assert type(string_to_number('RL')) == tuple
    assert string_to_number('RL'*5) == (144,89)
    assert type(string_to_number('LR'*10)) == tuple
    assert string_to_number('LLLLLLLLLLL') == (1,12)
    assert string_to_number('RRRRRRRRRR') == (11,1)
    print("all tests passed")
