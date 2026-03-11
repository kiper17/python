from itertools import *

k=0
for x in product('вишня',repeat=6):
    s = ''.join(x)
    if s.count('в')<=1 and s[0] != 'ш' and s[5]  in 'вшн':
        k+=1
print(k)