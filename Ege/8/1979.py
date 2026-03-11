from itertools import *

k=0
for x in product('КРЕСЛО', repeat=4):
    s = ''.join(x)
    if s[0] in 'КРСЛ' and s[3] in 'ЕО':
        k+=1

print(k)