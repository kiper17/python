from ipaddress import *

for mask in range(33):
    net = ip_network('84.23.84.23/'+str(mask),0)
    if net.network_address == ip_address('84.23.84.0'):
        print(mask)

print(int('11111111',2))
print(int('11100000',2))
print(255+224)