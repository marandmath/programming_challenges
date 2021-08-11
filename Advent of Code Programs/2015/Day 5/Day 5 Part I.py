# Ways to split the characters of a string strand to a list:
# https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/

def word_splitter(word):
    """A function that splits a word to its letters and appends them in order
    to a list"""
    return [char for char in word]

def double_letter(letters):
    """A function that checks the letters of a word to find any doubles
    and if any forbidden sequences are in that word"""
    forbidden_sequences = ['ab', 'cd', 'pq', 'xy']
    flag = 0
    for i in range(len(letters)-1):
        check_double = letters[i] == letters[i+1]
        check_forbidden = letters[i]+letters[i+1] in forbidden_sequences
        if check_double and not check_forbidden:
            flag = 1
        else:
            continue
    return flag

def vowels_checker(letters):
    """A function that checks if a word contains at LEAST 3 vowels"""
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    vowels_counter = 0
    for letter in letters:
        if letter in vowels_list:
            vowels_counter +=1 
    if vowels_counter >= 3:
        return True
    else:
        return False
    
file_name = "input.txt"

with open(file_name) as f_obj:
    contents = f_obj.readlines()


nice_words_counter = 0
for line in contents:
    if double_letter(word_splitter(line)) and vowels_checker(word_splitter(line)):
        nice_words_counter += 1

print(f"There are {nice_words_counter} nice words in total!")


    


