from ipaddress import *

net = ip_network('135.13.142.29/255.255.255.128',0)
for ad in net:
    print(ad)