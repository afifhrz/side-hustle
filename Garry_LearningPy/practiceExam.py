# number 3
def Simpson13(fcn,a,b,dx):
    ''' Description:  Calculate the integral of the function fcn using simpsons 1/3 rule
        Parameters: fcn = function name
                    a = lower bound
                    b = upper bound
                    n = number of subintervals
        Returns: integral value
    '''

    # Calculate n
    n = int((b-a)/dx)
    
    # Finding sum 
    sum = fcn(a) + fcn(b)

    # ---------- Calculating the summation 

    for i in range(1,n):
        k = a + i*dx
        
        if i%2 == 0:
            sum = sum + 2 * fcn(k)
        else:
            sum = sum + 4 * fcn(k)

    sum = sum * dx/3
    
    return sum
import numpy as np
import math

fcn = lambda x: np.exp(math.sin(x))
# print(Simpson13(fcn,1,4,0.05))

# number 4
def findRoot(f, xL, xU, tolx, tolf): # your code goes here
    xF= (2*xL+3*xU)/5
    counter = 0
    while True:
        counter +=1
        if abs(f(xF)) < tolf and (xU-xL) < tolx:
            break
        
        if f(xF) > 0 and f(xU) > 0:
            xU = xF
        else:
            xL = xF
        
        xF= (2*xL+3*xU)/5
    return xF, counter

fcn = lambda x: np.exp(math.sin(x))-1
xL = 4
xU = 2 
tolx = 1e-2 
tolf = 1e-5 
# root = findRoot(fcn, xL,xU, tolx, tolf) 
# print(root)
        
# number 5
def ElementWiseMult(A,B):
    if A.shape != B.shape:
        return np.array([[]])
    
    result = []
    for row in range(A.shape[0]):
        temp = []
        for col in range(A.shape[1]):
            temp.append(A[row][col]*B[row][col])
        result.append(temp)
    
    return np.array(result)

A = np.array([[1,2,3], [4,0,2]])
B = np.array([[1,-1,0], [2,0,1]])

print(ElementWiseMult(A,B))