# Problem 3:

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# ----------------------------------------------------------------------------

# Solution:
    
# Applying the Augmented Sieve of Eratosthenes Algorithm - here we define our 
# function to also calculate the multiplicity of a prime number which is not needed
# for this problem but we do for completion purposes:

from math import floor  
from itertools import groupby  
    
def sieve(n):
    factors = []
    p = 2
    while p <= floor(n**0.5):
        if n % p:
            p += 1
        else:
            n //= p
            factors.append(p)
    if n != 1:
        factors.append(n)
    factors_and_multiplicity = [(k, len(list(g))) for k, g in groupby(factors)]
    return factors_and_multiplicity

print(sieve(600851475143)[-1][0]) # to get the largest prime factor due to how 
                                  # our function works - it finishes its 
                                  # iteration with the largest one
    
    

