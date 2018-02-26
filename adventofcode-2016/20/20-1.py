with open('input.txt', 'r') as fp:
    ranges = [tuple(map(int, row.strip().split('-'))) for row in fp] 
ranges = sorted(ranges, lambda x, y: cmp(int(x[0]), int(y[0])))

start, end = ranges.pop(0)
for r in ranges:
    r_start, r_end = r
    if start <= r_start <= end + 1:
        if end < r_end:
            end = r_end
    elif start > end + 1:
        break
print start, end
