# This is a very ugly "solution" (there is something wrong in the check_seq
# function which leads to a false output, mostlikely has to do with the
# indeces) which doesnt utilise regex or the eval() function. See the other
# MUCH better solutions!

escape_sequences = [r'\"',r'\\',r'\x']

def check_seq(word,count):
    """A function that searches the input for any of the wanted
    escape sequences"""
    new_word = word
    for i, char in enumerate(word):
        if char == "\\" and i < len(word)-1:
            if word[i+1] == '"' or word[i+1] ==  '\\':
                # Because strings dont support the del statement we use this:
                new_word = new_word[:i] + new_word[i+2:] 
                count += 1
                check_seq(new_word, count)
            elif word[i+1] == 'x':
                new_word = new_word[:i] + new_word[i+4:]
                count += 1
                check_seq(new_word, count)
            else:
                pass
    return new_word, count
                            
with open("input.txt") as f_obj:
    contents = f_obj.readlines()

total_number_of_characters = 0
for line in contents:
    total_number_of_characters += len(line.strip())

total_number_of_characters_inmem = 0

for line in contents:
    flag = False
    for seq in escape_sequences:
        if seq in line:
            flag = True
            break
    if flag:
        new_word, count_in_memchar = check_seq(line,0)
        total_number_of_characters_inmem += count_in_memchar + len(new_word)
    else:
        total_number_of_characters_inmem += len(line.strip())-2
        
needed_amount = total_number_of_characters - total_number_of_characters_inmem

print(f"Result: {needed_amount}")

    