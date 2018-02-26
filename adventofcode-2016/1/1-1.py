orientation = 0
coordinate = (0, 0)

update = [
    lambda coordinate, distance: (coordinate[0], coordinate[1] + distance),
    lambda coordinate, distance: (coordinate[0] + distance, coordinate[1]),
    lambda coordinate, distance: (coordinate[0], coordinate[1] - distance),
    lambda coordinate, distance: (coordinate[0] - distance, coordinate[1])
]

with open('input.txt', 'r') as input_file:
    for instruction in input_file.readline().split(','):
        instruction = instruction.strip()
        rotation = instruction[0]
        distance = int(instruction[1:])
        
        if rotation == 'R':
            orientation += 1
            if orientation > 3:
                orientation -= 4
        elif rotation == 'L':
            orientation -= 1
            if orientation < 0:
                orientation += 4

        coordinate = update[orientation](coordinate, distance)

print coordinate
print abs(coordinate[0]) + abs(coordinate[1])
