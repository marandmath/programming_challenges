# Problem 1:
    
# If we list all the natural numbers below 10 that are multiples of 3 or 5, 
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

# ----------------------------------------------------------------------------

# 1st way - Naive:
    
# print(sum([x for x in range(1, 1000) if x % 3 == 0 or x % 5 == 0]))

# ----------------------------------------------------------------------------

# 2nd way - Mathematical Approach:

# Notice that the numbers divisible by 3 or 5 between 1 and n are exactly the
# numbers divisible by 3 and the numbers divisible by 5, but due to double
# counting the numbers divisible by 15(=3*5) we take out the amount of numbers
# divisible by 15. So due to the divison algorithm / Zp partition of the integers
# there are exactly floor(n/3) numbers divisible by 3 between 1 and n (or n // 3)
# and so one and so forth for 5 and 15. Then these numbers are of the form 3*k
# for k between 1 and floor(n/3) so: 
# (Sum of numbers divisible by 3 between 1 and n) = 3*(1+2+...+floor(n/3))
# But 1+2+...+p = p(p+1)/2, so the answer to the problem has a closed form formula:
# 3p(p+1)/2 + 5q(q+1)/2 - 15t(t+1)/2 where p=floor(n/3), q=floor(n/5), t=floor(n/15)
# and n = 999.

# Here just to be "cool" we make it a one-liner
(floor := __import__('math',fromlist=["floor"]).floor);print(int(3*floor(999/3)*(floor(999/3)+1)/2+5*floor(999/5)*(floor(999/5)+1)/2-15*floor(999/15)*(floor(999/15)+1)/2))