import hashlib


def is_final(location):
    return location == (3, 3)


def get_doors(location, passcode, path):
    open_codes = 'bcdef'
    hash_val = hashlib.md5(passcode + path).hexdigest()[:4]
    doors = {
        'U': hash_val[0] in open_codes if location[1] > 0 else False, # up
        'D': hash_val[1] in open_codes if location[1] < 3 else False, # down
        'L': hash_val[2] in open_codes if location[0] > 0 else False, # left
        'R': hash_val[3] in open_codes if location[0] < 3 else False  # right 
    }
    return doors


def move(location, direction):
    operations = {
        'U': lambda location: (location[0], location[1] - 1),
        'D': lambda location: (location[0], location[1] + 1),
        'L': lambda location: (location[0] - 1, location[1]),
        'R': lambda location: (location[0] + 1, location[1])
    }
    return operations[direction](location)


def get_new_states(location, passcode, path):
    new_states = []
    doors = get_doors(location, passcode, path)
    for direction, is_open in doors.items():
        if is_open:
            new_states.append({
                'location': move(location, direction),
                'path': path + direction
            })
    return new_states
    

passcode = 'vkjiggvb'
current_state = {
    'location': (0, 0),
    'path': ''
}
next_states = []

while not is_final(current_state['location']):
    cs = current_state
    next_states.extend(get_new_states(cs['location'], passcode, cs['path']))
    current_state = next_states.pop(0)

print current_state

