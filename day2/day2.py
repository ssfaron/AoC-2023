#####################################################
### Author: Sarah Faron
### Advent of Code Day 2
### Date: 12/01/2023
######################################################

### Part 1 ###
input = "input_day2.txt"
games = {}
ids = []
id_sum = 0

# Read in the input file
with open(input) as f:
    lines = f.readlines()
    
    for line in lines:
        blue = []
        red = []
        green = []
        
        game = int(line.split(":")[0].split(" ")[1])
        results = line.split(":")[1].split(" ")
        results.pop(0)
        
        for i in range(0, len(results)):
            if i%2 != 0:
                if results[i][0] == "r":
                    #red = red + int(results[i-1])
                    red.append(int(results[i-1]))
                if results[i][0] == "b":
                    #blue = blue + int(results[i-1])
                    blue.append(int(results[i-1]))
                if results[i][0] == "g":
                    #green = green + int(results[i-1])
                    green.append(int(results[i-1]))
            
        games[game] = [red, blue, green]

for game in games:
    if all(x <= 12 for x in games[game][0]) and all(x <= 14 for x in games[game][1]) and all(x <= 13 for x in games[game][2]):
        ids.append(game)

for i in range(0, len(ids)):
    id_sum = id_sum + ids[i]

print(id_sum)

### Part 2 ###
power_sums = 0

for game in games:
    red_needed = max(games[game][0])
    blue_needed = max(games[game][1])
    green_needed = max(games[game][2])
    
    powers = red_needed*blue_needed*green_needed
    
    power_sums = power_sums + powers

print(power_sums)