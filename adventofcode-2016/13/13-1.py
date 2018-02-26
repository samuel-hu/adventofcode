def is_final(coordinate):
    return coordinate == (31, 39)

def is_open(state):
    key = 1364
    x, y = state['location']
    val = x*x + 3*x + 2*x*y + y + y*y + key
    
    one_bits = 0
    while val:
        one_bits += val & 1 
        val = val >> 1
    if one_bits % 2:
        return False 
    return True 

def gen_next_states(current_state):
    current_location = current_state['location']
    current_distance = current_state['distance']
    new_states = [
        {
            'location': (current_location[0] + 1, current_location[1]),
            'distance': current_distance + 1
        },
        {
            'location': (current_location[0] - 1, current_location[1]),
            'distance': current_distance + 1
        },
        {
            'location': (current_location[0], current_location[1] + 1),
            'distance': current_distance + 1
        },
        {
            'location': (current_location[0], current_location[1] - 1),
            'distance': current_distance + 1
        }
    ]
    return filter(is_open, new_states)


searched_coordinates = set()
states_to_search = []
current_state = {
    'location': (1, 1),
    'distance': 0
}

while not is_final(current_state['location']):
    if current_state['location'] not in searched_coordinates:
        states_to_search.extend(gen_next_states(current_state))
        searched_coordinates.add(current_state['location'])
    current_state = states_to_search.pop(0)
    
print current_state
