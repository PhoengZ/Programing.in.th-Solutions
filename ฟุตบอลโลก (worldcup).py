teamlist = []
scorelist = []
team_point = []
different_point = []
team_goal = []
result = []
for i in range(4):
    teamlist.append(input().strip())
for j in range(4):
    score = [int(e) for e in input().split()]
    scorelist.append(score)
for k in range(4):
    point = 0
    goal = 0
    goal_diff = 0
    for l in range(4):
        if k == l:pass
        else:
            goal += scorelist[k][l]
            x= scorelist[k][l] - scorelist[l][k]
            goal_diff += x
            if x > 0:point+=3
            elif x == 0:point+=1
    different_point.append(goal_diff)
    team_goal.append(goal)
    team_point.append(point)
#team_point_sort = sorted(team_point)
for n in range(4):
    rank = 0
    for m in range(4):
        if team_point[n]>team_point[m]:rank+=1
        elif team_point[n]==team_point[m]:
            if different_point[n] > different_point[m]:rank+=1
            elif different_point[n] == different_point[m]:
                if team_goal[n]>team_goal[m]:rank+=1
    result.append(rank)
#print(different_point)
#print(result)
for p in range(3,-1,-1):
    print(teamlist[result.index(p)],team_point[result.index(p)])