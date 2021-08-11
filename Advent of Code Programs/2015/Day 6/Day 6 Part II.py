# Due to the nature of the exercise we will use the numpy library for
# 2D-Matrices

import numpy as np

file_name = 'input.txt'

with open(file_name) as f_obj:
    instructions = f_obj.readlines()
    
grid = np.zeros((1000,1000))

for line in instructions:
    instruction = line.split()
    if (instruction[1] == 'on') or (instruction[1] == 'off'):
        start_coordinates = instruction[2].split(',')
        end_coordinates = instruction[-1].split(',')
        # Because we used the split method we turned integers to strings!
        x_coordinate_start = int(start_coordinates[0])
        y_coordinate_start = int(start_coordinates[1])
        x_coordinate_end = int(end_coordinates[0])
        y_coordinate_end = int(end_coordinates[1])
        if instruction[1] == 'on':
            for i in range(x_coordinate_start,x_coordinate_end+1):
                for j in range(y_coordinate_start,y_coordinate_end+1):
                    grid[i,j] += 1
    
        else:
            for i in range(x_coordinate_start,x_coordinate_end+1):
                for j in range(y_coordinate_start,y_coordinate_end+1):
                    grid[i,j] = grid[i,j]-1 if grid[i,j]>=1 else 0
    else:
        start_coordinates = instruction[1].split(',')
        end_coordinates = instruction[-1].split(',')
        # Because we used the split method we turned integers to strings!
        x_coordinate_start = int(start_coordinates[0])
        y_coordinate_start = int(start_coordinates[1])
        x_coordinate_end = int(end_coordinates[0])
        y_coordinate_end = int(end_coordinates[1])
        for i in range(x_coordinate_start,x_coordinate_end+1):
                for j in range(y_coordinate_start,y_coordinate_end+1):
                    grid[i,j] += 2
                    
total_brightness = np.sum(grid)

print(f"Total brightness level: {total_brightness}")
            
