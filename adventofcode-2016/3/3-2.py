num_valid = 0

def get_triangles_from_columns(columns):
    return [
        [columns[0][0], columns[1][0], columns[2][0]],
        [columns[0][1], columns[1][1], columns[2][1]],
        [columns[0][2], columns[1][2], columns[2][2]],
    ]

with open('input.txt', 'r') as input_file:
    input_line = input_file.readline()
    while input_line:
        triangles = []
        sides = [int(side) for side in input_line.strip().split()]
        triangles.append(sides)
        input_line = input_file.readline()
        sides = [int(side) for side in input_line.strip().split()]
        triangles.append(sides)
        input_line = input_file.readline()
        sides = [int(side) for side in input_line.strip().split()]
        triangles.append(sides)
        for sides in get_triangles_from_columns(triangles):
            sides.sort()
            if sides[0] + sides[1] > sides[2]:
                num_valid += 1

        input_line = input_file.readline()
print num_valid
