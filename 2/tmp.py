import re

input = "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"

def find_biggest(s, color):
    matches = re.findall(rf'(\d+)\s{color}', s)
    biggest = str(max(map(int, matches), default=None))
    return biggest

id = (re.search(r'Game\s(\d+)', input)).group(1)
result = find_biggest(input, "red")
print ("result: " + result)
print ("id = " + id)
