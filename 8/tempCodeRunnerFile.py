for line in nodes:
    parent, children = line.split(" = ")
    children_of[parent] = tuple(child.strip() for child in children.strip('()').split(','))