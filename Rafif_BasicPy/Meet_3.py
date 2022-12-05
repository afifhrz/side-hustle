def is_palindrome(s):
    palindrome = True
    i = 1
    for x in s:
        if x != s[-1*i]:
            palindrome = False
            break
        i+=1
    return palindrome

# Tn(f; a; b) = h 2 (f(x0) + 2f(x1) +    + 2f(xn􀀀1) + f(xn))

import math
def trapezoidal_rule(f, a, b, n=1000):
    
    jml_sisi_sejajar = 0
    h = (b - a)/n
    
    for i in range(n+1):
        x_k = a + i*h
        if i == 0:
            jml_sisi_sejajar = jml_sisi_sejajar + f(x_k)
        elif i == n:
            jml_sisi_sejajar = jml_sisi_sejajar + f(x_k)
        else:
            jml_sisi_sejajar += 2*f(x_k)
    
    return h / 2 * jml_sisi_sejajar

print(trapezoidal_rule(math.sin, 0, math.pi))
print(trapezoidal_rule(math.sin, 0, math.pi, 5000))
print(trapezoidal_rule(lambda x : x**2, 0, 1, 5000))