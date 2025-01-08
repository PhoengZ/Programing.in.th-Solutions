a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())
a7 = int(input())
a8 = int(input())
a9 = int(input())
y = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
x = sum(y)
dif = x-100
for i in y:
    for j in y:
        if i+j == dif:
            e = y.index(i)
            b = y.index(j)
            break

y.pop(e)
y.pop(b)
for k in y:print(k)
