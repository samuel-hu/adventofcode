from knot_hash import knot_hash


def count_bits(n):
    count = 0
    while n:
        count += n & 1
        n = n >> 1
    return count



key_string = 'oundnydw'
num_used = 0

for i in range(128):
    row_hash = knot_hash('{}-{}'.format(key_string, i))
    num_used += count_bits(int(row_hash, 16))

print num_used
    
