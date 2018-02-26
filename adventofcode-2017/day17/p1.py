num_steps = 355

buf = [0]
position = 0

for i in range(2017):
    position = (position + num_steps) % len(buf)
    buf = buf[:position+1] + [i + 1] + buf[position+1:]
    position = (position + 1) % len(buf)

print buf[position-1:position+2]
