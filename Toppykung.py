n = int(input())
x = []
for i in range(n):
    k = input().strip()
    if k not in x:
        x.append(k)
x.sort()
for j in x:print(j)