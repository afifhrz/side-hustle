def alternating_harmonic_series(bound=0.1):
    k = 1/bound - 1
    L = (-1)**(k+1)/k
    return L

print(alternating_harmonic_series())
print(alternating_harmonic_series(0.001))
print(alternating_harmonic_series(0.00001))