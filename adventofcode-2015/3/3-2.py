with open('input.txt', 'r') as f:
    santa_x = 0
    santa_y = 0
    robo_x = 0
    robo_y = 0
    index = 0
    visited = set()

    for direction in f.readline():
        if index % 2:
            location = (santa_x, santa_y)
            visited.add(location)

            if direction == '^':
                santa_y += 1
            elif direction == '>':
                santa_x += 1
            elif direction == 'v':
                santa_y -= 1
            elif direction == '<':
                santa_x -= 1
        else:
            location = (robo_x, robo_y)
            visited.add(location)

            if direction == '^':
                robo_y += 1
            elif direction == '>':
                robo_x += 1
            elif direction == 'v':
                robo_y -= 1
            elif direction == '<':
                robo_x -= 1
        index += 1
    print len(visited)
