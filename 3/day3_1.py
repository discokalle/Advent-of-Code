import re

input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.rstrip('\n') + '.' for line in lines] # Added period to eahc line; Something goes wrong for numbers that extend to the right but I don't know why
sum = 0
for line_i, line in enumerate(lines):
    for match in re.finditer(r'\d+', line): # find all numbers and their index on a given line
        number = match.group()
        number_length = len(str(number))
        number_start_index = match.start()
        
        neighbours = ''.join(#string of all neighbours; cleaner version of neihbours found in tmp file
            lines[line_i + row][number_start_index + col]
            for row in range(-1, 2) #up, center, down of number
            for col in range(-1, number_length + 1) #left, center, right of number
            if 0 <= line_i + row < len(lines) and 0 <= number_start_index + col < len(line) #within bounds
            )
    
        if any(c not in '.0123456789' for c in neighbours):
            sum += int (number)
print (sum)
        

