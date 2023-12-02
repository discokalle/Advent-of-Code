'''
DAY1:
- Take first and last number of each line as a two digit number.
- If only one number, repeat for second digit
- Add all numbers
- Some of the numbers were spelled out with letters
'''

input_file = open('input.txt', 'r')
Lines = input_file.readlines()

def fuckingshit(str):
    
   return(str
          .replace("one", "o1e")
          .replace("two", "t2o")
          .replace("three", "t3e")
          .replace("four", "f4r")
          .replace("five", "f5e")
          .replace("six", "s6x")
          .replace("seven", "s7n")
          .replace("eight", "e8t")
          .replace("nine", "n9e"))
   
sum = 0
for line in Lines:
    line = fuckingshit(line)
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
        
