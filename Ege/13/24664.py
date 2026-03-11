from ipaddress import ip_network

net = ip_network("0.0.0.0/255.255.192.0")

max_ip = None

for ad in net:
    print(ad)
    a, b, c, d = map(int, str(ad).split('.'))
    if a + b + c + d == 31:
        if max_ip is None or ad > max_ip:
            max_ip = ad

print(str(max_ip).replace('.', ''))