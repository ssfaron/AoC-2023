#hands = ['32T3K', 'T55J5', 'KK677', 'KTJJT', 'QQQJA']
#bids = [765, 684, 28, 220, 483]
hands = []
bids = []
input = "input.txt"

# Read in the input file
with open(input) as f:
    lines = f.readlines()
    
for line in lines:
    hands.append(line.split(' ')[0])
    bids.append(line.split(' ')[1])

results = {1:[],
           2:[],
           3:[],
           4:[],
           5:[],
           6:[],
           7:[]}

for hand in hands:
    
    first = hand[0]
    
    # check for 5 of a kind
    if len(set(hand)) == 1:
        results[7].append(hand)
    
    # check for 4 of a kind -- len(set(hand)) == 2
    if len(set(hand)) == 2:
        
        counts = []
        for i in range(0, len(hand)):
            counts.append(hand.count(hand[i]))
        
        if 1 in counts:
            results[6].append(hand)
        else:
            results[5].append(hand)
    
    # check for 3 of a kind -- len(set(hand)) == 3
    if len(set(hand)) == 3:
        
        counts = []
        for i in range(0, len(hand)):
            counts.append(hand.count(hand[i]))
        
        # check for two pair
        if 2 in counts:
            results[3].append(hand)
        else:              
            results[4].append(hand)
    
    # check for a pair
    if len(set(hand)) == 4:
        results[2].append(hand)
    
    # check for high card
    if len(set(hand)) == 5:
        results[1].append(hand)

order = ['A', 'K', 'Q', 'J', 'T']
        

rank = []
for key in results:
    if results[key] != []:
        if len(results[key]) == 1:
            rank.append(results[key])
        else:
            for i in range(0, len(results[key])):
                rank.append(results[key][i])
                
grand_total = 0

for i in range(0, len(rank)):
    #hand_total = 0
    for j in range(0, len(lines)):
        if str(rank[i]) in lines[j]:
            hand_bid = int(lines[j].split(' ')[1].split('\n')[0])
            hand_total = hand_bid*(i+1)
    grand_total = grand_total + hand_total
            
        
# 252193083 too low
# 252830445 too low
# 254534939 too high