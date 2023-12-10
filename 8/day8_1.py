from collections import defaultdict
with open('input.txt', 'r') as file:
    instructions, _ = file.read().split('\n\n')
    nodes = _.split('\n')
    
children_of = defaultdict(str)

for line in nodes:
    parent, children = line.split(" = ")
    children_of[parent] = tuple(child.strip() for child in children.strip('()').split(','))

current, steps = "AAA", 0
while current != "ZZZ":
    direction = instructions[steps % len(instructions)]
    current = children_of[current][0] if direction == 'L' else children_of[current][1]
    steps += 1
print(steps)
