from ipaddress import *

net = ip_network('190.202.83.62/255.255.252.0',0)
for ad in net:
    print(ad)

print(190+202+83+254)