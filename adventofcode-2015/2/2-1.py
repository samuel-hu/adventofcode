with open('input.txt', 'r') as f:
    total = 0
    for present in f:
        dimensions = sorted(
            map(
                lambda x: int(x),
                present.strip().split('x')
            )
        )
        total += (3 * dimensions[0] * dimensions[1]) + \
                 (2 * dimensions[1] * dimensions[2]) + \
                 (2 * dimensions[0] * dimensions[2])

    print total
