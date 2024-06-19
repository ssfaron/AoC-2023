#####################################################
### Author: Sarah Faron
### Advent of Code Day 5
### Date: 12/04/2023
######################################################

### Part 1 ###
input = "C:\\Users\\Sarah Smallwood\\Desktop\\day5.txt"

seeds = {}
seed_to_soil_map = []
soil_to_fert_map = []
fert_to_water_map = []
water_to_light_map = []
light_to_temp_map = []
temp_to_hum_map = []
hum_to_loc_map = []

#Read in the input file
with open(input) as f:
    lines = f.readlines()

my_seeds = lines[0].split(': ')[1]
my_seeds = my_seeds.split('\n')[0]
my_seeds = my_seeds.split(' ')

for i in range(0, len(my_seeds)):
    my_seeds[i] = int(my_seeds[i])
    
# Part 2
all_seeds = []
for i in range(0, len(my_seeds), 2):
    all_seeds.append(my_seeds[i])
    all_seeds.append(my_seeds[i]+my_seeds[i+1])

for i in range(3, 35):
    stsm = lines[i].split('\n')[0]
    stsm = lines[i].split(' ')
    for j in range(0, len(stsm)):
        stsm[j] = int(stsm[j])
    seed_to_soil_map.append(stsm)
    
for i in range(37, 66):
    stfm = lines[i].split('\n')[0]
    stfm = lines[i].split(' ')
    for j in range(0, len(stfm)):
        stfm[j] = int(stfm[j])
    soil_to_fert_map.append(stfm)

for i in range(68, 103):
    ftwm = lines[i].split('\n')[0]
    ftwm = lines[i].split(' ')
    for j in range(0, len(ftwm)):
        ftwm[j] = int(ftwm[j])
    fert_to_water_map.append(ftwm)

for i in range(105, 130):
    wtlm = lines[i].split('\n')[0]
    wtlm = lines[i].split(' ')
    for j in range(0, len(wtlm)):
        wtlm[j] = int(wtlm[j])
    water_to_light_map.append(wtlm)

for i in range(132, 146):
    lttm = lines[i].split('\n')[0]
    lttm = lines[i].split(' ')
    for j in range(0, len(lttm)):
        lttm[j] = int(lttm[j])
    light_to_temp_map.append(lttm)

for i in range(148, 180):
    tthm = lines[i].split('\n')[0]
    tthm = lines[i].split(' ')
    for j in range(0, len(tthm)):
        tthm[j] = int(tthm[j])
    temp_to_hum_map.append(tthm)

for i in range(182, 197):
    htlm = lines[i].split('\n')[0]
    htlm = lines[i].split(' ')
    for j in range(0, len(htlm)):
        htlm[j] = int(htlm[j])
    hum_to_loc_map.append(htlm)

# seed to soil mapping
seed_ranges = []
for i in range(0, len(seed_to_soil_map)):
    seed_ranges.append((seed_to_soil_map[i][1], seed_to_soil_map[i][1]+seed_to_soil_map[i][2]-1))

for seed in all_seeds:
    for i in range(0, len(seed_ranges)):
        if seed >= seed_ranges[i][0] and seed <= seed_ranges[i][1]:
            diff = seed - seed_ranges[i][0]
            soil = seed_to_soil_map[i][0] + diff
            seeds[seed] = [soil]

for seed in all_seeds:
    if seed not in seeds.keys():
        seeds[seed] = [seed]

# soil to fertilizer mapping
soil_ranges = []
for i in range(0, len(soil_to_fert_map)):
    soil_ranges.append((soil_to_fert_map[i][1], soil_to_fert_map[i][1]+soil_to_fert_map[i][2]-1))

for seed in seeds.keys():
    soil = seeds[seed][0]
    for i in range(0, len(soil_ranges)):
        if soil >= soil_ranges[i][0] and soil <= soil_ranges[i][1]:
            diff = soil - soil_ranges[i][0]
            fert = soil_to_fert_map[i][0] + diff
            seeds[seed].append(fert)
    
