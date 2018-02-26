def get_lengths(filename):
    with open(filename, 'r') as fp:
        return map(int, fp.read().strip().split(','))


def shift_list(circular_list, offset):
    return circular_list[offset:len(circular_list)] + circular_list[0:offset]


def reverse_partial(circular_list, position, length):
    if length > len(circular_list):
        raise RuntimeError('invalid length {}'.format(length))
    lst = shift_list(circular_list, position)
    rev_list = lst[0:length][::-1] + lst[length:len(lst)]
    return shift_list(rev_list, -position)


circular_list = list(range(256))
lengths = get_lengths('input.txt')

#circular_list = list(range(5))
#lengths = [3,4,1,5]

position = 0
skip_size = 0

for length in lengths:
    circular_list = reverse_partial(circular_list, position, length)
    position += length + skip_size
    position %= len(circular_list)
    skip_size += 1

print circular_list
x, y = circular_list[0], circular_list[1]
print '{} * {} = {}'.format(x, y, x * y)
