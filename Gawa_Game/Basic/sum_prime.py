def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  # since all primes > 3 are of the form 6n ± 1
  # start with f=5 (which is prime)
  # and test f, f+2 for being prime
  # then loop by 6. 
  f = 5
  while f <= r:
    # print('\t',f)
    if n % f == 0: return False
    if n % (f+2) == 0: return False
    f += 6
  return True

def sum_prime_factor(n):
    # example input 9
    # return 3
    # example input 15
    # return 8
    # example input 60 = 2 3 5
    # return 10
    result = 0
    for number in range(1,n):
        if is_prime(number) and n % number == 0:
            result += number
    
    return result

print(sum_prime_factor(9))
print(sum_prime_factor(15))
print(sum_prime_factor(60))