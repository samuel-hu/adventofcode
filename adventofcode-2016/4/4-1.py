from collections import defaultdict
import re


regex = '([^\d]+)([\d]+)\[(\D+)\]'
sum_of_ids = 0

def compare(x, y):
    if x[1] == y[1]:
        return cmp(y[0], x[0])
    return cmp(x[1], y[1])

def get_checksum(name):
    totals = defaultdict(int)
    for char in name:
        totals[char] += 1
    checksum = sorted(totals.items(), cmp=compare, reverse=True)
    return ''.join([item[0] for item in checksum])[:5]

with open('input.txt', 'r') as rooms:
    for room in rooms:
        match = re.search(regex, room.strip())
        name, room_id, checksum = match.groups()
        name = name.replace('-', '')
        
        if get_checksum(name) == checksum:
            sum_of_ids += int(room_id)

print sum_of_ids
