from itertools import combinations

n = 18
# l = [chr(x) for x in range(65, 74)]
l = [x for x in range(n)]
memo = [[1 if x == i else 0 for x in range(n)] for i in range(n)]
visited = [0 for _ in range(n)]

def go(l, N, n, memo):
    result = []
   
    for team in combinations(l, 3):
        team_out = False
        for x,y in combinations(team, 2):
            if memo[x][y] == 1 : team_out = True
        if team_out : continue

        if n == 1:
            return [team]
        else:
            sibal = go([x for x in l if x not in team], N, n-1, memo)
            if not sibal :
                continue
            tt = [team] + sibal

            if n < N:
                return tt

            else: # n == N
                for team in tt:
                    for x,y in combinations(team, 2):
                        memo[x][y] = 1
                        memo[y][x] = 1     
                print(tt)           
                result.append(tt)

    return result

go(l,n//3,n//3,memo)
for line in memo:
    print(line)


    
# result = []
# for first_team in combinations(l, 3):
#     first_team_out = False
#     for x,y in combinations(first_team, 2):
#         if memo[x][y] == 1 : first_team_out = True
#     if first_team_out : continue

#     for second_team in combinations([x for x in l if x not in first_team], 3):
#         second_team_out = False
#         for x,y in combinations(second_team, 2):
#             if memo[x][y] == 1 : second_team_out = True
#         if second_team_out : continue

#         third_team = tuple([x for x in l if x not in first_team and x not in second_team])
#         third_team_out = False
#         for x,y in combinations(third_team, 2):
#             if memo[x][y] == 1 : third_team_out = True
#         if third_team_out : continue

#         # 세 팀다 통과 되었을 때
#         teams = [first_team, second_team, third_team]
#         for team in teams:
#             for x,y in combinations(team, 2):
#                 memo[x][y] = 1
#                 memo[y][x] = 1

#         result.append(teams)

# for line in result:
#     print(line)

    


# while not all([sum(x) == n for x in memo]):
#     week = []
#     visited = [0 for x in range(n)]
#     for i in range(len(l)):
#         if visited[i] : continue

#         team = [l[i]]
#         visited[i] = 1

#         for j in range(len(l)):
#             if visited[j] == 1 : continue

#             flag = False
#             for one in [x for x in team if x != j]:
#                 if memo[j][one] == 1 : flag = True

#             if flag : continue
            
#             for one in [x for x in team if x != j]:
#                 memo[j][one] = 1
#                 memo[one][j] = 1
#             team += [l[j]]
#             visited[j] = 1
            
#             if len(team) == 3 : break

#         week.append(team)

#     print(week)


# perms = permutations(range(24), 24)

# cnt = 0
# for _, p in enumerate(perms):
#     flag = False
#     for i in range(0, 22, 3):
#         c = p[i:i+3]
#         for x,y in combinations(c, 2):
#             if memo[x][y] == 1 :
#                 flag = True
#                 break

#     if not flag:
#         for i in range(0, 22, 3):
#             c = p[i:i+3]
#             for x,y in combinations(c, 2):
#                 memo[x][y] = 1
#                 memo[y][x] = 1
#         print(_)
#         print(p)
#         print('------------------------------------------------------------------------------------------------')
#         for line in memo:
#             print(line)

#         cnt += 1

# print(cnt)