#80 Score
a,b = [int(e) for e in input().split()]
take_brick = []
for i in range(a):
    brick = input().strip()
    take_brick.append(brick)
fall_brick = [int(e) for e in input().split()]
result = [""]*a
for j in range(b):
    t = fall_brick[j]
    for k in range(a):
        if take_brick[k][j] == "O":
            c = b
            result[k]+="O"
            for l in range(k-1,-2,-1):
                if l == -1:
                    t = 0
                    break
                else:
                    if t == 0:break
                    else:
                        result[l] = result[l][:j] + "#"
                        t-=1
        else:
            if k+1 == a:
                if t!= 0:
                    result[k]+="#"
                else:result[k] += "."
            else:result[k] += "."
for p in result:print(p)