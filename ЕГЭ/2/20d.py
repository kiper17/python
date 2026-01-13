from itertools import *

def f(x,y,z,w):
    return (x==(not z))<=((x or w)==y) # Меняем условие

for a1,a2,a3,a4,a5 in product([0,1], repeat=5): #Неизвестные
    t = [(0,a1,0,a2),(a3,a4,0,0),(a5,0,0,0)] #Табличка
    if len(t)==len(set(t)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p,r))) for r in t]==[0,0,0]: #Результат который должен получиться
                print(*p)