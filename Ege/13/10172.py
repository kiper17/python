from ipaddress import *

for mask in range(33-6):
    net = ip_network('175.122.80.13/'+str(mask),0)
    if net.network_address == ip_address('175.122.80.0'):
        print(mask)