import hashlib
import re


def get_hash(input_str, index, searched):
    if index < len(searched):
        return searched[index]

    for i in range(2017):
        input_str = hashlib.md5(input_str).hexdigest()
    searched.append(input_str)
    return input_str


salt = 'ahsbgdzn'
#salt = 'abc'
index = 0
three_regex = re.compile(r'(.)\1{2}')

num_found = 0
searched = []

hash_val = None
while num_found < 64:
    hash_val = get_hash(salt + str(index), index, searched)

    match = three_regex.search(hash_val)
    if match:
        repeat_char = match.groups()[0]
        inner_index = 0
        five_regex = re.compile(r'(' + repeat_char + r')\1{4}')

        for i in range(index + 1, index + 1000):
            if five_regex.search(get_hash(salt + str(i), i, searched)):
                num_found += 1

                print '-------------------------------------------------------------'
                print index, i
                print hash_val
                print get_hash(salt + str(i), i, searched)
                print '-------------------------------------------------------------'


                break
    index += 1

print index - 1
