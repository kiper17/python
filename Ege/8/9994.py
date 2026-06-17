from itertools import *

k=0
for x in product('аклош',repeat=5):
    s=''.join(x)
    k+=1
    if s=='шалаш':
        print(k)