from ipaddress import *

valid = [0,128,192,224,240,248,252,254,255]

for A in valid:
    net = ip_network(f'255.112.1.136/255.255.{A}.0', strict=False)
    if all(
        f'{int(ad):032b}'[:16].count('1') >= 
        f'{int(ad):032b}'[16:].count('1')
        for ad in net
    ):
        print(A)
        break