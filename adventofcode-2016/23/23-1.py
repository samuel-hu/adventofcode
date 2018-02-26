from collections import defaultdict

def val(value, registers):
    try:
        return int(value)
    except ValueError:
        return registers[value]

def toggle(instructions, index):
    if index >= len(instructions): 
        return instructions

    ins = instructions[index]
    if len(ins) == 2:
        ins[0] = 'dec' if ins[0] == 'inc' else 'inc'
    elif len(ins) == 3:
        ins[0] = 'cpy' if ins[0] == 'jnz' else 'jnz'

    instructions[index] = ins
    return instructions


possible_registers = ('a', 'b', 'c', 'd')
instructions = [] 
index = 0
registers = defaultdict(int)
registers['a'] = 7

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
        if i[2] in possible_registers:
            registers[i[2]] = val(i[1], registers)
    elif i_type == 'inc':
        registers[i[1]] += 1
    elif i_type == 'dec':
        registers[i[1]] -= 1
    elif i_type == 'tgl':
        instructions = toggle(instructions, val(i[1], registers) + index)

    index += 1

print registers
