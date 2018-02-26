from itertools import product


def move(coord, direction):
    return coord[0] + direction[0], coord[1] + direction[1]

def can_move(coord, direction, memory):
    if move(coord, direction) in memory:
        return False
    return True

def get_value(coord, memory):
    value = 0
    for offset in product((1, 0, -1), repeat=2):
        try:
            value += memory[(coord[0] + offset[0], coord[1] + offset[1])]
        except KeyError:
            pass
    return value 
    
    
target = 265149
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
memory = {(0, 0): 1}

curr_value = 0
curr_coordinate = (0, 0)
curr_direction = 0 
next_direction = curr_direction + 1 % 4

while curr_value <= target:
    if can_move(curr_coordinate, directions[next_direction], memory):
        curr_coordinate = move(curr_coordinate, directions[next_direction])
        curr_direction = (curr_direction + 1) % len(directions)
        next_direction = (curr_direction + 1) % len(directions)
    else:
        curr_coordinate = move(curr_coordinate, directions[curr_direction])
    curr_value = get_value(curr_coordinate, memory)
    memory[curr_coordinate] = curr_value

print curr_value

