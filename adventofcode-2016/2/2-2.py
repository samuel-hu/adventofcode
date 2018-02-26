#     1
#   2 3 4
# 5 6 7 8 9
#   A B C
#     D

coordinate = (0, 2)
operations = {
    'U': lambda coordinate: (coordinate[0], coordinate[1] - 1),
    'D': lambda coordinate: (coordinate[0], coordinate[1] + 1),
    'L': lambda coordinate: (coordinate[0] - 1, coordinate[1]),
    'R': lambda coordinate: (coordinate[0] + 1, coordinate[1])
}
code = ''

def is_in_bounds(coordinate):
    if (coordinate[0] < 0 or 
        coordinate[0] > 4 or
        coordinate[1] < 0 or
        coordinate[1] > 4):
        return False

    return to_num(coordinate) != ' ' 

def to_num(coordinate):
    matrix = [
        [' ',' ','1',' ',' '],
        [' ','2','3','4',' '],
        ['5','6','7','8','9'],
        [' ','A','B','C',' '],
        [' ',' ','D',' ',' '],
    ]
    return matrix[coordinate[1]][coordinate[0]]

with open('input.txt', 'r') as instructions:
    for line in instructions:
        for instruction in line.strip():
            new_coordinate = operations[instruction](coordinate)
            if is_in_bounds(new_coordinate):
                coordinate = new_coordinate
        code += str(to_num(coordinate)) 

print code

