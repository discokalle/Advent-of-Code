import re
'''
DAY2:
- Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
- What is the sum of the IDs of those games?
'''

input_file = open('input.txt', 'r')
Lines = input_file.readlines()

def find_biggest(s, color):
    matches = re.findall(rf'(\d+)\s{color}', s)
    biggest = str(max(map(int, matches), default=None))
    return biggest

sum = 0
for line in Lines:
    id = (re.search(r'Game\s(\d+)', line)).group(1)
    if int (find_biggest(line, "red")) <= 12:
        if int (find_biggest(line, "green")) <= 13:
            if int (find_biggest(line, "blue")) <= 14:
                sum += int(id)
print (sum)