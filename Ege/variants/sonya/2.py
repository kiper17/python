
# from itertools import *

# def f(x,y,z,w):
#     return (w or x or y) <= (((y or z) and x) or (y and (w or z)))

# for a1,a2,a3,a4 in product([0,1], repeat=4):
#     t = [(0,0,0,a1),(a2,1,1,a3),(a3,1,a4,1 )]    
#     if len(t)==len(set(t)):
#         for p in permutations("xyzw"):
#             if [f(**dict(zip(p,r))) for r in t]==[0,0,0]:
#                 print(p)


# def f(x):
#     s=''
#     while x>0:
#         s = str(x%4)+s
#         x=x//4
#     return s

# for n in range(1,112):
#     b = f(n)
#     if b[0]=='3':
#         b = b.replace('3','?').replace('1','3').replace('?','1')
#         b = '21' + b
#     else:
#         b = '1' + b[1:] + '12'
#     r = int(b,4)
#     if  r<598:
#         print(n,r)
    

# from turtle import *

# tracer(0)
# screensize(5000,5000)
# m=10

# for i in range(8):
#     fd(22*m)
#     rt(90)
#     fd(33*m)
#     rt(90)

# up()
# bk(8*m)
# rt(90)
# fd(11*m)
# lt(90)
# down()

# for i in range(8):
#     fd(73*m)
#     rt(90)
#     fd(62*m)
#     rt(90)      

# up()
# for x in range(-100,100):
#     for y in range(-100,100):
#         goto(x*m,y*m)
#         dot(3,'blue')

# update()
# exitonclick()

# from itertools import *

# k=0
# for x in product("абдеоп", repeat=6):
#     s = ''.join(x)
#     k+=1
#     cnt = [s.count(x) for x in s]
#     if s[0]=='о' and k%2==0 and cnt.count(1)==6:
#         print(k)


# k=0
# k1=0
# for line in open('Ege\Variants\sonya\9.txt'):
#     a = sorted([int(x) for x in line.split()])
#     k+=1
#     if (max(a)+min(a))>(a[1]**3 + a[2]**3):
#         if a[0] + a[3] != a[1]+a[2]:
#             k1+=k

# print(k1)


# from ipaddress import *

# # net = ip_network('192.168.12.207/255.192.0.0',0)
# # for ad in net:
# #     ed = f'{ad:b}'.zfill(32)
# #     if ed.count('0')==ed.count('1'):
# #         # print(ed, ed.count('0'))
        

# print(int('11000000101111111111111000000000',2))



# c = 30 * 36**231 + 18 * 6**101 - 3 * 36**45 -2357
# cc = []
# while c>0:
#     cc+= [str(c%36)]
#     c=c//36

# k=0
# for x in cc:
#     x = int(x)
#     if (x%5==0 and x%3!=0) or (x%5!=0 and x%3==0):
#         k+=1
    
# print(k)



# from functools import *

# @lru_cache(112)
# def f(n):
#     if n<15:
#         return 4
#     if n>=15 and n%3==0:
#         return f(2*n/3)+n-1
#     if n>=15 and n%3!=0:
#         return f(n-1)+3

# for n in range(112):
#     if f(n)==251:
#         print(n,f(n))




# # считываем числа из файла
# f = open('Ege\Variants\sonya\9.txt')
# a = [int(x) for x in f]

# k = 0      # количество подходящих троек
# mx_sum = 0 # максимальная сумма элементов тройки

# for i in range(len(a) - 2):
#     troika = a[i:i+3]

#     # 1) считаем числа, у которых первая и последняя цифра совпадают
#     cnt_same = 0
#     for x in troika:
#         if str(x)[0] == str(x)[-1]:
#             cnt_same += 1

#     # 2) считаем четырёхзначные числа,
#     # у которых цифры в разряде сотен равны 2
#     cnt_4 = 0
#     for x in troika:
#         if 112 <= x <= 9999 and (x // 100) % 10 == 2:
#             cnt_4 += 1

#     # проверяем условия
#     if cnt_same == 1 and cnt_4 == 2:
#         k += 1
#         mx_sum = max(mx_sum, sum(troika))

# print(k, mx_sum)




# def f(s, m):
#     if s >= 112:
#         return m % 2 == 0
#     if m == 0:
#         return 0
#     h = []
#     if (s + 1) % 2 == 0:
#         h.append(f(s + 1, m - 1))
#     if (s + 2) % 2 == 0:
#         h.append(f(s + 2, m - 1))
#     if (s * 2) % 2 == 0:
#         h.append(f(s * 2, m - 1))
#     return any(h) if m % 2 != 0 else all(h)


# print("19)", [s for s in range(1, 112) if not f(s, 1) and f(s, 2)])
# print("20)", [s for s in range(1, 112) if not f(s, 1) and f(s, 3)])
# print("21)", [s for s in range(1, 112) if not f(s, 2) and f(s, 4)])



from functools import lru_cache


def solve(d):
    @lru_cache(None)
    def f(x, y):
        if x > y:
            return 0
        if x == y:
            return 1
        return f(x + d, y) + f(x * 2, y)

    return f(1, 10) * f(10, 100)


for d in range(1, 200):
    if solve(d) == 13:
        print(d)
        break
