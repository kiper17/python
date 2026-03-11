from itertools import *

k=0
for x in product('abcwxyz',repeat=6):
    s = ''.join(x)
    if s[0] in 'wxyz' and s[5] in 'wxyz' and s[1] in 'abc' and s[2] in 'abc' and s[3] in 'abc' and s[4] in 'abc':
        k+=1
print(k)