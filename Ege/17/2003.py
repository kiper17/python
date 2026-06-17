f = open('17.txt')
a = [int(s) for s in f]

res = [x for x in a if x % 3 == 0 and x % 7 != 0 and x % 17 != 0 and x % 19 != 0 and x % 27 != 0]
print(len(res),max(res))