with open('input.txt', 'r') as f:
    line = f.readline()
    floor = 0
    index = 0
    for paren in line:
        if paren == '(':
            floor += 1
        elif paren == ')':
            floor -= 1
        index += 1
        if floor < 0:
            print index
            break
