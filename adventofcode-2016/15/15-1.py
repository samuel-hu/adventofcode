def can_get_capsule(starting_time):
    disc_max_positions = [13, 19, 3, 7, 5, 17]
    disc_starting_positions = [1, 10, 2, 1, 3, 5]

    for i in range(len(disc_starting_positions)):
        disc_position = (starting_time + 1 + i + disc_starting_positions[i]) % disc_max_positions[i] 
        if disc_position:
            return False
    print starting_time
    return True


time = 0
while not can_get_capsule(time):
    time += 1

