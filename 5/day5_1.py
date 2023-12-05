with open('input.txt', 'r') as file:
    content = file.read()
sections = [section for section in content.split('\n\n')] #Split each section on empty line
seeds = sections.pop(0).split()[1:] #pop first line into seeds, split by space and ignore "seeds:"

def get_location_number(seed): #start from seed and get next number for each level
    num = int(seed)
    for section in sections: #Seed, soil, fertilizer, etc.
        lines = section.split('\n')
        for line in lines[1:]: #Look for num on each line, ignore first line
            dst, src, rng = map(int, line.split()) #extract numbers on line as ints
            if src < num < src + rng:
                num = dst + (num - src) #If we find num then next numb is dst + offset and break. Else just keep number
                break
    return num
lowest = min(map(get_location_number, seeds)) #Get lowest location of all seeds
print(lowest)