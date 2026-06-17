from re import *

s = open('24.txt').readline()
r1 = r'(([1-9][0-9]*)|0)'
r2 = rf'(({r1}\*)*0(\*{r1})*)'
r3 = rf'{r2}(\+{r2})*'

print(max([len(x.group()) for x in finditer(r3,s)]))