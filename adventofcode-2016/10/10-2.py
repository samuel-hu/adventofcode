import collections


init_instructions = []
transfer_instructions = {} 
bots = collections.defaultdict(list)
outputs = collections.defaultdict(list)
destinations = {
    'bot': bots,
    'output': outputs
}

def bot_has_values(bots, high, low):
    for bot, values in bots.items():
        if len(values) != 2:
            continue 
        if values[0] == low and values[1] == high:
            return bot
    return None

with open('input.txt', 'r') as instructions:
    for line in instructions:
        instruction = line.strip().split()
        if instruction[0] == 'value':
            init_instructions.append(instruction)
        elif instruction[0] == 'bot':
            source_bot = instruction[1]
            low_type = instruction[5]
            low_id = instruction[6]
            high_type = instruction[10]
            high_id = instruction[11]
            transfer_instructions[source_bot] = {
                'low_type': instruction[5],
                'low_id': instruction[6],
                'high_type': instruction[10],
                'high_id': instruction[11]
            }

for instruction in init_instructions:
    _, value, _, _, _, bot = instruction
    bots[bot].append(int(value))
    bots[bot] = sorted(bots[bot])

while any([len(value) == 2 for value in bots.values()]):
    for bot, values in bots.items():
        if len(values) == 2:
            instruction = transfer_instructions[bot]

            destination = destinations[instruction['low_type']][instruction['low_id']]
            destination.append(values[0])
            destinations[instruction['low_type']][instruction['low_id']] = sorted(destination)

            destination = destinations[instruction['high_type']][instruction['high_id']]
            destination.append(values[1])
            destinations[instruction['high_type']][instruction['high_id']] = sorted(destination)

            bots[bot] = []
            break

print outputs
print outputs['0'][0] * outputs['1'][0] * outputs['2'][0]

