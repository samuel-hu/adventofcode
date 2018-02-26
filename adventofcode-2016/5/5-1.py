import hashlib

door_id = 'abbhdwsy'
counter = 0
password = ''

while len(password) < 8:
    md5_hash = hashlib.md5(door_id + str(counter)).hexdigest()
    if md5_hash[:5] == '00000':
        print md5_hash
        password += md5_hash[5]
    counter += 1

print password
