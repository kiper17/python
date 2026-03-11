from itertools import *

k=0
for x in product('алпця',repeat=5):
    s = ''.join(x)
    k+=1
    if s.count('а')<=1 and s.count('ц')==2 and s.count('л')==0:
        print(k)
        exit()