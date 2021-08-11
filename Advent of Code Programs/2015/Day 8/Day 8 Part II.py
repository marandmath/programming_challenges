# MUCH MORE ELEGANT SOLUTION USING THE EVAL() FUNCTION

total_number_of_characters = 0
total_number_of_characters_encoded = 0
for s in open("input.txt"): # We dont really need to convert this iterable
                            # to a list
    total_number_of_characters += len(s.strip()) # to get rid of the nl escseq
    total_number_of_characters_encoded += len(s.strip()) + 2 + s.count('\"') + s.count('\\')
    # We add: 1. The length of the string without the newline escseq '\n'
    # 2. 2 for the leading and trailing double quotes for each  which we will 
    # need two 'extra' backslashes to encode them
    # 3. How many '"' we have
    # 4. How many '\' we have

number_needed = total_number_of_characters_encoded - total_number_of_characters
print(f"Result: {number_needed}")
