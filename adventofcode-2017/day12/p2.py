def parse_programs(filename):
    programs = {}
    with open(filename, 'r') as fp:
        for line in fp:
            program, connected = line.strip().split(' <-> ')
            programs[program] = connected.split(', ')
    return programs


def get_connected(programs, target, connected=None):
    if connected is None:
        connected = set()
    connected.add(target)

    for child in programs[target]:
        if child not in connected:
            get_connected(programs, child, connected)
    
    return connected


programs = parse_programs('input.txt')
'''
programs = {
    '0': ['2'],
    '1': ['1'],
    '2': ['0', '3', '4'],
    '3': ['2', '4'],
    '4': ['2', '3', '6'],
    '5': ['6'],
    '6': ['4', '5']
}
'''

num_groups = 0
has_group = set()
for program in programs:
    if program not in has_group:
        num_groups += 1
        has_group = has_group | get_connected(programs, program)
    
print num_groups
