from itertools import *

k=0
for x in product('abc','abc','abc','abc','abcx'):
    k+=1
print(k)