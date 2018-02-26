checksum = 0
with open('input.txt', 'r') as fp:
    for row in fp:
        maximum = 0
        minimum = 99999
        for value in row.split():
            if int(value) < minimum:
                minimum = int(value)
            if int(value) > maximum:
                maximum = int(value) 
        checksum += maximum - minimum
print checksum