for seed in seeds.keys():
    if len(seeds[seed]) == 1:
        seeds[seed].append(seeds[seed][0])

# fertilizer to water mapping
fert_ranges = []
for i in range(0, len(fert_to_water_map)):
    fert_ranges.append((fert_to_water_map[i][1], fert_to_water_map[i][1]+fert_to_water_map[i][2]-1))

for seed in seeds.keys():
    fert = seeds[seed][1]
    for i in range(0, len(fert_ranges)):
        if fert >= fert_ranges[i][0] and fert <= fert_ranges[i][1]:
            diff = fert - fert_ranges[i][0]
            water = fert_to_water_map[i][0] + diff
            seeds[seed].append(water)
    
for seed in seeds.keys():
    if len(seeds[seed]) == 2:
        seeds[seed].append(seeds[seed][1])

# water to light mapping
water_ranges = []
for i in range(0, len(water_to_light_map)):
    water_ranges.append((water_to_light_map[i][1], water_to_light_map[i][1]+water_to_light_map[i][2]-1))

for seed in seeds.keys():
    water = seeds[seed][2]
    for i in range(0, len(water_ranges)):
        if water >= water_ranges[i][0] and water <= water_ranges[i][1]:
            diff = water - water_ranges[i][0]
            light = water_to_light_map[i][0] + diff
            seeds[seed].append(light)
    
for seed in seeds.keys():
    if len(seeds[seed]) == 3:
        seeds[seed].append(seeds[seed][2])

# light to temperature mapping
light_ranges = []
for i in range(0, len(light_to_temp_map)):
    light_ranges.append((light_to_temp_map[i][1], light_to_temp_map[i][1]+light_to_temp_map[i][2]-1))

for seed in seeds.keys():
    light = seeds[seed][3]
    for i in range(0, len(light_ranges)):
        if light >= light_ranges[i][0] and light <= light_ranges[i][1]:
            diff = light - light_ranges[i][0]
            temp = light_to_temp_map[i][0] + diff
            seeds[seed].append(temp)
    
for seed in seeds.keys():
    if len(seeds[seed]) == 4:
        seeds[seed].append(seeds[seed][3])

# temperature to humidity mapping
temp_ranges = []
for i in range(0, len(temp_to_hum_map)):
    temp_ranges.append((temp_to_hum_map[i][1], temp_to_hum_map[i][1]+temp_to_hum_map[i][2]-1))

for seed in seeds.keys():
    temp = seeds[seed][4]
    for i in range(0, len(temp_ranges)):
        if temp >= temp_ranges[i][0] and temp <= temp_ranges[i][1]:
            diff = temp - temp_ranges[i][0]
            hum = temp_to_hum_map[i][0] + diff
            seeds[seed].append(hum)
    
for seed in seeds.keys():
    if len(seeds[seed]) == 5:
        seeds[seed].append(seeds[seed][4])

# humidity to location mapping
hum_ranges = []
for i in range(0, len(hum_to_loc_map)):
    hum_ranges.append((hum_to_loc_map[i][1], hum_to_loc_map[i][1]+hum_to_loc_map[i][2]-1))

for seed in seeds.keys():
    hum = seeds[seed][4]
    for i in range(0, len(hum_ranges)):
        if hum >= hum_ranges[i][0] and hum <= hum_ranges[i][1]:
            diff = hum - hum_ranges[i][0]
            loc = hum_to_loc_map[i][0] + diff
            seeds[seed].append(loc)
    
for seed in seeds.keys():
    if len(seeds[seed]) == 6:
        seeds[seed].append(seeds[seed][5])
        
# find min location
min_val = 1000000000000
min_val_key = 1000000000000

for seed in seeds.keys():
    if seeds[seed][6] < min_val:
        min_val = seeds[seed][6]
        min_val_key = seed
        
print(min_val)