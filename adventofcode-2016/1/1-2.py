orientation = 0
coordinate = (0, 0)
visited = [coordinate]

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

        for i in range(distance):
            coordinate = update[orientation](coordinate, 1)

            if coordinate in visited:
                print coordinate
            visited.append(coordinate)
