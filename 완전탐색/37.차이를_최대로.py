import sys
sys.stdin = open("완전탐색/input_37.txt","r")

n, *l = map(int, sys.stdin.read().split())

def permute(t, l):
    if t == 1:
        return [[x] for x in l]

    sc = []
    for i in range(len(l)):
        a = l[i]
        shit = permute(t-1, [l[j] for j in range(len(l)) if j != i])
        for x in shit:
            x.insert(0,a)
        sc += shit
    return sc

print(max(sum(abs(x-y) for x,y in zip(l[1:],l)) for l in permute(n,l)))