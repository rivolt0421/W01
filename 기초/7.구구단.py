import sys
sys.stdin = open("input.txt","r")

n = int(input())

for i in range(1,10) :
    print(f'{n} * {i} = {n*i}')
