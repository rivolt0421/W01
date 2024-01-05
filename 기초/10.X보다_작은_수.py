import sys
sys.stdin = open("input.txt","r")

n, x = map(int, input().split())
list = list(map(int, input().split()))

for i in range(0,n):
    print(list[i]) if list[i] < x else ''
