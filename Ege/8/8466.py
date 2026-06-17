from itertools import *

k=0
for x in product('0123456', repeat=6):
    s = ''.join(x)
    if s[0]!='0' and s[5] not in '0123':
        s = s.replace('1','3').replace('5','3').replace('0','2').replace('4','2').replace('6','2')
        if s.count('3') == s.count('2'):
            k+=1

print(k)