from itertools import *

k=0
for x in product('абдеоп',repeat=6):
    s=''.join(x)
    k+=1
    if k%2==0:
        if s[0]=='о' and s.count('а')==1 and s.count('б')==1 and s.count('д')==1 and s.count('е')==1 and s.count('о')==1 and s.count('п')==1:
            print(k)