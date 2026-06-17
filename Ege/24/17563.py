from re import *

s = open('24.txt').readline()
r = r'[789][0789]*([-*][789][0789]*)*'

print(max([len(x.group()) for x in finditer(r,s)]))