from re import *

s = open('24.txt').readline()
num = [1234567890]
r = r'\d*(?:[+*]\d+)*'

print(max([len(x.group()) for x in finditer(r,s)]))

#хуй знает вообще чё за мутки с маской