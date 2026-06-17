from re import *

s = open('24.txt').readline()
p = r'([ABC][89])+|([89][ABC])+'

print(max([len(x.group()) for x in finditer(p,s)]))