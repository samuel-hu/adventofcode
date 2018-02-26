num_valid = 0

with open('input.txt', 'r') as triangles:
    for triangle in triangles:
        sides = [int(side) for side in triangle.strip().split()]
        sides.sort()
        if sides[0] + sides[1] > sides[2]:
            num_valid += 1
print num_valid
