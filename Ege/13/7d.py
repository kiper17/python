from ipaddress import *

for mask in range(33):
    net = ip_network('118.187.59.255/'+str(mask),0)
    net1 = ip_network('118.187.65.115/'+str(mask),0)
    if net.network_address != net1.network_address:
        print(mask)