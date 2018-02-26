import sys
from collections import defaultdict


counts = [
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int),
    defaultdict(int)
]

def get_least_frequent(count):
    least_frequent_char = None
    least_frequent_count = sys.maxint 
    for k, v in count.items():
        if v < least_frequent_count:
            least_frequent_count = v
            least_frequent_char = k
    return least_frequent_char

with open('input.txt', 'r') as message:
    for line in message:
        for index, char, in enumerate(line.strip()):
            counts[index][char] += 1
print ''.join([get_least_frequent(count) for count in counts])

