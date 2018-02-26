def parse_scanners(filename):
    with open(filename, 'r') as fp:
        return [map(int, line.strip().split(': ')) for line in fp]


def at_top_layer(scanner, time):
    s_depth, s_range = scanner
    if s_range < 2:
        return True

    period = (s_range - 2) * 2 + 2
    return (s_depth + time) % period == 0


time = 0
safe = False
scanners = parse_scanners('input.txt')

#scanners = [[0, 3], [1, 2], [4, 4], [6, 4]]

while not safe:
    time += 1
    if not any(map(lambda s: at_top_layer(s, time), scanners)):
        safe = True

    if not time % 10000:
        print time
        print map(lambda s: at_top_layer(s, time), scanners)
        
print time
            
