import sys
sys.stdin = open("재귀함수/input_27.txt","r")

def draw(t, l):
    if t == 1:
        return [[x] for x in l]

    sc = []
    for i in range(len(l)):
        a = l[i]
        shit = draw(t-1, [l[j] for j in range(len(l)) if j != i])
        for x in shit:
            x.insert(0,a)
        sc += shit
    return sc


n, k, *cards = sys.stdin.read().split()

result = draw(int(k),cards)
print(len(set([''.join(x) for x in result])))
print(result)