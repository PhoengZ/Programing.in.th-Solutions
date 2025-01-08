data = input().strip()
x = ""
symbols_check = ["a","e","i","o","u"]
i =0
while True:
    if i >=len(data):break
    if data[i] not in symbols_check:
        x+=data[i]
        i+=1
    else:
        if data[i+1] != "p" and data[i+2] != data[i]:
            x+=data[i]
            i+=1
        else:
            x+=data[i]
            i+=3
print(x)