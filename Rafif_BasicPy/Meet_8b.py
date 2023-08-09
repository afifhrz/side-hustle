def alternating_harmonic_series(bound=0.1):
    a_k1 = 1000000
    err = a_k1
    L = 0
    for k in range(1,abs(a_k1)):
        if abs(err) <= bound:
            break
        a_k = (-1)**(k+1)/k
        err = (-1)**(k+2)/(k+1)
        L += a_k
    return L

print(alternating_harmonic_series())
print(alternating_harmonic_series(0.001))
print(alternating_harmonic_series(0.00001))