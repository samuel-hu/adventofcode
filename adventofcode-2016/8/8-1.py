import copy


SCREEN_WIDTH = 50
SCREEN_HEIGHT = 6

def print_screen(screen):
    for row in screen:
        for column in row:
            print column,
        print ''

def rect(screen, width, height):
    new_screen = copy.deepcopy(screen)
    for i in range(min(width, SCREEN_WIDTH)):
        for j in range(min(height, SCREEN_HEIGHT)):
            new_screen[j][i] = '#'
    return new_screen

def rotate_row(screen, row, distance):
    new_row = copy.deepcopy(screen[row])
    distance = distance % SCREEN_WIDTH
    for i in range(SCREEN_WIDTH):
        offset = i + distance
        if offset >= SCREEN_WIDTH:
            offset -= SCREEN_WIDTH
        new_row[offset] = screen[row][i]

    new_screen = copy.deepcopy(screen)
    new_screen[row] = new_row
    return new_screen

def rotate_column(screen, column, distance):
    new_screen = copy.deepcopy(screen)
    distance = distance % SCREEN_HEIGHT
    for i in range(SCREEN_HEIGHT):
        offset = i + distance
        if offset >= SCREEN_HEIGHT:
            offset -= SCREEN_HEIGHT
        new_screen[offset][column] = screen[i][column]
    return new_screen

def count_on(screen):
    count = 0
    for row in screen:
        for column in row:
            if column == '#':
                count += 1
    return count
    
screen = [ ['.' for i in range(SCREEN_WIDTH)] for height in range(SCREEN_HEIGHT) ]
print_screen(screen)

with open('input.txt', 'r') as instructions:
    for instruction in instructions:
        instruction = instruction.split()
        operation = instruction[0]
        if operation == 'rect':
            width, height = instruction[1].split('x')
            screen = rect(screen, int(width), int(height))
        if operation == 'rotate':
            direction = instruction[1]
            if direction == 'row':
                screen = rotate_row(screen, int(instruction[2].split('=')[1]), int(instruction[4]))
            elif direction == 'column':
                screen = rotate_column(screen, int(instruction[2].split('=')[1]), int(instruction[4]))

        print instruction
        print_screen(screen)
        
print count_on(screen)
