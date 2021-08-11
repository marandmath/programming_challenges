# MUCH MORE ELEGANT SOLUTION USING THE EVAL() FUNCTION

total_number_of_characters = 0
total_number_of_characters_inmem = 0
for s in open("input.txt"): # We dont really need to convert this iterable
                            # to a list
    total_number_of_characters += len(s.strip()) # to get rid of the nl escseq
    total_number_of_characters_inmem += len(eval(s))
    # The reason we can use the eval function explicitly and immediately is due
    # to the fact than the syntax of the input for each string is in the form:
    # "[string with eg. hexadecimal ascii code]"

number_needed = total_number_of_characters - total_number_of_characters_inmem
print(f"Result: {number_needed}")
