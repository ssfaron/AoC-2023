#####################################################
### Author: Sarah Faron
### Advent of Code Day 6
### Date: 12/05/2023
######################################################

import numpy as np

### Part 1 ###
input = "day6.txt"

# Read in the input file
with open(input) as f:
    lines = f.readlines()

times = [35, 69, 68, 87]
distance = [213, 1168, 1086, 1248]

total_options = []

for i in range(0, len(times)):
    options = {}
    total = 0
    for j in range(1, times[i]):
    
        options[j] = j*(times[i]-j)
    
    for key in options:
        if options[key] > distance[i]:
            total = total + 1
    total_options.append(total)
        
        
print(np.prod(total_options))

### Part 2 ###

times = [35696887]
distance = [213116810861248]

total_options = []

for j in range(10000000, 100000000):
    if j*(times[0]-j) < distance[0]:
        print(j)
        break
    
minimum = 7579553
maximum = 28117334

print(maximum-minimum+1)
    