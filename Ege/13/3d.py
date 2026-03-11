from ipaddress import *

k=0
net = ip_network('142.178.32.160/255.255.255.240',0)
for ad in net:
    ed = bin(int(ad))[2:]
    if ed.count('1') % 2==0:
        k+=1

print(k)