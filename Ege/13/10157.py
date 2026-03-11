from ipaddress import *

for mask in range(33):
    net = ip_network('241.185.253.57/'+str(mask),0)
    if net.network_address == ip_address('241.185.252.0'):
        print(mask)