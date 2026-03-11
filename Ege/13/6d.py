from ipaddress import *

k=0
net = ip_network('187.127.0.0/255.255.240.0',0)
for ad in net:
    ed = f'{ad:b}'.count('1')
    if ed%3==0:
        k+=1

print(k)