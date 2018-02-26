import hashlib

door_id = 'abbhdwsy'
counter = 0
password = list('_' * 8)

print ''.join(password)
while '_' in password: 
    md5_hash = hashlib.md5(door_id + str(counter)).hexdigest()
    if md5_hash[:5] == '00000':
        position = int(md5_hash[5], 16)
        if position < 8 and password[position] == '_': 
            password[position] = md5_hash[6]
            print ''.join(password)
    counter += 1

print ''.join(password)
