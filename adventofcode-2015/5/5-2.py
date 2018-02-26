import re

two_letter_pair = re.compile(r'(.{2}).*\1')
letter_in_between = re.compile(r'(.).{1}\1')

def nice_word(word):
    if re.search(two_letter_pair, word) and re.search(letter_in_between, word):
        return True
    return False

num_nice = 0
with open('input.txt', 'r') as f:
    for word in f:
        if nice_word(word):
            num_nice += 1
print num_nice
