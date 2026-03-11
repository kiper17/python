from ipaddress import *

for mask in range(33):
    net = ip_network('198.162.201.94/'+str(mask),0)
    if net.network_address == ip_address('198.162.192.0'):
        print(mask)