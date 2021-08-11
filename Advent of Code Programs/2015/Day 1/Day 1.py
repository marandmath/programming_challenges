file_name = "input.txt"

with open(file_name) as f_obj:
    content = f_obj.read()
    
step_up = 0
step_down = 0
for char in content:
    if char == '(':
        step_up += 1
    elif char == ')':
        step_down += 1
    else: # this is to be honest not needed because we already know the
          # contents of the input.txt file
        print("There's an invalid character here. This loop will now break")
        break

if step_down == step_up:
    print("With these directions, Santa will remain at the ground level")
else:
    direction = 'up' if step_up-step_down > 0 else 'down'
    print(f"Santa will go {abs(step_up-step_down)} floor(s) {direction}")


