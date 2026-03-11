from itertools import *

k=0
for x in product('лодка',repeat=4):
    s = ''.join(x)
    if s.count('о')>=2:
        k+=1

print(k)