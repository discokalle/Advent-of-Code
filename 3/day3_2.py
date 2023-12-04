import re

input_file = open('input.txt', 'r')
lines = input_file.readlines()
lines = [line.rstrip('\n') + '.' for line in lines] # Added period to eahc line; Something goes wrong for numbers that extend to the right but I don't know why

star_numbers = {} #Will contain stars and their neighbouring numbers
for line_i, line in enumerate(lines):
    for match in re.finditer(r'\d+', line): # find all numbers and their index on a given line
        number = match.group()
        number_length = len(str(number))
        number_start_index = match.start()
        
        neighbouring_stars = [ #index of neighbouring star
            (line_i + row, number_start_index + col)
            for row in range(-1, 2) #up, center, down of number
            for col in range(-1, number_length + 1) #left, center, right of number
            if (
                0 <= line_i + row < len(lines) and 0 <= number_start_index + col < len(line) #within bounds
                and lines[line_i + row][number_start_index + col] == '*' #is star
            )
        ]
        
        for star in neighbouring_stars: #Add numbers to stars
            if star not in star_numbers:
                star_numbers[star] = [number]
            else:
                star_numbers[star].append(number)

star_numbers = {star: numbers for star, numbers in star_numbers.items() if len(star_numbers[star]) == 2} #only keep stars with 2 numbers
sum = 0
for star, numbers in star_numbers.items(): #calculation
    gear_ratio = int(numbers[0]) * int(numbers[1])
    sum += gear_ratio
print (sum)
        

