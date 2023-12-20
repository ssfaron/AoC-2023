#####################################################
### Author: Sarah Faron
### Advent of Code Day 2
### Date: 12/02/2023
######################################################

### Part 1 ###
input = "day4.txt"

my_nums_dict = {}
winning_nums_dict = {}
matches_dict = {}

counter = 0
total_points = 0

# Read in the input file
with open(input) as f:
    lines = f.readlines()
    
    for line in lines:
        counter = counter + 1
        matches = []
        card = line.split(":")[1]
        winning = card.split(" | ")[0].lstrip()
        winning = winning.split(' ')
        mine = card.split(" | ")[1].split("\n")[0].split(' ')
        
        winning_nums = []
        for i in range(0, len(winning)):
            if winning[i] != '':
                winning_nums.append(int(winning[i]))
                
        my_nums = []
        for i in range(0, len(mine)):
            if mine[i] != '':
                my_nums.append(int(mine[i]))
        
        for i in range(0, len(my_nums)):
            if my_nums[i] in winning_nums:
                matches.append(my_nums[i])                
        
        my_nums_dict[counter] = my_nums
        winning_nums_dict[counter] = winning_nums
        matches_dict[counter] = len(matches)
        
        if len(matches) == 0:
            total_points = total_points + 0
        elif len(matches) == 1:
            total_points = total_points + 1
        elif len(matches) == 2:
            total_points = total_points + 2
        elif len(matches) == 3:
            total_points = total_points + 4
        elif len(matches) == 4: 
            total_points = total_points + 8
        elif len(matches) == 5:
            total_points = total_points + 16
        elif len(matches) == 6:
            total_points = total_points + 32
        elif len(matches) == 7:
            total_points = total_points + 64
        elif len(matches) == 8:
            total_points = total_points + 128
        elif len(matches) == 9:
            total_points = total_points + 256
        elif len(matches) == 10:
            total_points = total_points + 512

print(total_points)

### Part 2 ###
copies = {}

for i in range(1,212):
    copies[i] = 1

for i in range(1,212):
    match_num = matches_dict[i]
    
    # process copies  
    for k in range(0, copies[i]):
        for j in range(i+1, i+match_num+1):
            copies[j] = copies[j]+1       

total_cards = 0
for key in copies:
    total_cards = total_cards + copies[key]
print(total_cards)