def swap_positions(string, index_x, index_y):
    if index_x > index_y:
        return swap_positions(string, index_y, index_x)
    return string[:index_x] + string[index_y] + string[index_x+1:index_y] + string[index_x] + string[index_y+1:]


def swap_letters(string, letter_x, letter_y):
    return swap_positions(string, string.find(letter_x), string.find(letter_y))


def rotate_right(string, distance):
    return string[len(string) - distance:] + string[:len(string) - distance]


def rotate_left(string, distance):
    return string[distance:] + string[:distance]


def rotate_by_letter(string, letter):
    position = string.find(letter)
    distance = 1 + position
    if position >= 4:
        distance += 1
    return rotate_right(string, distance)


def reverse_between_indices(string, index_x, index_y):
    return string[:index_x] + string[index_x:index_y+1][::-1] + string[index_y + 1:]


def reverse_between_letters(string, letter_x, letter_y):
    index_x = string.find(letter_x)
    index_y = string.find(letter_y)
    return reverse_between_indices(string, index_x, index_y)


def move(string, from_index, to_index):
    letter = string[from_index]
    without_x = string[:from_index] + string[from_index + 1:]
    return without_x[:to_index] + letter + without_x[to_index:]


def find_permutations(password):
    permutations = set()
    if len(password) < 1:
        return ['']
    for i in range(len(password)):
        for rest in find_permutations(password[:i] + password[i+1:]):
            permutations.add(password[i] + rest)
    return permutations 


scrambled = 'fbgdceah'
instructions = []
permutations = find_permutations('abcdefgh')

with open('input.txt', 'r') as fp:
    for row in fp:
        instruction = row.strip().split()
        instructions.append(instruction)

for permutation in permutations:
    password = permutation
    for instruction in instructions:
        operation = instruction[0]

        if operation == 'rotate':
            direction = instruction[1]
            distance = instruction[2]
            if direction == 'right':
                password = rotate_right(password, int(distance))
            elif direction == 'left':
                password = rotate_left(password, int(distance))
            else:
                password = rotate_by_letter(password, instruction[6])
        elif operation == 'swap':
            operation_type = instruction[1]
            x = instruction[2]
            y = instruction[5]
            if operation_type == 'letter':
                password = swap_letters(password, x, y)
            else:
                password = swap_positions(password, int(x), int(y))
        elif operation == 'reverse':
            x = int(instruction[2])
            y = int(instruction[4])
            password = reverse_between_indices(password, x, y)
        elif operation == 'move':
            from_index = int(instruction[2])
            to_index = int(instruction[5])
            password = move(password, from_index, to_index) 
        
        if len(password) != 8:
            print instruction
            print password
            raise RuntimeError

    if password == scrambled:
        print permutation
        break

