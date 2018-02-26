def parse_scanners(filename):
    with open(filename, 'r') as fp:
        return [map(int, line.strip().split(': ')) for line in fp]


def at_top_layer(scanner, time):
    s_depth, s_range = scanner
    if s_range < 2:
        return True

    period = (s_range - 2) * 2 + 2
    return time % period == 0


total_severity = 0
scanners = parse_scanners('input.txt')

#scanners = [[0, 3], [1, 2], [4, 4], [6, 4]]

for scanner in scanners:
    if at_top_layer(scanner, scanner[0]):
        total_severity += scanner[0] * scanner[1]        

print total_severity
            
