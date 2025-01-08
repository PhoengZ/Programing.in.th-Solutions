N = int(input())
Check = input().strip()
Score_ardrain = 0
Score_bruno = 0
Score_goran = 0
b= [["Adrian"],["Bruno"],["Goran"]]
for i in range(N):
    if (i+1)%3 == 1 and Check[i] == "A":
        Score_ardrain += 1
    if (i+1)%3 == 2 and Check[i] == "B":
        Score_ardrain += 1
    if (i+1)%3 == 0 and Check[i] == "C":
        Score_ardrain += 1
    if ((i+1)%4 == 1 or (i+1) %4 == 3) and Check[i] == "B":
        Score_bruno += 1
    if ((i+1)%4 == 2) and Check[i] == "A":
        Score_bruno += 1
    if ((i+1)%4 == 0) and Check[i] == "C":
        Score_bruno += 1
    if ((i+1)%6 == 1 or (i+1) %6 == 2) and Check[i] == "C":
        Score_goran += 1
    if ((i+1)%6 == 3 or (i+1) %6 == 4)and Check[i] == "A":
        Score_goran += 1
    if ((i+1)%6 == 5 or (i+1) %6 == 0) and Check[i] == "B":
        Score_goran += 1
Score_max = max(Score_ardrain,Score_bruno,Score_goran)
b[0].append(Score_ardrain)
b[1].append(Score_bruno)
b[2].append(Score_goran)
print(Score_max)
for j in range(len(b)):
    if Score_max == b[j][1] :
        print(b[j][0])