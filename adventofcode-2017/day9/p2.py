def get_stream(filename):
    with open(filename, 'r') as fp:
        char = fp.read(1)
        while char != '\n':
            yield char
            char = fp.read(1)
        raise StopIteration


def process_stream(stream):
    garbage_count = 0
    try:
        char = stream.next()
        while(True):
            if char == '!':
                stream.next()
            elif char == '<':
                char = stream.next()
                while char != '>':
                    if char == '!':
                        stream.next()
                    else:
                        garbage_count += 1
                    char = stream.next()
            char = stream.next()
    except StopIteration:
        pass
    return garbage_count


stream = get_stream('input.txt')
print process_stream(stream)

