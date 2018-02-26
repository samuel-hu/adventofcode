from itertools import combinations

total = 0
with open('input.txt', 'r') as fp:
    for row in fp:
        values = [int(value) for value in row.split()]
        values.sort(reverse=True)
        pairs = combinations(values, 2) 
        for (a, b) in pairs:
            if a % b == 0:
                total += a / b
                break
print total
