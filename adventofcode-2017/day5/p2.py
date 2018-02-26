with open('input.txt') as fp:
    jumps = [int(jump.strip()) for jump in fp if not jump.isspace()]

curr_position = 0
steps = 0

while curr_position < len(jumps):
    next_position = curr_position + jumps[curr_position]
    curr_offset = jumps[curr_position]
    jumps[curr_position] = curr_offset + 1 if curr_offset < 3 else curr_offset - 1
    curr_position = next_position
    steps += 1

print steps
