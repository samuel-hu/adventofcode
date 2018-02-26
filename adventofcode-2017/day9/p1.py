def get_stream(filename):
    with open(filename, 'r') as fp:
        char = fp.read(1)
        while char != '\n':
            yield char
            char = fp.read(1)
        raise StopIteration


def process_stream(stream):
    current_point_value = 0
    total_points = 0
    try:
        char = stream.next()
        while(True):
            if char == '{':
                current_point_value += 1
            elif char == '}':
                total_points += current_point_value
                current_point_value -= 1
            elif char == '!':
                stream.next()
            elif char == '<':
                char = stream.next()
                while char != '>':
                    if char == '!':
                        stream.next()
                    char = stream.next()
            char = stream.next()
    except StopIteration:
        pass
    return total_points


stream = get_stream('input.txt')
print process_stream(stream)

