input_data = '11110010111001001'
disk_size = 35651584


def generate_data(input_data, disk_size):
    data = input_data
    while len(data) < disk_size:
        reverse = data[::-1]
        reverse = ''.join(['0' if char == '1' else '1' for char in reverse])
        data = data + '0' + reverse
    return data[:disk_size]


def generate_checksum(data):
    checksum = ''
    for i in range(0, len(data), 2):
        if data[i] == data[i+1]:
            checksum += '1'
        else:
            checksum += '0' 
    return checksum


data = generate_data(input_data, disk_size)
checksum = generate_checksum(data)
while not len(checksum) % 2:
    checksum = generate_checksum(checksum)
print checksum

