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

def get_most_frequent(count):
    most_frequent_char = None
    most_frequent_count = 0
    for k, v in count.items():
        if v > most_frequent_count:
            most_frequent_count = v
            most_frequent_char = k
    return most_frequent_char

with open('input.txt', 'r') as message:
    for line in message:
        for index, char, in enumerate(line.strip()):
            counts[index][char] += 1
print ''.join([get_most_frequent(count) for count in counts])

