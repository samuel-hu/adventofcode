def get_initial_banks(filename):
    with open(filename, 'r') as fp:
        return [int(blocks) for blocks in fp.readline().strip().split()]
    
def find_largest_bank(banks):
    return max(enumerate(banks), key=lambda x: x[1])

def reallocate(old_banks):
    banks = list(old_banks)
    size = len(banks)
    index, blocks = find_largest_bank(banks)
    banks[index] = 0
    for i in range(blocks):
        index += 1
        if index >= size:
            index -= size
        banks[index] = banks[index] + 1
    return banks
    
            
banks = get_initial_banks('input.txt')
#banks = [0, 2, 7, 0]

steps = 0
previous_states = set()

while tuple(banks) not in previous_states:
    previous_states.add(tuple(banks))
    banks = reallocate(banks)
    steps += 1

print steps
