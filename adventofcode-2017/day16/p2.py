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


def dance(instructions, sequence):
    for instruction in instructions:
        sequence = process_instruction(instruction, sequence)
    return sequence

sequence = 'abcdefghijklmnop'
instructions = parse_instructions('input.txt')
seen_sequences = []
iteration = 0

while iteration <= 10 ** 9:
    if sequence in seen_sequences:
        print seen_sequences[(10 ** 9) % iteration]
        break
    else:
        seen_sequences.append(sequence)
        sequence = dance(instructions, sequence)
        iteration += 1

