from ipaddress import *

k=0
net = ip_network('242.67.112.134/255.255.255.192',0)
for ad in net:
    ed = f'{ad:b}'
    pr = ed[:16]
    lt = ed[16:]
    if pr.count('1')>=lt.count('1'):
        k+=1

print(k)