# def is_valid_IP(strng):
#     lenstr = len(strng.split('.'))
#     if lenstr < 4 or strng == '':
#         return False
#     for i in strng.split('.'):
#         for j in i:
#             if j in ' -':
#                 return False
#         if i.isalpha() or int(i) > 255 or (len(i) > 1 and i[0] == '0'):
#             return False
#     return True

# def is_valid_IP(ip):
#     octets = ip.split('.')
#     if len(octets) != 4: return False
#     for octet in octets:
#         if not is_valid_octet(octet):
#             return False
#     return True
#
# def is_valid_octet(octet):
#     if not octet.isdigit():
#         return False
#     if len(octet) > 1 and octet[0] == '0':
#         return False
#     octet = int(octet)
#     if octet >= 0 and octet <= 255:
#         return True
#     else:
#         return False

import socket


def is_valid_IP(addr):
    try:
        socket.inet_pton(socket.AF_INET, addr)
        return True
    except socket.error:
        return False


print(is_valid_IP('123.45.67.89'))
print(is_valid_IP(''))
print(is_valid_IP('123.045.067.089'))
print(is_valid_IP('abc.def.ghi.jkl'))
print(is_valid_IP('123.456.789.0'))
print(is_valid_IP('12.34.56'))
print(is_valid_IP('12.34.56 .1'))
print(is_valid_IP('12.34.56.-1'))
print(is_valid_IP('123.045.067.089'))
print(is_valid_IP('127.1.1.0'))
print(is_valid_IP('0.0.0.0'))
print(is_valid_IP('0.34.82.53'))
print(is_valid_IP('192.168.1.300'))
