n  = int(input())
test = []
for i in range(n):
    x = int(input())
    test.append(x)
for j in test:
    if j%2 != 0 or j == 2:print("T")
    elif j == 0 :print("F")
    else:
        for k in range(2,j//2):
            if j%k == 0:
                print("F")
                break
        else:
            print("F")
