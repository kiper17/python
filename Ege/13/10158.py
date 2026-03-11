from ipaddress import *

for mask in range(33):
    net = ip_network('204.108.112.142/'+str(mask),0)
    if net.network_address == ip_address('204.108.64.0'):
        print(mask)