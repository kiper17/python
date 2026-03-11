def f(a, b, m):
    if a + b <= 60: return m % 2 == 0
    if m == 0: return 0
    h = [f(a-5, b, m-1), f(a, b-3, m-1), f(a // 2, b, m-1), f(a, b // 2 + b % 2, m-1)] 
    return any(h) if m % 2 != 0 else all(h) # чтобы найти ответ на 19, меняем all на any

print("19", [s for s in range(5, 151) if f(130, s, 2)])
print("20", [s for s in range(5, 151) if f(130, s, 3) and (not f(130, s, 1))])
# print("21", [s for s in range(5, 151) if f(130, s, 5) and (not f(130, s, 3)) and (not f(130,s,1))]) - это если самому произведение найти
a = [s for s in range(5, 151) if f(130, s, 5) and (not f(130, s, 3))]
pr = 1
for i in a:
    pr *= i
print(pr)