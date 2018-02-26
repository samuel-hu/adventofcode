def get_moves(filename):
    with open(filename, 'r') as fp:
        return fp.read().strip().split(',')


def move(location, direction):
    x, y, z = location
    if direction == 'n':
        return (x, y + 1, z - 1)
    elif direction == 'ne':
        return (x + 1, y, z - 1)
    elif direction == 'nw':
        return (x + 1, y - 1, z)
    elif direction == 's':
        return (x, y - 1, z + 1)
    elif direction == 'se':
        return (x - 1, y + 1, z)
    elif direction == 'sw':
        return (x - 1, y, z + 1)
    else:
        raise ValueError('Unknown direction "{}"'.format(direction))


def distance(a, b):
    ax, ay, az = a
    bx, by, bz = b
    return max(abs(ax - bx), abs(ay - by), abs(az - bz))


location = (0, 0, 0)
max_distance = 0
moves = get_moves('input.txt')
for m in moves:
    location = move(location, m)
    curr_distance = distance((0, 0, 0), location)
    if curr_distance > max_distance:
        max_distance = curr_distance

print max_distance
