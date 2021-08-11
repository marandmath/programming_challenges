# For this exercise we used this article on the hashlib library:
# https://www.geeksforgeeks.org/md5-hash-python/
# and using the wikipedia page on the md5 hash function
import hashlib
from itertools import count

puzzle_input = "yzbqklnj"

for number in count(start=0, step=1):
    temp_str2hash = puzzle_input+str(number)
    temp_result = hashlib.md5(temp_str2hash.encode())
    first_6_digits = ""
    for i in range(6):
        first_6_digits += str(temp_result.hexdigest()[i])
    if first_6_digits == "000000":
        break

print(f"""The least integer that gives a digest that has 6 leading zeroes in 
      hexadecimal is {number}""")
