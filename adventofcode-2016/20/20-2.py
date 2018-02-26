total_ips = 4294967296

with open('input.txt', 'r') as fp:
    ranges = [tuple(map(int, row.strip().split('-'))) for row in fp] 
ranges = sorted(ranges, lambda x, y: cmp(int(x[0]), int(y[0])))

start, end = ranges.pop(0)
for i, r in enumerate(ranges):
    r_start, r_end = r
    if start <= r_start <= end + 1:
        if end < r_end:
            end = r_end
    elif r_start > end + 1:
        print start, end, end - start + 1
        total_ips -= (end - start + 1)
        start = r_start
        end = r_end

print start, end, end - start + 1
total_ips -= end - start + 1
print total_ips
