from ipaddress import *

for mask in range(33):
    net = ip_network('188.162.71.94/'+str(mask),0)
    if net.network_address == ip_address('188.162.71.64'):
        print(mask)