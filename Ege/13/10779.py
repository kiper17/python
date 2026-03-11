from ipaddress import *

for mask in range(33):
    net1 = ip_network('201.92.0.49/'+str(mask),0)
    net2 = ip_network('201.92.0.20/'+str(mask),0)
    if net1.network_address == net2.network_address:
        print(mask)

print(2**6 -4)