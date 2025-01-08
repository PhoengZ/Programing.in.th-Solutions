g = []
for i in range(5):
    a,b,c,d = [int(e) for e in input().split()]
    g.append(a+b+c+d)
k  = max(g)
j = g.index(k)
print(j+1,k)