with open ('input.txt', 'r') as file:
    lines = file.readlines()

def count_occurrences(s):
    occurrences = {char: 0 for char in set(s)}  #Dict with values 0 for chars (ignores repeats)
    for c in s:
        occurrences[c] = occurrences.get(c, 0) + 1 
    return occurrences

def get_hand_type(s):
    occurrences = count_occurrences(s)
    most_occurring = max(occurrences, key = lambda x: occurrences[x] if x != 'J' else 0) #find most occurring character that isn't J
    s = s.replace('J', most_occurring)
    occurrences = count_occurrences(s)
    occurrences = (sorted(occurrences.values(), reverse=True)) #list sorted from most to least occurring. Example: 32T3K will yield [2, 1, 1, 1]
    
    match occurrences[0]:               #Check first card (and sometimes second) to determine the type of hand.
        case 5:                         #Five of a kind
            return 6
        case 4:                         #Four of a kind
            return 5
        case 3 if occurrences[1] == 2:  #Full house
            return 4
        case 3:                         #Three of a kind
            return 3 
        case 2 if occurrences[1] == 2:  #Two pairs
            return 2 
        case 2:                         #Pair
            return 1 
        case _:                         #Else: High card
            return 0 

def my_sort(hand):
    strength = "J123456789TQKA"
    return(get_hand_type(hand), #Sort by hand type first. If they are the same, sort by hand[0]...
           strength.index(hand[0]),
           strength.index(hand[1]),
           strength.index(hand[2]),
           strength.index(hand[3]),
           strength.index(hand[4]))

ranked = [(line.split()[0], line.split()[1]) for line in lines] #tuple from hand and bid
ranked.sort(key = lambda x: my_sort(x[0])) #sort based on my_sort
tot = sum(int(bid) * (i+1) for i, (_, bid) in enumerate(ranked))
print(tot)


    