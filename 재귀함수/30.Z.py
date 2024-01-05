import enum
import sys
sys.stdin = open("재귀함수/input_30.txt","r")

n, r, c = map(int, input().split())

def z(r,c,n):
    if n==1:
        return int('0b'+str(r)+str(c), 2)
    else:
        k = 2**(n-1)
        plus = 2**(2*(n-1))
        s = int('0b'+str(r//k)+str(c//k), 2)

        r = z(r%k, c%k, n-1)
        r += plus*s

        return r

print(z(r,c,n))

# 직접 그리기...
# def z(n):
#     sc =[]

#     if n == 2:
#         return [[0,1,4,5],
#                 [2,3,6,7],
#                 [8,9,12,13],
#                 [10,11,14,15]]
#     else:
#         a = z(n-1)
#         wh = 2**(2*(n-1))

#         b = [[x+(wh) for x in line] for line in a]

#         for i in range(2**(n-1)):
#             sc += [a[i] + b[i]]

#         sc += [[x+(wh*2) for x in line] for line in sc]

#         return sc

# print(z(n)[r][c])
        



