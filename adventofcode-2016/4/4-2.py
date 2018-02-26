from collections import defaultdict
import re


regex = '([^\d]+)([\d]+)\[(\D+)\]'


def shift(cipher, shift_value):
    plaintext = ''
    for char in cipher:
        if char != '-':
            char_offset = (ord(char) - ord('a') + (shift_value % 26)) % 26
            plaintext += chr(char_offset + ord('a'))
        else:
            plaintext += ' '
    return plaintext


with open('input.txt', 'r') as rooms:
    for room in rooms:
        match = re.search(regex, room.strip())
        name, room_id, checksum = match.groups()
        
        plain_name = shift(name, int(room_id))
#        if 'santa' in plain_name:
        print plain_name
        print room_id
