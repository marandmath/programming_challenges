file_name = "input.txt"

with open(file_name, 'r') as f_obj:
    directions = f_obj.read()

# We will work in the Cartesian Coordinates of the R^2 plane by having santa
# start at the origin; that is (0,0) (we use lists and not tuples for obvious
# reasons, that will become apparent through the course of this program)

# The first two coordinates correspond to the xy-position of the real santa
# The second two coordinates correspond to the xy-position of robo-santa
current_position_of_santa = [0,0]
current_position_of_robo_santa = [0,0]

houses_delivered = ([tuple(current_position_of_santa),
                     tuple(current_position_of_robo_santa)])

switch_to_robo_santa = False
for direction in directions:
        if not switch_to_robo_santa:
            if direction == "^":
                current_position_of_santa[1] += 1
            elif direction == "v":
                current_position_of_santa[1] -= 1
            elif direction == ">":
                current_position_of_santa[0] += 1
            else:
                current_position_of_santa[0] -= 1 
                # due to the contets of the file input.txt
                # we know that we dont have invalid characters
            houses_delivered.append(tuple(current_position_of_santa))
            switch_to_robo_santa = True
        else:
            if direction == "^":
                current_position_of_robo_santa[1] += 1
            elif direction == "v":
                current_position_of_robo_santa[1] -= 1
            elif direction == ">":
                current_position_of_robo_santa[0] += 1
            else:
                current_position_of_robo_santa[0] -= 1 
            houses_delivered.append(tuple(current_position_of_robo_santa))
            switch_to_robo_santa = False
        
# Here for this next part of the code we had to turn our lists of coordinates
# to an unhashable data type like a tuple which is ummutable. For more refer 
# to the notes under the "Hash() function" section or refer to this SO article
#https://stackoverflow.com/questions/19371358/python-typeerror-unhashable-type-list

no_houses = len(set(houses_delivered))

print(f"Santa and Robo-Santa will visit exactly {no_houses} unique houses")
