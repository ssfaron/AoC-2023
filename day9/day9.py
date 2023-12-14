# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 09:47:23 2023

@author: sfaron
"""



history = []

def take_diff_fwd(line, index):
    for i in range(0, len(line)-1):
        if index in diffs.keys():
            diffs[index].append(line[i+1] - line[i])
        else: 
            diffs[index] = []
            diffs[index].append(line[i+1] - line[i])

    if diffs != {}:
        current_line = diffs[index]
        if all(x == 0 for x in current_line):
            current_diff = 0
            for j in range(1, len(diffs)):
                if j == 1:
                    current_diff = diffs[j][-1] + diffs[j+1][-1]
                else:
                    current_diff = current_diff + diffs[j+1][-1]
            history.append(curl[-1] + current_diff)
        else:
            previous_index = index
            index = index + 1
            take_diff_fwd(diffs[previous_index], index)
            
    else:
        previous_index = index
        index = index + 1
        take_diff_fwd(diffs[previous_index], index)

def take_diff_bck(line, index):
    if diffs == {}:
        for i in range(len(line)-1, 0, -1):
            if index in diffs.keys():
                diffs[index].append(line[i] - line[i-1])
            else: 
                diffs[index] = []
                diffs[index].append(line[i] - line[i-1])
    else:
        for i in range(0, len(line)-1):
            if index in diffs.keys():
                diffs[index].append(line[i] - line[i+1])
            else: 
                diffs[index] = []
                diffs[index].append(line[i] - line[i+1])

    if diffs != {}:
        current_line = diffs[index]
        if all(x == 0 for x in current_line):
            current_diff = 0
            for j in range(len(diffs), 1, -1):
                if j == len(diffs):
                    current_diff = diffs[j-1][0] - diffs[j][0]
                #elif j == 2:
                    #current_diff = diffs[j-1][-1] - diffs[j][0]
                else:
                    current_diff = diffs[j-1][-1] - current_diff
            history.append(curl[0] - current_diff)
        else:
            previous_index = index
            index = index + 1
            take_diff_bck(diffs[previous_index], index)
            
    else:
        previous_index = index
        index = index + 1
        take_diff_bck(diffs[previous_index], index)
        
input = "input.txt"
#input = "sample.txt"

# Read in the input file
with open(input) as f:
    lines = f.readlines()
    
    for line in lines:
        
        curl = []
        index = 1
        diffs = {}
        
        line = line.split('\n')[0].split(' ')
        for i in range(0, len(line)):
            curl.append(int(line[i]))

        ### Part 1 ###
        #take_diff_fwd(curl, index)
        
        ### Part 2 ###
        take_diff_bck(curl, index)

print(sum(history))