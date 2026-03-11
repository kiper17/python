from ipaddress import *

for mask in range(33):
    net = ip_network('215.181.200.27/'+str(mask),0)
    if net.network_address == ip_address('215.181.192.0'):
        print(mask)

print(int('11110000',2))