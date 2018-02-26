def get_decompressed_file_length(cf):
    index = 0
    output_length = 0

    while index < len(cf):
        if cf[index] == '(':
            close_index = cf.find(')', index) 
            marker = cf[index+1:close_index]
            length, frequency = marker.split('x')

            repeat_token = cf[close_index+1:close_index+1+int(length)]

            output_length += get_decompressed_file_length(repeat_token) * int(frequency)
            index = close_index + 1 + int(length)
        else:
            output_length += 1
            index += 1
    return output_length


with open('input.txt', 'r') as input_file:
    compressed_file = input_file.readline().strip()

print get_decompressed_file_length(compressed_file)

