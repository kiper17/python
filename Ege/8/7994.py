from itertools import *

k=0
for x in product('аклмня',repeat=5):
    s=''.join(x)
    k+=1
    if s[0]+s[1]=='мн':
        print(k)

print(4968-4753-1)