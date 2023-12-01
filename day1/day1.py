######################################################
### Author: Sarah Faron
### Advent of Code Day 1
### Date: 11/30/2023
######################################################

### Part 1 ###
input = "input.txt"
full_sum = 0

# Read in the input file
with open(input) as f:
    lines = f.readlines()
    
    for line in lines:
        vals = []
        for i in range(0, len(line)):
            try: 
                if isinstance(int(line[i]), int):
                    vals.append(int(line[i]))
                else:
                    continue
            except:
                continue
        line_sum = str(vals[0])+str(vals[-1])
        line_sum = int(line_sum)
        full_sum = full_sum+line_sum

print("The total sum with just numerals is "+str(full_sum)+".")

### Part 2 ###
full_sum = 0
num_strings = ["one", 
               "two", 
               "three",
               "four",
               "five", 
               "six",
               "seven",
               "eight",
               "nine"]
ints = ["1","2","3","4","5","6","7","8","9"]

# Read in the input file
with open(input) as f:
    lines = f.readlines()

    for line in lines:
        vals = []
        indices = {}
        for i in range(0, len(num_strings)):
            for j in range(0, len(line)):
                if line.startswith(num_strings[i], j):
                    indices[j] = i+1
                elif line.startswith(ints[i], j):
                    indices[j] = i+1
        vals.append(indices[min(indices)])
        vals.append(indices[max(indices)])
        line_sum = str(vals[0])+str(vals[-1])
        line_sum = int(line_sum)
        full_sum = full_sum+line_sum
    
print("The total sum with numerals and number words is "+str(full_sum)+".")
