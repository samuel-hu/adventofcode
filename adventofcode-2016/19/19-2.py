num_elves = 3001330
#num_elves = 5

elves = [{'index': i + 1} for i in xrange(num_elves)]
for i in xrange(num_elves - 2):
    elves[i+1]['next'] = elves[i+2]
    elves[i+1]['prev'] = elves[i]
elves[-1]['next'] = elves[0]
elves[-1]['prev'] = elves[-2]
elves[0]['next'] = elves[1]
elves[0]['prev'] = elves[-1]

current_elf = elves[0]
half = elves[num_elves / 2]
count = 0
while current_elf['next']['index'] != current_elf['index']:
    half['prev']['next'] = half['next']
    half['next']['prev'] = half['prev']
    half = half['next']

    if (num_elves - count) % 2:
        half = half['next']

    count += 1
    current_elf = current_elf['next']

print current_elf

