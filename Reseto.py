N,K = [int(j) for j in input().split()]
s = set()
c = 0
for i in range(2,N+1):
    for k in range(i,N+1,i):
        s.add(k)
        if len(s) == K:
            c = k
            print(c)
            break
    if len(s) == K:
        break