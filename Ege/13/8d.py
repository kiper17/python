from ipaddress import *

for mask in range(33):
    net = ip_network('99.148.161.94/'+str(mask),0)
    if net.network_address == ip_address('99.148.160.0'):
        print(mask)

#32-19=13