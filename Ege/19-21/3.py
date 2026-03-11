def f(s, m, step):
    if s >= 231: return m % 2 == 0
    if m == 0: return 0
    if step == "P":
        h = [f(s + 3,m - 1,'V'), f(s * 3,m - 1, 'V')]
    else:
        h = [f(s + 5,m - 1,'P'), f(s * 3,m - 1, 'P')]
    return any(h) if m % 2 else all(h)

print("19", [s for s in range(10, 121) if f(s, 2, "P")])
print("20", [s for s in range(10, 121) if f(s, 3, "P")])
print("21", [s for s in range(10, 121) if f(s, 4, "P") and (not(f(s,2,'P')))])