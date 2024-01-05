import sys
sys.stdin = open("input_22.txt","r")

numbers = list(map(int, sys.stdin.read().split()))[1:]
for x in numbers:
    for y in range(x // 2, 0, -1):
        if all(y%j for j in range(2,y)) and all((x-y)%j for j in range(2,y)) :
            print(x, ' -> ', y, x-y)
            break
