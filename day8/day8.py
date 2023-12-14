# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 08:35:30 2023

@author: sfaron
"""
import sys

input = "input.txt"

### Part 1 ###

values = {}
position = 'AAA'
steps = 0

# def execute_order(order, position, steps):
#     for i in range(0, len(order)):
#         if order[i] == 'L':
#             position = values[position][0]
#             steps = steps + 1
            
#             if position == 'TNZ':
#                 print(steps)
#                 sys.exit()
#         elif order[i] == 'R':
            
#             position = values[position][1]
#             steps = steps + 1
            
#             if position == 'TNZ':
#                 print(steps)
#                 sys.exit() 
    
#     execute_order(order, position, steps)

# def execute_all_orders(order, a_dict, steps):
    
#     for i in range(0, len(order)):
#         if order[i] == 'L':
            
#             if steps == 0:
#                 for a in range(0, len(all_A)):                
#                     position = values[all_A[a]][0] 
#                     a_dict[all_A[a]] = position
#                 steps = steps + 1
#             else:
#                 for key in a_dict.keys():
#                     position = values[a_dict[key]][0]
#                     a_dict[key] = position
#                 steps = steps + 1
            
#             Zs = []
#             for a in all_A: 
#                 position = a_dict[a]
#                 Zs.append(position)
            
#             Z_count = 0
#             for i in range(0, len(all_Z)):
#                 if all_Z[i] in Zs:
#                     Z_count = Z_count + 1
#             if Z_count == len(all_Z):
#                 print(steps)
#                 sys.exit()
                
#         elif order[i] == 'R':
            
#             if steps == 0:
#                 for a in range(0, len(all_A)): 
#                     position = values[all_A[a]][1]
#                     a_dict[all_A[a]] = position
#                 steps = steps + 1
#             else:
#                 for key in a_dict.keys():
#                     position = values[a_dict[key]][1]
#                     a_dict[key] = position
#                 steps = steps + 1
            
#             Zs = []
#             for a in all_A: 
#                 position = a_dict[a]
#                 Zs.append(position)
            
#             Z_count = 0
#             for i in range(0, len(all_Z)):
#                 if all_Z[i] in Zs:
#                     Z_count = Z_count + 1
#             if Z_count == len(all_Z):
#                 print(steps)
#                 sys.exit()
    
#     execute_all_orders(order, a_dict, steps)

# Read in the input file
with open(input) as f:
    lines = f.readlines()
    
    order = lines[0].split('\n')[0]
    
    for i in range(2, len(lines)):
        value = lines[i].split(' ')[0]
        left = lines[i].split(' ')[2].split('(')[1].split(',')[0]
        right = lines[i].split(' ')[3].split(')')[0]
        
        values[value] = left, right

i = 0
while i < len(order):
    if order[i] == 'L':
        position = values[position][0]
        steps = steps + 1
        
        if position == 'ZZZ':
            print(steps)
            sys.exit()
    elif order[i] == 'R':
        
        position = values[position][1]
        steps = steps + 1
        
        if position == 'ZZZ':
            print(steps)
            sys.exit() 
    
    if i == len(order)-1:
        i = 0
    else:
        i = i+1
    
    
#execute_order(order, position, steps) # RIP my beautiful functions
    
### Part 2 (Ideally) ###
    
all_A = []
all_Z = []
for value in values:
    if value[2] == 'A':
        all_A.append(value)
    elif value[2] == 'Z':
        all_Z.append(value)


a_dict = {}
z_dict = {}

for a in all_A:
    a_dict[a] = []
    
#execute_all_orders(order, a_dict, 0) # RIP my beautiful functions

i = 0
while i < len(order):
    if order[i] == 'L':
        
        if steps == 0:
            for a in range(0, len(all_A)):                
                position = values[all_A[a]][0] 
                a_dict[all_A[a]] = position
            steps = steps + 1
        else:
            for key in a_dict.keys():
                position = values[a_dict[key]][0]
                a_dict[key] = position
            steps = steps + 1
        
        Zs = []
        for a in all_A: 
            position = a_dict[a]
            Zs.append(position)
        
        Z_count = 0
        for i in range(0, len(all_Z)):
            if all_Z[i] in Zs:
                Z_count = Z_count + 1
        if Z_count == len(all_Z):
            print(steps)
            sys.exit()
            
    elif order[i] == 'R':
        
        if steps == 0:
            for a in range(0, len(all_A)): 
                position = values[all_A[a]][1]
                a_dict[all_A[a]] = position
            steps = steps + 1
        else:
            for key in a_dict.keys():
                position = values[a_dict[key]][1]
                a_dict[key] = position
            steps = steps + 1
        
        Zs = []
        for a in all_A: 
            position = a_dict[a]
            Zs.append(position)
        
        Z_count = 0
        for i in range(0, len(all_Z)):
            if all_Z[i] in Zs:
                Z_count = Z_count + 1
        if Z_count == len(all_Z):
            print(steps)
            sys.exit()
    
    if i == len(order)-1:
        i = 0
    else:
        i = i+1

### What I actually did for Part 2: 
    # AAA -> ZZZ in 22199
    # DVA -> XDZ in 13207
    # VXA -> TNZ in 16579
    # JHA -> FRZ in 18827
    # NMA -> JFZ in 17141
    # PXA -> LHZ in 14893
    # LCM = 13,334,102,464,297
    