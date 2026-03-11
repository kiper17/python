# for n in range(1,100):
#     b = bin(n)[2:]
#     if b.count("1")%2 == 0:
#         b = b + "0"
#     else: 
#         b = b + "1"
#     if b.count("1")%2 == 0:
#         b = b + "0"
#     else: 
#         b = b + "1"
#     r = bin(b, 2)
#     if r>130:
#         print(n,r)


# for n in range(1,100):
#     b = bin(n)[2:]
#     b = b + b[-1]
#     if b.count("1")%2==0:
#         b = b + '0'
#     else:
#         b = b + "1"
#     if b.count("1")%2==0:
#         b = b + '0'
#     else:
#         b = b + "1"
#     r = int(b,2)
#     if r>97:
#         print(n, r)    


# for n in range(1,100):
#     b1 = b = bin(n)[2:]
#     b = b + b[-1]
#     if b1.count("1")%2==0:
#         b = b + "0"
#     else:
#         b = b + "1"
#     if b.count("1")%2==0:
#         b = b + "0"
#     else:
#         b = b + "1"
#     r = int(b,2)
#     if r>90:
#         print(n,r)


# for n in range(1,100):
#     b = bin(n)[2:]
#     if sum(map(int,b))%2==0:
#         b = b + '0'
#     else:
#         b = b + "1"
#     if sum(map(int,b))%2==0:
#         b = b + '0'
#     else:
#         b = b + "1"
#     r = int(b,2)
#     if 210<=r<=260:
#         print(n,r)


# for n in range(1,100):
#     b = bin(n)[2:]
#     if n%2 != 0:
#         b = "1" + b + "11"
#     else:
#         b = "11" + b + "00"
#     r = int(b, 2)
#     if r<237:
#         print(n,r)


# for n in range(1,100):
#     b = bin(n)[2:]
#     if sum(map(int, b))%2 ==0:
#         b = "10" +b[2:]+ "0"
#     else:
#         b = "11" +b[2:]+ "1"
#     r = int(b,2)
#     if r>=16:
#         print(n,r)


# def cc(x):
#     s = ""
#     d = "0123456789abcdefghijklmnopqrstuvwxyz"
#     while x>0:
#         s = d[x%12] + s
#         x = x//12
#     return s


# def cc(x):
#     s = ""
#     while x>0:
#         s = str(x%3) + s
#         x = x//3
#     return s

# for n in range(1,200):
#     b = cc(n)
#     if n%3==0:
#         b = "1" + b + "02"
#     else:
#         b = b + cc(n%3*4)
#     r = int(b,3)
#     if r<199:
#         print(n,r)


# def cc(x):
#     s = ""
#     d = "0123456789ab"
#     while x>0:
#         s = d[x%12] + s
#         x = x//12
#     return s
# for n in range(1,200):
#     b = cc(n)
#     if n%12==0:
#         b = b + b[-2] + b[-1]
#     else:
#         b = b + cc(n%12*9)
#     r = int(b,12)
#     if r>300:
#         print(n,r)


# for n in range(1,128):
#     b = bin(n)[2:].zfill(8)
#     b = b.replace("1","2").replace("0","1").replace("2","1")
#     r = int(b,2)
#     r = r+1
#     if r==153:
#         print(n,r)


# for n in range(1,100):
#     b = bin(n)[2:]
#     if len(b)%2==0:
#         b = b[:len(b)//2] + "1" + b[len(b)//2:]
#     r = int(b,2)
#     if r<=26:
#         print(n,r)


# for n in range(1000,10000):
#     d = [int(d) for d in str(n)]
#     a = d[0] + d[2]
#     b = d[1] + d[3]
#     if a<b:
#         r = int(str(a) + str(b))
#     else:
#         r = int(str(b) + str(a))
#     if r==1315:
#         print(n,r)


# k=0
# for n in range(100,1000):
#     d = str(n)
#     a = [d[0]+d[1], d[0]+d[2], d[1]+d[0], d[1]+d[2], d[2]+d[0], d[2]+d[1]]
#     a = [int(x) for x in a if x[0]!='0']
#     r = max(a)-min(a)
#     if r==35:
#         k+=1
#         print(n,r)
# print(k)


# for n in range(100,1000):
#     d = str(n)
#     a = [int(d[0] + d[1]), int(d[1]+d[2])]
#     r = max(a) - min(a) 
#     if r==26:
#         print(n,r)


# for n in range(1, 1000):
#     a = [int(d) for d in str(n)]
#     s1 = sum(d for d in a if d%2==0)
#     s2 = 0
#     for i in range((len(a))):
#         if (i+1)%2==0:
#             s2+=a[i]
#     r = abs(s2-s1)
#     if r==7:
#         print(n,r)


# for n in range(1,100000):
#     x = n
#     if x%3==0:
#         x = x//3
#     else:
#         x = x-1
#     if x%7==0:
#         x = x//7
#     else:
#         x = x-1
#     if x%11==0:
#         x = x//11
#     else:
#         x = x-1
#     if x==6:
#         print(n)


def f(n):
    b = bin(n)[2:]
    b = b + bin(n%3)[2:].zfill(2)
    r = int(b,2)
    b = b + bin(r%5)[2:].zfill(3)
    r = int(b,2)
    return r
st = 1_111_111_110 //32
for i in range(st-100,st+100):
    if f(i) >= 1_111_111_110:
        print(i)
        break
end = 1_444_444_416 //32
for i in range(end+100, end-100,-1):
    if f(i) <= 1_444_444_416:
        print(i)
        break