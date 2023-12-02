'''
DAY1_Part2:
- First attempt. Ignore
- Works for test1 and test2 but not input... :(

'''

input_file = open('input.txt', 'r')
Lines = input_file.readlines()

def replace_first(input_str):
    spelled_numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    current_word = ""
    
    for char in input_str:
        if char == '\n':
            continue
        if (current_word + char).isnumeric():
            return input_str
        if any(numb.startswith(current_word + char) for numb in spelled_numbers):
            current_word += char
        else:
            if current_word in spelled_numbers:
                digit = spelled_numbers[current_word]
                input_str = input_str.replace(current_word[0], digit, 1)
                current_word = char
                if char.isalpha():
                    current_word = ""
                break
            elif char.isalpha():
                current_word = char
    return input_str

def replace_last(input_str):
    input_str = "".join(reversed(input_str))
    spelled_numbers = {"eno": "1", "owt": "2", "eerht": "3", "ruof": "4", "evif": "5", "xis": "6", "neves": "7", "thgie": "8", "enin": "9"}
    current_word = ""
    
    for char in input_str:
        if char == '\n':
            continue
        if (current_word + char).isnumeric():
            return "".join(reversed(input_str))
        if any(numb.startswith(current_word + char) for numb in spelled_numbers):
            current_word += char
        else:
            if current_word in spelled_numbers:
                digit = spelled_numbers[current_word]
                input_str = input_str.replace(current_word[0], digit, 1)
                current_word = char
                if char.isalpha():
                    current_word = ""
                break
            elif char.isalpha():
                current_word = char

    return "".join(reversed(input_str))

for line in Lines:
    print(line)
    line = replace_first(line)
    print(line)
    line = replace_last(line) 
    print(line)
'''
sum = 0
for line in Lines:
    print(line)
    line = replace_first(line)
    line = replace_last(line) 
    print(line)
    first_digit = 0
    second_digit = 0
    
    for char in line: #first number
        if char.isdigit():
            first_digit = int(char)
            break
        
    for char in reversed(line): #second number
        if char.isdigit():
            second_digit = int(char)
            break
        
    num = first_digit * 10 + second_digit
    
    print(num)
    sum += num

print(sum)
'''
        
