from itertools import *

k=0
for x in product('сало',repeat=6):
    s = ''.join(x)
    if s.count('о')<=3 and s.count('о')>=1:
        k+=1
print(k)