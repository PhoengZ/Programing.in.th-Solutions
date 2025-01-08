month_31 = [1,3,5,7,8,10,12]
month = 0
a,b = [int(e) for e in input().split()]
for i in range(1,b):
    if i in month_31:month+=31
    elif i == 2:month+=28
    else:month+=30
month+=a
if month % 7 == 1:print("Thursday")
elif month % 7 == 2:print("Friday")
elif month % 7 == 3:print("Saturday")
elif month % 7 == 4:print("Sunday")
elif month % 7 == 5:print("Monday")
elif month % 7 == 6:print("Tuesday")
else:print("Wednesday")