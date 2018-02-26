coordinate = (1, 1)
operations = {
    'U': lambda coordinate: (coordinate[0], coordinate[1] - 1),
    'D': lambda coordinate: (coordinate[0], coordinate[1] + 1),
    'L': lambda coordinate: (coordinate[0] - 1, coordinate[1]),
    'R': lambda coordinate: (coordinate[0] + 1, coordinate[1])
}
code = ''

def clamp(coordinate):
    return (min(max(coordinate[0], 0), 2), min(max(coordinate[1], 0), 2))

def to_num(coordinate):
    return coordinate[0] + 3 * coordinate[1] + 1

with open('input.txt', 'r') as instructions:
    for line in instructions:
        for instruction in line.strip():
            # print instruction
            coordinate = operations[instruction](coordinate)
            coordinate = clamp(coordinate)
        code += str(to_num(coordinate)) 

print code

