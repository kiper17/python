from ipaddress import *

net = ip_network(f'192.168.156.235/255.255.255.240',0)
print(int(ip_address('192.168.156.235')) - int(net.network_address))