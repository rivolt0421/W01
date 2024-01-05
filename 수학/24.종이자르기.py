from functools import reduce
import sys
sys.stdin = open("input_24.txt","r")

# w, h = map(int, input().split())
# n = int(input())
# xl = []
# yl = []
# for i in range(n):
#     flag, z = map(int, input().split())
#     xl.append(z) if flag else yl.append(z)

# xl.sort()
# xl += [w]
# yl.sort()
# yl += [h]
# print(max(q*w for q in ([xl[0]]+[xl[i+1] - xl[i] for i in range(len(xl)-1)]) for w in ([yl[0]]+[yl[i+1] - yl[i] for i in range(len(yl)-1)])))

################백준 숏코딩####################
f = lambda: map(int, input().split())
w,h=f()
w=[0,w];h=[0,h]
for _ in range(f()):
    o, t = f()
    [h,w][o].append(t)

w.sort();h.sort()
print(max((b-a)*(d-c) for a,b in zip(w,w[1:]) for c,d in zip(h,h[1:])))


# 입력 값 받는 람다식 선언 후 unpacking과 함께 활용
# 원소 전 후로 계산 시 zip을 활용.




