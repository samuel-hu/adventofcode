from operator import xor


def get_lengths(filename):
    suffix = [17, 31, 73, 47, 23]
    with open(filename, 'r') as fp:
        return map(ord, list(fp.read().strip())) + suffix


def shift_list(circular_list, offset):
    return circular_list[offset:len(circular_list)] + circular_list[0:offset]


def reverse_partial(circular_list, position, length):
    if length > len(circular_list):
        raise RuntimeError('invalid length {}'.format(length))

    lst = shift_list(circular_list, position)
    rev_list = lst[0:length][::-1] + lst[length:len(lst)]
    return shift_list(rev_list, -position)


def get_chunks(l, size):
    for i in range(0, len(l), size):
        yield l[i:i+size]


def condense(circular_list):
    chunks = list(get_chunks(circular_list, 16))
    return map(lambda x: reduce(xor, x), chunks)


def to_hex(dense_hash):
    return reduce(lambda x, y: x + '{:02x}'.format(y), dense_hash, '')


total_rounds = 64
circular_list = list(range(256))
lengths = get_lengths('input.txt')
position = 0
skip_size = 0

for i in range(total_rounds):
    for length in lengths:
        circular_list = reverse_partial(circular_list, position, length)
        position += length + skip_size
        position %= len(circular_list)
        skip_size += 1

dense_hash = condense(circular_list)
print dense_hash
print to_hex(dense_hash)

