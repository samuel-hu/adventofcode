num_valid = 0
with open('input.txt', 'r') as fp:
    for line in fp:
        phrases = line.split()
        if len(phrases) == len(set(phrases)):
            num_valid += 1
print num_valid
