import hashlib
import re


salt = 'ahsbgdzn'
#salt = 'abc'
index = 0
three_regex = re.compile(r'(.)\1{2}')

num_found = 0

hash_val = None
while num_found < 64:
    hash_val = hashlib.md5(salt + str(index)).hexdigest()

    match = three_regex.search(hash_val)
    if match:
        repeat_char = match.groups()[0]
        inner_index = 0
        five_regex = re.compile(r'(' + repeat_char + r')\1{4}')

        for i in range(index + 1, index + 1000):
            if five_regex.search(hashlib.md5(salt + str(i)).hexdigest()):
                print '-------------------------------------------------------------'
                print index, i
                print hash_val
                print hashlib.md5(salt + str(i)).hexdigest()
                print '-------------------------------------------------------------'
                num_found += 1
                break
    index += 1

print index - 1
