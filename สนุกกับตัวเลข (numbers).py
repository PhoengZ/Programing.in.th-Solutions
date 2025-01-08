n = int(input())
x = [int(e) for e in input().split()]
x.sort()
c = ""
i = 0
while True:
    if len(c) == n:break
    if x[i] == 0:
        if i == 0:
            for j in range(i+1,n):
                if x[j] == 0:pass
                else:
                    c+=str(x[j])
                    break
            c+="0"*j
            i+=j+1
        else:
            c+=str(x[i])
            i+=1
    else:
        c+=str(x[i])
        i+=1
print(c)