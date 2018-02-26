from copy import deepcopy


STARTING_FLOORS = [
    ['1g', '2g', '3m', '3g', '4g', '4m', '5g', '7g', '7m', '6g', '6m', '5m'],
    ['1m', '2m'],
    [],
    []
]
NUM_PAIRS = 8
STARTING_CONFIG = {
    'depth': 0,
    'elevator': 0,
    'floors': [sorted(floor) for floor in STARTING_FLOORS]
}


def is_final(config):
    if len(config['floors'][0]) == 0 \
        and len(config['floors'][1]) == 0 \
        and len(config['floors'][2]) == 0:
        return True
    return False

def is_valid(config):
    for floor in config['floors']:
        generators = []
        microchips = []
        for item in floor:
            if item[-1] == 'g':
                generators.append(item)
            else:
                microchips.append(item)

        if any(generators):
            for microchip in microchips:
                if microchip[:-1] + 'g' not in generators:
                    return False
    return True

def get_pairs(config, num_pairs=0):
    #return a list of floor pairs -> ["gen_floor + chip_floor"]
    pairs = ['xx' for i in range(num_pairs)]
    for index, floor in enumerate(config['floors']):
        for item in floor:
            if item[-1] == 'g':
                pairs[int(item[:-1]) - 1] = str(index) + pairs[int(item[:-1]) - 1][1]
            else:
                pairs[int(item[:-1]) - 1] = pairs[int(item[:-1]) - 1][0] + str(index)
    return sorted(pairs)

def get_hash(config, num_pairs=0):
    return ''.join(get_pairs(config, num_pairs)) + str(config['elevator'])

def get_movement_combos(floor):
    combos = []
    for item in floor:
        if item[-1] == 'g':
            paired_chip = item[:-1] + 'm'
            if paired_chip in floor:
                combos.append([item, paired_chip])
                break

    for i, outer in enumerate(floor):
        for j in range(len(floor) - i):
            inner = floor[j + i]
            if outer == inner:
                combos.append([outer])
            elif outer[-1] == inner[-1]:
                combos.append([outer, inner])
    
    return combos

def move_floors(floors, from_floor, to_floor, items):
    new_floors = deepcopy(floors)
    for item in items:
        new_floors[from_floor].remove(item)
        new_floors[to_floor].append(item)
    return [sorted(floor) for floor in new_floors]

def gen_new_configs(config):
    new_configs = []
    elevator = config['elevator']
    floors = config['floors']
    current_floor = floors[elevator]

    for combo in get_movement_combos(current_floor):
        # move items down
        if elevator > 0:
            new_floors = move_floors(floors, elevator, elevator - 1, combo)
            new_state = {
                'depth': config['depth'] + 1,
                'elevator': elevator - 1,
                'floors': new_floors
            }
            if is_valid(new_state):
                new_configs.append(new_state)

        # move items up
        if elevator < 3:
            new_floors = move_floors(floors, elevator, elevator + 1, combo)
            new_state = {
                'depth': config['depth'] + 1,
                'elevator': elevator + 1,
                'floors': new_floors
            }
            if is_valid(new_state):
                new_configs.append(new_state)

    return new_configs



''' TESTS
print STARTING_CONFIG
Print is_final(STARTING_CONFIG)
print is_valid(STARTING_CONFIG)
print get_pairs(STARTING_CONFIG, NUM_PAIRS)
print get_movement_combos(STARTING_CONFIG['floors'][0])
'''

searched_configs = set()
configs_to_search = []
current_config = STARTING_CONFIG
count = 0

while not is_final(current_config):
    if is_valid(current_config):
        config_hash = get_hash(current_config, NUM_PAIRS)
        if config_hash not in searched_configs:
            configs_to_search.extend(gen_new_configs(current_config))
            searched_configs.add(config_hash)
    
    count += 1
    if not count % 1000:
        print current_config

    current_config = configs_to_search.pop(0)

print '##############################################################'
print current_config
print '##############################################################'

