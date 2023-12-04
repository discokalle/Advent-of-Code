input_file = open('input.txt', 'r')
lines = input_file.readlines()
card_amounts = [1]*len(lines) #At least 1 card of each
for line_i, line in enumerate(lines):
    card_num, numbers = line.split(":") #card_num is not used
    winning_numbers, my_numbers = [parts.split() for parts in numbers.split("|")] # split numbers into set of winning_ and my_
    hits = [number for number in winning_numbers if number in my_numbers] #all numbers they have in common
    for i in range(1, len(hits) + 1): #duplicate the next cards
        card_amounts[line_i + i] += card_amounts[line_i] if line_i + i < len(card_amounts) else card_amounts
print(sum(card_amounts))