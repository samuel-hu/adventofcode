import copy


def is_valid_floor(floor):
    for item in floor:
        if not item.is_generator():
            if any(maybe_generator.is_generator() for maybe_generator in floor) and \
                not any(maybe_generator.element == item.element and maybe_generator.is_generator() for maybe_generator in floor):
                return False
    return True

def get_item_combinations(floor):
    combos = [[item] for item in floor]
    for item_outer in floor:
        for item_inner in floor:
           if item_outer != item_inner:
                combos.append([item_outer, item_inner])
    return combos


class Item(object):
    def __init__(self, item_string):
        element, item_type = item_string.split(' ')

        self.item_type = item_type
        if item_type == 'microchip':
            element = element[:element.find('-')]
        self.element = element

    def __repr__(self):
        return '{} {}'.format(self.element, self.item_type)

    def __eq__(self, other):
        return self.element == other.element and self.item_type == other.item_type

    def __hash__(self):
        return hash(self.element + self.item_type)

    def is_generator(self):
        return self.item_type == 'generator'


class State(object):
    def __init__(self, floors, elevator, depth):
        self.floors = floors 
        self.elevator = elevator
        self.depth = depth

    def __repr__(self):
        r = ''
        for index, floor in enumerate(self.floors):
#            r += 'f{}: ['.format(index) + ', '.join([item.__repr__() for item in floor]) + ']'
            r += 'f{}: '.format(index) + floor.__repr__() 
            r += '\n'
        r += 'elevator: {}\n'.format(self.elevator)
        r += 'depth: {}\n'.format(self.depth)
#        r += 'parent: {}\n'.format(self.parent)
        return '#####\n{}#####\n'.format(r)

    def __eq__(self, other):
        if self.elevator != other.elevator:
            return False
        for index, floor in enumerate(self.floors):
            if floor != other.floors[index]:
                return False
        return True

    def __hash__(self):
        h = ''
        for floor in self.floors:
            h += ''.join(i.__repr__() for i in sorted(floor, cmp=lambda x,y: cmp(x.__repr__(), y.__repr__())))
        return hash(h + str(self.elevator))

    def to_str(self):
        r = ''
        for index, floor in enumerate(self.floors):
            r += 'f{}: ['.format(index) + ', '.join([item.__repr__() for item in floor]) + ']'
            r += '\n'
        r += 'elevator: {}\n'.format(self.elevator)
        return r

    def is_valid_state(self):
        for floor in self.floors:
            if not is_valid_floor(floor):
                return False
        return True

    def is_final_state(self):
        if len(self.floors[0]) + len(self.floors[1]) + len(self.floors[2]) == 0:
            return True 
        return False

    def gen_next_states(self):
        next_states = []
        elevator = self.elevator
        current_floor = self.floors[elevator]
        for combo in get_item_combinations(current_floor):
            if elevator - 1 >= 0:
                new_floor_state = self.move_floors(elevator, elevator - 1, combo)
                state = State(new_floor_state, elevator - 1, self.depth + 1)
                if state.is_valid_state():
                    next_states.append(state)
            if elevator + 1 < 4:
                new_floor_state = self.move_floors(elevator, elevator + 1, combo)
                state = State(new_floor_state, elevator + 1, self.depth + 1)
                if state.is_valid_state():
                    next_states.append(state)
        return next_states
        
    def move_floors(self, from_floor, to_floor, items):
        new_floor_state = copy.deepcopy(self.floors)
        for item in items:
            new_floor_state[from_floor].remove(item)
            new_floor_state[to_floor].add(item)
        return new_floor_state


test_floor = set([
    Item('polonium generator'), 
    Item('polonium-compatible microchip'),
    Item('thulium-compatible microchip'),
    Item('thulium generator')
])
test_floor2 = set([
    Item('thulium-compatible microchip'),
    Item('polonium-compatible microchip'),
    Item('polonium generator'), 
    Item('thulium generator')
])
test_state = State([test_floor, set(), set(), set()], 0, 0)
test_state2 = State([test_floor2, set(), set(), set()], 0, 0)

#print sorted(test_floor, cmp=lambda x,y: cmp(x.__repr__(), y.__repr__()))

#searched = set()
#searched.add(test_state2)
#print test_state in searched
#raise RuntimeError
#print test_state2 in [test_state]
#raise RuntimeError
#print test_state.is_valid_state()
#print test_state.is_final_state()
#print test_floor
#test_floor.remove(Item('polonium generator'))
#raise RuntimeError
                

floors = []
states = []
with open('input.txt', 'r') as floor_configs:
    for floor_config in floor_configs:
        if 'nothing relevant' in floor_config:
            floors.append(set())
        else:
            floor_config = floor_config.replace(' and ', ' ').strip()
            floor_config = floor_config[floor_config.find('contains') + 9:]
            floor_config = floor_config.split('a ')
            floor = [Item(item.strip().replace(',', '').replace('.', '')) for item in floor_config if len(item) > 0]
#            floor = set(Item(item.strip().replace(',', '').replace('.', '')) for item in floor_config if len(item) > 0)
            print floor
            floor = set(floor)
            floors.append(floor)

count = 0
current_state = State(floors, 0, 0)
print current_state
searched_states = set() 

while not current_state.is_final_state():
    searched = current_state in searched_states
    if current_state.is_valid_state() and not searched:
        states.extend(current_state.gen_next_states())

    if not searched:
        searched_states.add(current_state)

    count += 1
    if not count % 1000:
        print count
        print current_state.depth
        print len(searched_states)
        print

    current_state = states.pop(0)

print current_state

