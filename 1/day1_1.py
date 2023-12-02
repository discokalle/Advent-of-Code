'''
DAY1:
- Take first and last number of each line as a two digit number.
- If only one number, repeat for second digit
- Add all numbers
'''

input_file = open('input.txt', 'r')
Lines = input_file.readlines()

sum = 0
for line in Lines:
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
    sum += num

print(sum)
        