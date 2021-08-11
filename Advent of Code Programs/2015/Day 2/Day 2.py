import numpy as np
file_name = "input.txt"

# Due to efficiency we will use a list consisting of lists / rows instead of
# numpy arrays! For more read this SO article:
# https://stackoverflow.com/questions/568962/how-do-i-create-an-empty-array-matrix-in-numpy

matrix = []

with open(file_name) as f_obj:
    dimensions_list = f_obj.readlines()


for line in dimensions_list:
    flag = False
    temp_dimension = ''
    temp_row = []
    for char in line:
        if flag:
            temp_dimension = ''
        if char.isdigit():
            flag = False
            temp_dimension += str(char)
        elif char == 'x':
            flag = True
            temp_row.append(int(temp_dimension))
        else:
            temp_row.append(int(temp_dimension)) # This is the eol condition
            # That is when the 'character iteration' meets the end of the
            # line variable!
    matrix.append(temp_row)
    
total_area = 0.0        
for row in matrix:
    products = [row[0]*row[1], row[1]*row[2], row[0]*row[2]]
    total_area += 2*np.sum(products)+min(products)

print(f"The elves will need {total_area} square meters of wrapping paper")
