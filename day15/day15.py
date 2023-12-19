#lines = 'HASH'

input = "day15.txt"
all_vals = []
current_value = 0
boxes = {}

def hash(string, current_value):
    ## HASH algorithm ###
    #current_value = 0
    for i in range(0, len(string)):
        if string[i] != '\n':
            char = string[i]
            asc  = ord(char)
            current_value = current_value + asc
            current_value = current_value*17
            current_value = current_value%256
        
    #all_vals.append(current_value)
    return current_value

# Read in the input file
with open(input) as f:
    lines = f.readlines()

for line in lines:
    line = line.split(',')
    
    ### Part 1 ###
    # for i in range(0, len(line)):
    #     if line[i] != '\n':
#             hash(line[i], current_value)

# print(sum(all_vals))
    
    ### Part 2 ###   
    for i in range(0, len(line)):
        if line[i] != '\n':
            if '=' in line[i]:
                label = line[i].split('=')[0]
                focal_len = line[i].split('=')[1]
                       
                if label != '\n': 
                    box = hash(label, 0)
                    
                    if box not in boxes.keys():
                        boxes[box] = {}
                        boxes[box][1] = (label, focal_len)
                    else:
                        for slot_key in boxes[box]:
                            if label in boxes[box][slot_key]:
                                boxes[box][slot_key] = (label, focal_len)
                                break
                        else:
                            slot = len(boxes[box])+1
                            boxes[box][slot] = (label, focal_len)
                            
            if '-' in line[i]:
                label = line[i].split('-')[0]
                
                for box_key in boxes:
                    for slot_key in boxes[box_key]:
                        if label in boxes[box_key][slot_key]:
                            del boxes[box_key][slot_key]

                            for old_slot_key in range(slot_key+1, len(boxes[box_key])+2):
                                boxes[box_key][old_slot_key-1] = boxes[box_key][old_slot_key]
                                del boxes[box_key][old_slot_key]
                            break
                            
                        
                    

focusing_power = []
for box_key in boxes:
    box_number = box_key + 1

    for slot_key in boxes[box_key]:
        focal_length = int(boxes[box_key][slot_key][1])
        
        focusing_power.append(box_number*slot_key*focal_length)
print(sum(focusing_power))

# 166455 too low                