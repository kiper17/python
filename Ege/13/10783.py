from ipaddress import *

for mask in range(33):
    net = ip_network('121.171.5.105/'+str(mask),0)
    net1 = ip_network('121.171.5.70/'+str(mask),0)
    if net.network_address == net1.network_address:
        print(mask)