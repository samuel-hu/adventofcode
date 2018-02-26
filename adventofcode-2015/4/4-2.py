import hashlib

with open('input.txt', 'r') as f:
    key = f.read().strip()
    sequence = 1 
    found = False

    while not found:
        md5 = hashlib.md5()
        md5.update('{key}{sequence}'.format(key=key, sequence=sequence))
        md5_hash = int(md5.hexdigest(), 16)

        print (sequence, md5.hexdigest(), hex(md5_hash >> (26 * 4)))

        if not md5_hash >> (26 * 4):
            print sequence
            found = True
        else:
            sequence += 1
