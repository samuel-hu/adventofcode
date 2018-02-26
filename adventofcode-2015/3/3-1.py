with open('input.txt', 'r') as f:
    x = 0
    y = 0
    visited = set()
    for direction in f.readline():
        location = (x, y)
        visited.add(location)
        if direction == '^':
            y += 1
        elif direction == '>':
            x += 1
        elif direction == 'v':
            y -= 1
        elif direction == '<':
            x -= 1
    print len(visited)
