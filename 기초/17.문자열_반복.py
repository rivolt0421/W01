import sys
sys.stdin = open("input_17.txt","r")

n = int(input())
for i in range(n):
    time, string = input().split()
    for s in string:
        print(s*int(time), end='')
    print()
    