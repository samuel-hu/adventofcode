from collections import defaultdict

def val(value, registers):
    try:
        return int(value)
    except ValueError:
        return registers[value]


instructions = [] 
index = 0
registers = defaultdict(int)

with open('input.txt', 'r') as raw_instructions:
    instructions = [instruction.strip().split() for instruction in raw_instructions]


count = 0
while index < len(instructions):
    count += 1

    i = instructions[index]
    i_type = i[0]

    if i_type == 'jnz':
        if val(i[1], registers) != 0:
            index += val(i[2], registers)
            continue
    elif i_type == 'cpy':
        registers[i[2]] = val(i[1], registers)
    elif i_type == 'inc':
        registers[i[1]] += 1
    elif i_type == 'dec':
        registers[i[1]] -= 1
    index += 1

print registers
