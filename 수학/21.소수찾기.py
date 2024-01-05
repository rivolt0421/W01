import sys
sys.stdin = open("input_21.txt","r")

# n, *l = map(int, sys.stdin.read().split())
# cnt = 0
# for x in l:
#     flag = False
#     for y in range(2,x):
#         if x % y == 0:
#             flag = True
#             break
#     if not flag:
#         cnt += 1

# filter(lambda x: map(lambda y: x % y ,[y for y in range(2,x)]) , l)
# print(cnt)

input()
print(sum(all(n%j for j in range(2,n))*n>1for n in map(int,input().split())))
# 개수를 셀 때 논리 연산자의 결과는 True(1, 'string', )
