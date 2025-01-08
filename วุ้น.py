x = [int(e) for e in input().split()]
j = 0
while True:
    if x[0]==1 and x[1]== 1 and x[2]==1:
        break
    a = max(x)
    for i in range(3):
        if x[i] == a:
            if x[i] %2 == 0:
                x[i] = x[i]//2
            else:
                x[i] = x[i]-1
                x[i] = x[i]//2
                
            break
    j+=1
print(j)