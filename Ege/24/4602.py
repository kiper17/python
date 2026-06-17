from re import *

s = open('24.txt').readline()
r = r'([BCD][AO])+'

print(max([len(x.group())//2 for x in finditer(r,s)]))