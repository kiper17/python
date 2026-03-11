from ipaddress import *

k=0
net = ip_network('172.16.168.0/255.255.248.0',0)
for ad in net:
    ed = f'{ad:b}'.count('1')
    if ed%5!=0:
        k+=1

print(k)