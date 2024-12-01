import re

input_file = open('ex.txt', 'r')
lines = input_file.readlines()

for line_i, line in enumerate(lines):
    for match in re.finditer(r'\d+', line): #find all numbers and their index on a given line
        number = match.group()
        number_length = len(str(number))
        number_start_index = match.start()
        
        neighbours = (
            (line[number_start_index - 1] if number_start_index > 0 else '') + # Left
            (lines[line_i - 1][number_start_index - 1] if number_start_index > 0 and line_i > 0 else '') + # Upper Left
            (lines[line_i - 1][number_start_index:number_start_index + number_length] if line_i > 0 else '') + # Above
            (lines[line_i - 1][number_start_index + number_length] if number_start_index + number_length < len(line) and line_i > 0 else '') + # Upper Right
            (line[number_start_index + number_length] if number_start_index + number_length < len(line) else '') + # Right
            (lines[line_i + 1][number_start_index +  number_length] if number_start_index + number_length < len(line) and line_i + 1 < len(lines) else '') + # Lower Right
            (lines[line_i + 1][number_start_index:number_start_index + number_length] if line_i + 1 < len(lines) else '') + # Below
            (lines[line_i + 1][number_start_index - 1] if number_start_index + number_length < len(line) and line_i + 1 < len(lines) else '') # Lower Left
        )

