import sys
sys.stdin = open("input_12.txt","r")

from functools import reduce
n = int(input())

for i in range(n):
    list = input().split('X')
    #print(reduce(lambda score, x: score + (len(x)*(len(x)+1))//2, list, 0))
    print(sum([chunck_sum for chunck_sum in map(lambda o : (len(o)*(len(o)+1))//2, list)]))