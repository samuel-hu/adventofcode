import re

three_vowels = re.compile(r'.*[aeiou].*[aeiou].*[aeiou].*')
twice_in_row = re.compile(r'(.)\1')
bad_strings = re.compile(r'(ab|cd|pq|xy)')

def nice_word(word):
    if re.search(bad_strings, word):
        return False
    if re.search(three_vowels, word) and re.search(twice_in_row, word):
        return True
    return False

num_nice = 0
with open('input.txt', 'r') as f:
    for word in f:
        if nice_word(word):
            num_nice += 1
print num_nice
