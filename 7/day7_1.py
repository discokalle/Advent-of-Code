with open ('ex.txt', 'r') as file:
    lines = file.readlines()

def find_occurance(s, c1):
    char_at = [i for i, c2 in enumerate(s) if c1 == c2]
    return len(char_at)

for line in lines:
    hand, bid = line.split()
    checked_chars = ""
    for char in hand:
        if char not in checked_chars:
            print(f"hand: {hand}, char: {char}, occurance: {find_occurance(hand, char)}")
            checked_chars += char