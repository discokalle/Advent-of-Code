from collections import defaultdict
import math
with open('input.txt', 'r') as file:
    instructions, _ = file.read().split('\n\n')
    nodes = _.split('\n')
    
children_of = defaultdict(str)

for line in nodes:
    parent, children = line.split(" = ")
    children_of[parent] = tuple(child.strip() for child in children.strip('()').split(','))

ends_with_A = [parent for parent in children_of if parent[2] == 'A'] #MSA, AAA, PKA, NBA, RHA, CDA :)
def get_steps(current): #get steps to ..Z from current
    steps = 0
    while current[2] != 'Z':
        direction = instructions[steps % len(instructions)]
        current = children_of[current][0] if direction == 'L' else children_of[current][1]
        steps += 1
    return(steps)
steps_to_z = [get_steps(start) for start in ends_with_A] #steps to get to ..Z from each node ..A
print(math.lcm(*steps_to_z)) #they synch up at lowest common multiple


