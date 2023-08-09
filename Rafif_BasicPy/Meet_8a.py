def alternating_harmonic_series(bound=0.1):
    k = 1
    a_k1 = 1000000
    L = 0
    while abs(a_k1) > bound:
        a_k = (-1)**(k+1)/k
        a_k1 = (-1)**(k+2)/(k+1)
        L += a_k
        k+=1
        
    return L

print(alternating_harmonic_series())
print(alternating_harmonic_series(0.001))
print(alternating_harmonic_series(0.00001))