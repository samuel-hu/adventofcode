# rnqfzoisbqxbdlkgfh[lwlybvcsiupwnsyiljz]kmbgyaptjcsvwcltrdx[ntrpwgkrfeljpye]jxjdlgtntpljxaojufe
import re

regex = '\[\D*?\]'
support_tls_count = 0

def has_abba(token):
    if len(token) < 4:
        return False

    for i in range(len(token) - 3):
        sub_token = token[i:i+4]
        if sub_token[0] != sub_token[1] and sub_token[0:2] == ''.join(reversed(sub_token[2:4])):
            return True
    return False

def supports_tls(ip):
    outside_brackets = re.split(regex, ip)
    within_brackets = re.findall(regex, ip)

    for token in within_brackets:
        if has_abba(token):
            return False
    for token in outside_brackets:
        if has_abba(token):
            return True
    return False
   
with open('input.txt', 'r') as ips:
    for ip in ips:
        if supports_tls(ip):
            support_tls_count += 1
print support_tls_count
 
