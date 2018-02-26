num_steps = 355

buf = [0]
position = 0

for i in range(5 * (10 ** 7)):
    if not i % 10000:
        print i
    position = (position + num_steps) % len(buf)
    buf = buf[:position+1] + [i + 1] + buf[position+1:]
    position = (position + 1) % len(buf)

zero_index = buf.index(0)
print buf[zero_index-1:zero_index+2]
