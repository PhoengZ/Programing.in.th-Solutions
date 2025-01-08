m,n = [int(e) for e in input().split()]
c =[[int(i) for i in input().split()] for j in range(m)]
b =[[int(i) for i in input().split()] for j in range(m)]

for o in range(m):
    d = []
    for p in range(n):
        d.append(c[o][p] + b[o][p])
    result = " ".join(map(str,d))
    print(result)