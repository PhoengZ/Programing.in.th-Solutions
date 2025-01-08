a = input()
for i in range(5):
    x =""
    y = 0
    for j in range(len(a)):
        if (j+1) %3 ==0:
            y +=1
        if i ==0 or i ==4:
            if j == 0:
                x = x+ "..#.."
            else:
                if y ==1:
                    y=0
                    x = x+".*.."
                else:
                    x = x+".#.."
        elif i ==1 or i ==3:
            if j == 0:
                x = x+".#.#."
            else:
                if y ==1:
                    y=0
                    x = x+"*.*."
                else:
                    x = x+"#.#."
        else:
            if j == 0:
                x = x+"#."+ a[j] +".#"
            elif j+1 == len(a):
                if (j+2) %3 == 0:
                    x = x+"."+a[j]+".#"
                else:
                    if y ==1:
                        y = 0
                        x = x+"."+a[j]+".*"
                    else:
                        x = x+"."+a[j]+".#"
                    
            else:
                if y ==1:
                    y=0
                    x = x+"."+a[j]+".*"
                elif (j+2) %3 == 0:
                    x = x+"."+a[j]+".*"
                else:
                    x = x+"."+a[j]+".#"
    print(x)