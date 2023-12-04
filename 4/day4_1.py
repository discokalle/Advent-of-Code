input_file = open('input.txt', 'r')
lines = input_file.readlines()
sum = 0
for line in lines:
    card_num, numbers = line.split(":") #card_num is not used
    winning_numbers, my_numbers = [parts.split() for parts in numbers.split("|")] # split numbers into set of winning_ and my_
    hits = [number for number in winning_numbers if number in my_numbers] #all numbers they have in common
    points = 2 ** (len(hits)-1) if len(hits) > 0 else 0 #calculate
    sum += points
print(sum)