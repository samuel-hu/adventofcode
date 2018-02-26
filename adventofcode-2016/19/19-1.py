num_elves = 3001330
#num_elves = 5

elves = [{'index': i + 1} for i in xrange(num_elves)]
for i in xrange(num_elves - 1):
    elves[i]['next'] = elves[i+1]
elves[-1]['next'] = elves[0]
current_elf = elves[0]
    

while current_elf['next']['index'] != current_elf['index']:
    current_elf['next'] = current_elf['next']['next']
    current_elf = current_elf['next']

print current_elf

