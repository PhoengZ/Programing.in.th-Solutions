def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a,b = [int(e) for e in input().strip().split()]
print(gcd(a,b))