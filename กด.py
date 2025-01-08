x,y = [int(e) for e in input().split()]
step = 0
i= 0
if x>y:
    print(2)
else:
    while step <y:
        step+= x
        i+=1
    print(i)