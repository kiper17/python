from re import *

s = open('24.txt').readline()
r = r'[123456789ABCDEF]+'

print(max([len(x.group()) for x in finditer(r,s)]))