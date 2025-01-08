a = [int(e) for e in input().split()]
Area_list = []
for i in range(len(a)):
    b = a[:]
    b.pop(i)
    m1 = a[i]
    for j in range(len(b)):
        m2 = b[j]
        c = b[:]
        c.pop(j)
        for k in range(len(c)):
            m3 = c[k]
            d = c[:]
            d.pop(k)
            m4 = d[0]
            if m4 < m2 or m3 > m1:pass
            else:
                Area = (m3)*(m2)
                Area_list.append(Area)
print(max(Area_list))