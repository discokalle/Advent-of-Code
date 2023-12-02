import re
'''
DAY2:
- What is the fewest number of cubes of each color that could have been in the bag to make the game possible?
- The power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
- For each game, find the minimum set of cubes that must have been present. What is the sum of the power of these sets?
'''

input_file = open('input.txt', 'r')
Lines = input_file.readlines()

def find_biggest(s, color):
    matches = re.findall(rf'(\d+)\s{color}', s)
    biggest = str(max(map(int, matches), default=None))
    return biggest

sum = 0
for line in Lines:
    min_red = int (find_biggest(line, "red"))
    min_green = int (find_biggest(line, "green"))
    min_blue = int (find_biggest(line, "blue"))
    min_power = min_red * min_green * min_blue
    sum += min_power
print (sum)