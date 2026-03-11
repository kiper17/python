from ipaddress import *

for mask in range(33):
    net = ip_network('145.192.94.230/'+str(mask),0)
    if net.network_address == ip_address('145.192.80.0'):
        print(mask-16)