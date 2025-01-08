a,b,c = [int(e) for e in input().split()]
if b-a-1 >= c-b-1:
    print(b-a-1)
elif c-b-1 >b-a-1:
    print(c-b-1)
else:print(b-a-1)