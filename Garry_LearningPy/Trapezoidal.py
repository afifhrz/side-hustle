import numpy as np
import math 

def Trapz(fcn,a,b,n):
    ''' Calculate the integral of the function fcn using trapezoidal rule
        Parameters: fcn = function name
                    a = lower bound
                    b = upper bound
                    n = number of subintervals
        Returns: integral value        '''

    # the subinterval size
    dx = (b-a)/n

    # Finding sum 
    sum = fcn(b) + fcn(a)
    
    for i in range(1,n):
        k = a + i*dx
        sum = sum + 2 * fcn(k)
        
    # Finding final integration value
    sum = sum * dx/2
    
    return sum

def Simpson13(fcn,a,b,n):
    ''' Description:  Calculate the integral of the function fcn using simpsons 1/3 rule
        Parameters: fcn = function name
                    a = lower bound
                    b = upper bound
                    n = number of subintervals
        Returns: integral value
    '''

    # Calculate dx
    dx = (b-a)/n
    
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

def Trapz_xy(X,Y):
    ''' Calculate the integral of the function fcn using trapezoidal rule
        Parameters: fcn = function name
                    a = lower bound
                    b = upper bound
                    n = number of subintervals
        Returns: integral value        '''

    sum = 0
    
    for i in range(0,len(X)-1):
        dx = X[i+1] - X[i]
        sum = sum + dx * (Y[i]+Y[i+1])/2
    
    return sum
# --------------------- Main program --------------------

# defining function using lambda function:
miu = 0
sigma = 1
probability_function = lambda x: (math.e**(-((x-miu)**2)/(2*(sigma**2))))/(sigma*math.sqrt(2*math.pi))

# the integration parameters
a=int(input("Lower Bound:"))
b=int(input("Upper Bound:"))
n=100  # number of sub-interval

x = np.linspace(a,b,n+1)
y = np.linspace(a,b,n+1)

for i in range(len(y)):
    y[i] = probability_function(x[i])

print("n = {}, integral using Trapz rule= {}".format(n, Trapz(probability_function,a,b,n)))
print("n = {}, integral using Simpson13 rule= {}".format(n, Simpson13(probability_function,a,b,n)))
print("n = {}, integral using Trapz_xy rule= {}".format(n, Trapz_xy(x,y)))