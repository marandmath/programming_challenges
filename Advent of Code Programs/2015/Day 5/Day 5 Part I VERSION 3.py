def double_letter(word):
    """A function that checks the letters of a word to find any doubles
    and if any forbidden sequences are in that word"""
    flag = 0
    forbidden_flag = False
    if ('ab' in word) or ('cd' in word) or ('pq' in word) or ('xy' in word):
        forbidden_flag = True
    else:
        pass
    for i in range(len(word)-1):
        check_double = word[i] == word[i+1]
        if check_double and not forbidden_flag:
            flag = 1
        else:
            continue
    return flag

def vowels_checker(word):
    """A function that checks if a word contains at LEAST 3 vowels"""
    vowels_counter = 0
    for letter in word:
        if letter in "aeiou":
            vowels_counter +=1 
            if vowels_counter >= 3:
                return True
    return False
    
file_name = "input.txt"

with open(file_name) as f_obj:
    contents = f_obj.readlines()

nice_words_counter = 0
for word in contents:
    if double_letter(word) and vowels_checker(word):
        nice_words_counter += 1

print(f"There are {nice_words_counter} nice words in total!")


    


