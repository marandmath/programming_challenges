from itertools import permutations

with open("input.txt") as f_obj:
    contents = f_obj.readlines()

# Storing the new countries in an iterable; a list
# Due to the way the data is stored (that is, they are sorted) we proceed as;

countries = [contents[0].split()[0]]

for line in contents:
    if countries[0] == line.split()[0]:
        countries.append(line.split()[2])
    else:
        break

# For all the possible distances we will create a dictionary of dictionaries
# Each dictionary in this large dictionary will correspond to an 'origin' 
# country and its distances from all the other possible 'destinations'
destinations = {}
for line in contents:
    # With tuple (un)packing we get the data that we need and ignore the other
    # For conveniece we often define 'throwaway' values under a single
    # underscore variable
    (origin, _, destination, _, distance) = line.split()
    # Doing the double assignment for decreasing runtime due to the way the
    # setdefault method works when the specified keys ALREADY are in the dict
    destinations.setdefault(origin, dict())[destination] = int(distance)
    destinations.setdefault(destination, dict())[origin] = int(distance)

possible_journeys = list(permutations(destinations.keys()))
corresponding_total_distance = []
for journey in possible_journeys:
    temp_distance = 0
    for i in range(7):
        temp_distance += destinations[journey[i]][journey[i+1]]
    corresponding_total_distance.append(temp_distance)

minindex, mindist = corresponding_total_distance.index(min(corresponding_total_distance)), min(corresponding_total_distance)
maxindex, maxdist = corresponding_total_distance.index(max(corresponding_total_distance)), max(corresponding_total_distance)

print(f"Shortest trip: {possible_journeys[minindex]} with distance {mindist}")
print(f"Longest trip: {possible_journeys[maxindex]} with distance {maxdist}")
        
