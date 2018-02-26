def move(coord, direction):
    return coord[0] + direction[0], coord[1] + direction[1]

def can_move(coord, direction, memory):
    if move(coord, direction) in memory:
        return False
    return True
    
target = 265149
directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
memory = set((0, 0))

curr_location = 1
curr_coordinate = (0, 0)
curr_direction = 0 
next_direction = curr_direction + 1 % 4

while curr_location != target:
    if can_move(curr_coordinate, directions[next_direction], memory):
        curr_coordinate = move(curr_coordinate, directions[next_direction])
        curr_direction = (curr_direction + 1) % len(directions)
        next_direction = (curr_direction + 1) % len(directions)
    else:
        curr_coordinate = move(curr_coordinate, directions[curr_direction])
    memory.add(curr_coordinate)
    curr_location += 1

distance = abs(curr_coordinate[0]) + abs(curr_coordinate[1])
print curr_location, curr_coordinate, distance

