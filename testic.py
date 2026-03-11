from ipaddress import *

k=0
for mask in range(33):
    net1=ip_network('206.140.112.232/'+str(mask),0)
    net2 = ip_network('206.140.112.224/'+str(mask),0)
    if net1.network_address == net2.network_address:
        print(mask)

print(int('11110000',2))