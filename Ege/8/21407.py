from itertools import *

k=0
for x in product('дгиашэ',repeat=5):
    s = ''.join(x)
    if s[0] not in 'иаэ' and s[4] not in 'дгш':
        k+=1

print(k)