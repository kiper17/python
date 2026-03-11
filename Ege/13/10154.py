from ipaddress import *

for mask in range(33):
    net = ip_network('148.195.140.28/'+str(mask),0)
    if net.network_address ==ip_address('148.195.140.0'):
        print(mask) 