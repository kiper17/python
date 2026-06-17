f = open('17.txt')
a = [int(s) for s in f]

res = [x for x in a if (x%10==2 or x%10==7 )and x %3==0 and x%11==0]
print(len(res),min(res))