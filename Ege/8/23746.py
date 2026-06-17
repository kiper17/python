from itertools import *

k=0
for x in product('акорст',repeat=5):
    s=''.join(x)
    k+=1
    if k%2==0:
        if s.count('о')==2 and s[0] not in 'аст':
            print(k)