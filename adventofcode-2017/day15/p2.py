class Generator(object):
    def __init__(self, start, factor, multiple):
        self.start = start
        self.factor = factor
        self.divider = 2147483647
        self.multiple = multiple

    def generate(self):
        while True:
            self.start *= self.factor
            self.start %= self.divider
            if self.start % self.multiple == 0:
                return self.start


def right_sixteen_bits_match(x, y):
    return x & 0xffff == y & 0xffff


total_matches = 0
generator_a = Generator(699, 16807, 4)
generator_b = Generator(124, 48271, 8)

for i in range(5000000):
    if right_sixteen_bits_match(
        generator_a.generate(),
        generator_b.generate()
    ):
        total_matches += 1

print total_matches

