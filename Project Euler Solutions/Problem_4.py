import time

# Problem 4:
    
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

# ----------------------------------------------------------------------------

# 1st Way - Naive:
    
from itertools import combinations_with_replacement as c

t0 = time.time()
temp = [pair[0]*pair[1] for pair in c(range(100, 1000), 2)]
print(max([n for n in temp if str(n)[:3] == str(n)[:-4:-1]])) # Answer: 906609 = 913*993
t1 = time.time()
diff1 = t1-t0

# ----------------------------------------------------------------------------

# 2nd Way - Mathematical Approach:

# We note that if the number we are trying to find is let's say N, then because N is
# a palindrome, we have:

# First of all N is a 6-digit palindrome due to the fact that 111111 which is a
# 6 digit palindrome is the product of 3 digit numbers; 111111 = 231 * 481

# N = [abccba]_{10} = 100000a + 10000b + 1000c + 100c + 10b + a
#   = 100001a + 10010b + 1100c = 11(9091a + 910b + 100c) := a*b

# Let's say that a and b above are the two 3 digit numbers that have a product equal
# to N. Due to Euiclid's Lemma, because 11 is a prime number then 11 divides either a
# or b (or both). So if 11 DOES NOT divide a then it MUST divide b, which gives less values
# to check for each value of a not divisible by, instead of taking all the products
# of combination of a and b for a,b in {100,...,999}.
# Due to also trying to find the BIGGEST such number we begin a = 999 instead of 100
# to minimize futile checks for if a product is larger than the one that we already picked

t2 = time.time()
a = 999
largest = 0
while a >= 100:
    if a % 11 == 0: # so a is divisible by 11
        b = 999 # begin the checks from the largest one
        db = -1 # the increments are by -1 due to b not HAVING to be divisible by 11
    else:
        b = 990 # largest 3-digit number divisible by 11
        db = -11 # the increments have to be by -11 due to b, needing to be divisible by 11 because a isn't!
    while b >= a: # a*b and b*a is the same, so we just need to check the cases where a*b is our number
        if a*b <= largest:
            break # since we start from 999 (or 990) for b, if a*b are less than the largest number we have, in these
                  # extreme cases, then it's always going to be less than it, because we substract from b; db in each iteration
        if str(a*b) == str(a*b)[::-1]:
            largest = a*b
        b += db
    a -= 1
t3 = time.time()
diff2 = t3-t2
print(largest)

print(f"The 1st way took as much time as a {100*diff1/diff2:.0f}% increase from the time it took for the 2nd way to complete")