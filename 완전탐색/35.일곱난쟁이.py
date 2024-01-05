import sys
sys.stdin = open("완전탐색/input_35.txt","r")

# 아홉명의 난쟁이의 키가 각각 주어진다.
# 일곱 난쟁이 키의 합은 100

l = [int(x) for x in sys.stdin.read().split()]

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

group_list = combination(7,l)
for group in group_list:
    if sum(group) == 100:
        for dwarf in sorted(group): print(dwarf)
        break
