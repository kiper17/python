from ipaddress import *

k=0
for mask in range(33):
    net1 = ip_network('95.24.2.9/'+str(mask),0)
    net2 = ip_network('95.24.3.10/'+str(mask),0)
    if net1.network_address == net2.network_address:
        print(mask)

mask1 = 23
net = ip_network('95.24.2.9/'+str(mask1),0)
for ad in net:
    ed = f'{ad:b}'.zfill(32).count('0')
    if ed%2==0:
        k+=1

print(k)