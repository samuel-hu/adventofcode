def hashed(state):
    return '-'.join(str(i) for i in [state['location'][0], state['location'][1], state['found']])

def gen_next_states(state, hvac_map):
    new_states = []
    curr_x, curr_y = state['location']

    new_locations = [(curr_x - 1, curr_y), (curr_x + 1, curr_y), (curr_x, curr_y - 1), (curr_x, curr_y + 1),]
    for new_location in new_locations:
        new_x, new_y = new_location 
        location_type = hvac_map[new_y][new_x]
        if location_type != '#':
            new_state = {
                'location': (new_x, new_y),
                'found': state['found'],
                'steps': state['steps'] + 1
            }
            try:
                new_state['found'] = new_state['found'] | (1 << int(location_type))
            except ValueError:
                pass
            new_states.append(new_state)
    return new_states

hvac_map = []
start_location = None

with open('input.txt', 'r') as fp:
    for line in fp:
        row = [space for space in line.strip()]

        try:
            start_x = row.index('0')
            start_location = (start_x, len(hvac_map))
        except ValueError:
            pass

        hvac_map.append(row)

current_state = {
    'location': start_location,
    'found': 1,
    'steps': 0
}
states_to_search = []
searched_states = set()

while current_state['found'] != 0b11111111 or current_state['location'] != start_location:
    if hashed(current_state) not in searched_states:
        states_to_search.extend(gen_next_states(current_state, hvac_map)) 
        searched_states.add(hashed(current_state))
    current_state = states_to_search.pop(0)
    
print current_state
