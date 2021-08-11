# VERY IMPORTANT IN THESE EXERCISES (PART I AND PART II) are regular
# expressions and back references! Knowing how to properly use them makes this
# particular puzzle fairly straightforward.

def letter_reppetition_checker(word):
    """Checks the letter repetition rule of the instructions"""
    flag_1 = False
    flag_2 = False
    for i in range(len(word)-2):
        if word[i] == word[i+2]:
            flag_1 = True
            break
    # For better understanding this part a session of debugging works wonders!
    # (προκαταρκτικη εκτελεση / debugging / preliminary execution)
    for i in range(len(word)-3): # So we dont make a useless "round" of
                                 # checking we go up the second from 
                                 # last letter
        # Using slicing instead word[i]+word[i+1]
        temp = word[i:i+2]
        rest_of_the_word = word[i+2:]
        if temp in rest_of_the_word:
            flag_2 = True
            break
    return flag_1 and flag_2
            

file_name = "input.txt"

with open(file_name) as f_obj:
    contents = f_obj.readlines()

nice_words_counter = 0
for word in contents:
    if letter_reppetition_checker(word):
        nice_words_counter += 1 
    
print(f"There are {nice_words_counter} nice words in total!")
