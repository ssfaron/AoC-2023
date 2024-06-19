#####################################################
### Author: Sarah Faron
### Advent of Code Day 2
### Date: 12/02/2023
######################################################
import re
import collections

### Part 1 ###
input = "day3.txt"
line_num = 0
duplicates = False

digits = {}
symbols = {}
part_index = {}
all_vals_dict = {}
all_vals_indices_dict = {}

ints = ["0","1","2","3","4","5","6","7","8","9"]

# Read in the input file
with open(input) as f:
    lines = f.readlines()
    counter = 0
    for line in lines:
        counter = counter+1
        line_num = line_num + 1
        num_indices = []
        sym_indices = []
        line = line.split("\n")[0]
        
        # get all numbers in this line in a list
        all_vals = []
        current_num = ''
        same_num = False
        for i in range(0, len(line)):
            if line[i] in ints:
                current_num = current_num+line[i]
                same_num = True
            else:
                same_num = False
                if current_num != '':
                    all_vals.append(current_num)
                    current_num = ''
        
        if len(all_vals) != len(set(all_vals)):
            print("DUPLICATE: "+str(counter))
            duplicates = True
            duplicate = [item for item, count in collections.Counter(all_vals).items() if count > 1]
        else: 
            duplicates = False
        all_vals_dict[line_num] = all_vals
        
        all_vals_indices = {}
        for val in all_vals:
            match_indices = []
            match = (re.search(val,line))
            match_tuple = match.span()
            for i in range(0, match_tuple[1] - match_tuple[0]):
                match_indices.append(match_tuple[0]+i) #giving first instance only -- doesn't work for dupes
            
            if duplicates == True and val == duplicate[0]:
                if val in all_vals_indices.keys():
                    all_vals_indices_dict[line_num][val].append(match_indices)
                else:
                    all_vals_indices[val] = match_indices
                    all_vals_indices_dict[line_num] = all_vals_indices
            else:
                all_vals_indices[val] = match_indices
                all_vals_indices_dict[line_num] = all_vals_indices
            
        for i in range(0, len(line)):
            if line[i].isdigit():
                num_indices.append(i)
            else:
                if line[i] != ".":
                    sym_indices.append(i)
        
        digits[line_num] = num_indices
        symbols[line_num] = sym_indices
        
for i in range(1, len(all_vals_dict)+1):
    parts = []
    for index in digits[i]:
        check = int(index)
        
        a = [check-1, check, check+1]
        
        if i > 1 and i < len(all_vals_dict):
            if any(x in a for x in symbols[i]) or any(x in a for x in symbols[i-1]) or any(x in a for x in symbols[i+1]):
                parts.append(check)
        elif i == 1:
            if any(x in a for x in symbols[i]) or any(x in a for x in symbols[i+1]):
                parts.append(check)
        elif i == len(all_vals_dict):
            if any(x in a for x in symbols[i]) or any(x in a for x in symbols[i-1]):
                parts.append(check)
    
    part_index[i] = parts

part_numbers = []
for i in range(1, len(part_index)+1):
    this_line = []
    for j in range(0, len(part_index[i])):
        for val in all_vals_indices_dict[i]: 
            #duplicates = [item for item, count in collections.Counter(val).items() if count > 1])
            if part_index[i][j] in all_vals_indices_dict[i][val]:
                if int(val) not in this_line:
                    part_numbers.append(int(val))
                    this_line.append(int(val))
    
print(sum(part_numbers))

#269083 too low
# 298764 too low
#329272 too low
#531520 no

#536347 no