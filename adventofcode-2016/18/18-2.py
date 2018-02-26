def count_safe_tiles(row):
    return len([tile for tile in row if tile == '.'])

def get_tile(row, index):
    if index < 0 or index >= len(row):
        return '.'
    return row[index]

def get_next_row(row):
    next_row = ''
    for i in range(len(row)):
        if (get_tile(row, i - 1) == get_tile(row, i) == '^' and get_tile(row, i + 1) == '.') \
            or (get_tile(row, i + 1) == get_tile(row, i) == '^' and get_tile(row, i - 1) == '.') \
            or (get_tile(row, i - 1) == get_tile(row, i) == '.' and get_tile(row, i + 1) == '^') \
            or (get_tile(row, i + 1) == get_tile(row, i) == '.' and get_tile(row, i - 1) == '^'):
            next_row += '^'
        else:
            next_row += '.'
    return next_row


total_rows = 400000
current_row_index = 0
current_row = ''
num_safe_tiles = 0

with open('input.txt', 'r') as fp:
    current_row = fp.readline().strip()
    num_safe_tiles += count_safe_tiles(current_row)
    current_row_index += 1

while current_row_index < total_rows:
#    print current_row
    current_row = get_next_row(current_row)
    num_safe_tiles += count_safe_tiles(current_row)
    current_row_index += 1

print num_safe_tiles
