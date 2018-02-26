'''
sprial grid
37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18 5  4  3  12 29
40 19 6  1  2  11 28
41 20 7  8  9  10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 ...

distances

ring 1      ring 2      ring 3      ring 4
2 + 0 * 8   2 + 1 * 8   2 + 3 * 8   2 + 6 * 8
1 - 0       10 - 3      26 - 5      50 -
2 - 1       11 - 2      27 - 4
3 - 2       12 - 3      28 - 3 
4 - 1       13 - 4      29 - 4
5 - 2       14 - 3      30 - 5
6 - 1       15 - 2      31 - 6
7 - 2       16 - 3      32 - 5
8 - 1       17 - 4      33 - 4
9 - 2       18 - 3      34 - 3
            19 - 2      35 - 4
            20 - 3      36 - 5
            21 - 4      37 - 6
            22 - 3      38 - 5
            23 - 2      39 - 4
            24 - 3      40 - 3
            25 - 4      41 - 2
                        ...
                        49 - 6
'''

from itertools import chain, cycle

def get_ring(index):
    if index == 0:
        return 0

    ring = 1
    width = 1

    current_width = 1
    current_index = 1

    while index != current_index:
        current_index += 1
        current_width += 1
        if current_width > width:
            width += 1
            ring += 1
            current_width = 1
    return ring


target_location = 265149
target_location = 50 

index = (target_location + 6) / 8
ring = get_ring(index)
ring_start = 2 + 8 * ring
print ring, ring_start

ring_cycle = cycle(chain(range(ring * 2, ring, -1), range(ring, ring * 2)))
ring_cycle.next()

distance = ring_cycle.next()
while ring_start != target_location:
    distance = ring_cycle.next()
    ring_start += 1
print target_location, distance

'''
current_location = 1
current_coordinate = (0, 0)

while current_location != target_location:
    #move to next coordinate
    
    current_location += 1
'''
