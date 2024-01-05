import itertools
import sys
sys.stdin = open("W01/완전탐색/input_38.txt","r")

n = int(input())
road = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [False for _ in range(n)]
result = []

def tour(road, visited, home, start, cost):
    visited[start] = True
    end = True

    for c in [i for i, v in enumerate(visited) if not v]:
        if road[start][c]:
            end = False
            print(start+1, c+1)
            tour(road, visited, home, c, cost + road[start][c])
    
    if end and all(visited) and road[start][home]:
        print(cost + road[start][home])
        result.append(cost + road[start][home])
    
    visited[start] = False
    return

# 원순열. 싸이클이 하나 정해지면 그 싸이클 안의 어떤 지점에서 시작해도 총 비용이 같다. 방향만 같으면.
tour(road, visited, 0, 0, 0)
print(result)

# 순열 활용한 풀이. 시간초과.
# l = [x for x in range(n)]
# l = itertools.permutations(l)

# result = []
# for line in l:
#     s = 0
#     flag = False
#     for x,y in zip(line, line[1:]+line[0:1]):
#         if not road[x][y]:
#             flag = True
#             break
#         s += road[x][y]
#     if not flag:
#         result.append(s)

# print(min(result))