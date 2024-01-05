import sys
sys.stdin = open("input.txt","r")

cnt = 0
for x in range(1, int(input())+1):
    if x // 100 == 0:
        cnt += 1
        continue

    delta = int(str(x)[1]) - int(str(x)[0])
    cnt += all(int(str(x)[i]) + delta == int(str(x)[i+1]) for i in range(len(str(x))-1))

print(cnt)