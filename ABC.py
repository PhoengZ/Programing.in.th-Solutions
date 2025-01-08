a = [int(i) for i in input().split()]
a.sort()
b = input().strip()
d = []
for i in b:
    if i == "A":d.append(str(a[0]))
    elif i =="B":d.append(str(a[1]))
    else:d.append(str(a[2]))
print(" ".join(d))