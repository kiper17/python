from ipaddress import *

for mask in range(33):
    net = ip_network('112.117.121.80/'+str(mask),0)
    net1 = ip_network('112.117.107.170/'+str(mask),0)
    if net.network_address == net1.network_address:
        print(mask)

print(int('11100000',2))