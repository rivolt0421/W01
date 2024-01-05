import sys
sys.stdin = open("완전탐색/input_36.txt","r")

n, m = map(int, input().split())
l = list(map(int, input().split()))

def combination(t, l):
    if t == 1:
        return [[x] for x in l]

    sc = []
    for i in range(len(l)):
        a = l[i]
        shit = combination(t-1, l[i+1:])
        for x in shit:
            x.insert(0,a)
        sc += shit
    return sc

cards_list = combination(3, l)
print(m-min(m-sum(cards) for cards in cards_list if sum(cards) <= m))
    

