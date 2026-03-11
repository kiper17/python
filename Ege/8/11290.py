from itertools import *

k=0
for x in product('0123456789abcdef',repeat=4):
    s = ''.join(x)
    if s[0]!='0' and s.count('9')==1:
        s = s.replace('0','2').replace('4','2').replace('6','2').replace('8','2').replace('a','2').replace('c','2').replace('e','2').replace('3','1').replace('5','1').replace('7','1').replace('9','1').replace('b','1').replace('d','1').replace('f','1')
        if '22' not in s and '11' not in s:
            k+=1

print(k)