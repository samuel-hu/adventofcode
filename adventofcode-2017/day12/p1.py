def parse_programs(filename):
    programs = {}
    with open(filename, 'r') as fp:
        for line in fp:
            program, connected = line.strip().split(' <-> ')
            programs[program] = connected.split(', ')
    return programs


def count_connected(programs, target, connected=None):
    if connected is None:
        connected = set()
    connected.add(target)

    for child in programs[target]:
        if child not in connected:
            count_connected(programs, child, connected)
    
    return len(connected)


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
print count_connected(programs, '0')
