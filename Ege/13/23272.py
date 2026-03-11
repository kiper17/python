from ipaddress import *

net = ip_network('205.99.68.249/255.255.248.0',0)
for ad in net:
    print(ad)

#Нужен предпоследний, тк когда 255 - то это широковещательный, а он служебный