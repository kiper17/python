import math
def f(s, d, m):
    if s + d <= 200: return m % 2 == 0
    if m == 0: return 0
    h = [f(s-3, d-4, m-1), f(s-8, d//2, m-1), f(s // 2 + s % 2, d-10, m-1)]
    return any(h) if m % 2 != 0 else all(h)

print('19', [s for s in range(100, 1000) if f(110, s, 2)])
print('20', [s for s in range(100, 1000) if f(110, s, 3) and (not f(110, s, 1))])
print('21', [s for s in range(100, 1000) if f(110, s, 4) and (not f(110, s, 2))])