from ipaddress import *

for mask in range(33):
    net = ip_network('98.162.75.91/'+str(mask),0)
    if net.network_address == ip_address('98.162.75.64'):
        print(mask)