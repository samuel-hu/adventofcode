import re

regex = '\[\D*?\]'
support_ssl_count = 0

def get_abas(token):
    abas = []
    if len(token) < 3:
        return abas 

    for i in range(len(token) - 2):
        sub_token = token[i:i+3]
        if sub_token[0] != sub_token[1] and sub_token[0:2] == ''.join(reversed(sub_token[1:3])):
            abas.append(sub_token) 
    return abas 

def supports_ssl(ip):
    outside_brackets = re.split(regex, ip)
    supernet_abas = []

    within_brackets = re.findall(regex, ip)
    hypernet_babs = []

    for token in within_brackets:
        hypernet_babs.extend(get_abas(token))

    for token in outside_brackets:
        supernet_abas.extend(get_abas(token))

    if len(supernet_abas) == 0:
        return False

    for aba in supernet_abas:
        if aba[1] + aba[0] + aba[1] in hypernet_babs:
#            print supernet_abas
#            print hypernet_babs 
            return True
    return False
   
with open('input.txt', 'r') as ips:
    for ip in ips:
        if supports_ssl(ip):
            support_ssl_count += 1
            print ip
#            raise RuntimeError
print support_ssl_count
 
