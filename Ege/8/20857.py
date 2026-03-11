from itertools import *

k=0
for x in product('012345678',repeat=6):
    s =''.join(x)
    if s[0]!='0':
        k+=1
        s1 = s
        s1 = s1.replace('3','1').replace('5','1').replace('7','1')
        if '11' not in s1 and k%10==5:
            print(s,k)