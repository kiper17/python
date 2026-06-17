from re import *

s = open('24.txt').readline()
r = r'([24][135])+'

print(max([len(x.group())//2 for x in finditer(r,s)]))