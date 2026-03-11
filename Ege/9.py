count = 0
for line in open('...'): # название файла за место ...
    a = [int(x) for x in line.split()]
    # внизу пишем условия
    if max(a) < sum(a) - max(a):
        if ((a[0] + a[1]) == (a[2] + a[3])) or ((a[0] + a[2]) == (a[1] + a[3])) or ((a[0] + a[3]) == (a[2] + a[1])):
            count += 1 # количество строк подходящих по условию

print(count)