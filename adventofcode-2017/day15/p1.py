class Generator(object):
    def __init__(self, start, factor):
        self.start = start
        self.factor = factor
        self.divider = 2147483647

    def generate(self):
        self.start *= self.factor
        self.start %= self.divider
        return self.start


def right_sixteen_bits_match(x, y):
    return x & 0xffff == y & 0xffff


total_matches = 0
generator_a = Generator(699, 16807)
generator_b = Generator(124, 48271)

for i in range(40000000):
    if right_sixteen_bits_match(
        generator_a.generate(),
        generator_b.generate()
    ):
        total_matches += 1

print total_matches

