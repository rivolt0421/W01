import sys
sys.stdin = open("완전탐색/input_39.txt","r")
from itertools import *

n = int(input())
l = list(map(int, input().split()))
b = map(int, input().split())
r = ['+','-','*','//']
ops = []
for x,y in zip(b,r):
    for _ in range(x):
        ops.append(y)

ops = set(permutations(ops))

min = max = 0

for j,op in enumerate(ops):
    a = l[0]
    for i,num in enumerate(l[1:]):
        if op[i] == "//" and a*num < 0:
            a = -1 * (abs(a)//abs(num))
        else:
            exec("a"+op[i]+"="+str(num))

    if j == 0 : min = max = a

    if min > a : min = a
    if max < a : max = a

print(max)
print(min)

# 백트래킹 활용
# method 2
# def backtrack( prevVal, size, idx, plus, minus, multi, divide ):
# 	global max, min
# 	if size == N - 1:
# 		if max < prevVal:
# 			max = prevVal
# 		if min > prevVal:
# 			min = prevVal
# 	else:
# 		if plus:
# 			backtrack( prevVal + nums[idx], size + 1, idx + 1, plus - 1, minus, multi, divide )

# 		if minus:
# 			backtrack( prevVal - nums[idx], size + 1, idx + 1, plus, minus - 1, multi, divide )

# 		if multi:
# 			backtrack( prevVal * nums[idx], size + 1, idx + 1, plus, minus, multi - 1, divide )

# 		if divide:
# 			if prevVal < 0:
# 				backtrack( -(abs(prevVal) // nums[idx]), size + 1, idx + 1, plus, minus, multi, divide - 1 )
# 			else:
# 				backtrack( prevVal // nums[idx], size + 1, idx + 1, plus, minus, multi, divide - 1 )
# max = -(10**9+1)
# min = 10 ** 9 + 1
# backtrack( nums[0], 0, 1, *oper )