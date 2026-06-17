from re import *

s = open('24.txt').readline()
r1 = r'([1-6][1-6]*)'
r2 = rf'[B]+{r1}((\-|\*){r1})*'

print(max([len(x.group()) for x in finditer(r2,s)]))