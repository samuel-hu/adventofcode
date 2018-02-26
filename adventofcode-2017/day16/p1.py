def parse_instructions(filename):
    with open(filename, 'r') as fp:
        instructions = fp.read().strip().split(',')
        return instructions


def spin(offset, sequence):
    return sequence[len(sequence) - offset:] + sequence[:len(sequence) - offset]


def swap(a, b, sequence):
    if a > b:
        a, b = b, a
    return sequence[:a] + sequence[b] + sequence[a+1:b] + sequence[a] + sequence[b+1:]


def process_instruction(instruction, sequence):
    if instruction[0] == 's':
        return spin(int(instruction[1:]), sequence)
    elif instruction[0] == 'x':
        a, b = instruction[1:].split('/')
        return swap(int(a), int(b), sequence)
    elif instruction[0] == 'p':
        a, b = instruction[1:].split('/')
        return swap(sequence.find(a), sequence.find(b), sequence)


sequence = 'abcdefghijklmnop'
instructions = parse_instructions('input.txt')

#sequence = 'abcde'
#instructions = ['s1', 'x3/4', 'pe/b']

for instruction in instructions:
    sequence = process_instruction(instruction, sequence)

print sequence
