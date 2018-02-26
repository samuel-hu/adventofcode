index = 0
output = ''

with open('input.txt', 'r') as input_file:
    compressed_file = input_file.readline().strip()
    cf = compressed_file
    while index < len(cf):
        if cf[index] == '(':
            close_index = cf.find(')', index) 
            marker = cf[index+1:close_index]
            length, frequency = marker.split('x')
            repeat_token = cf[close_index+1:close_index+1+int(length)]
            output += (repeat_token * int(frequency))
            index = close_index + 1 + int(length)
        else:
            output += cf[index]
            index += 1

print len(output)

