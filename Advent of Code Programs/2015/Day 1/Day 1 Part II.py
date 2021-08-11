file_name = "input.txt"

with open(file_name) as f_obj:
    instructions = f_obj.read()
    
current_steps = 0
elevation = 0
for char in instructions:
    current_steps += 1
    if char == '(':
        elevation += 1
    elif char == ')':
        elevation -= 1
    else: # this is to be honest not needed because we already know the
          # contents of the input.txt file
        print("There's an invalid character here. This loop will now break")
    if elevation == -1 : break 

print(f'Santa reached the basement at step number {current_steps}')



