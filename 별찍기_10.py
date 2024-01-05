import math

def star(n):

    if n == 1 :
        return [
          "*"
         ]
    else:
        sc = []
        one = star(n//3)
        # 배열에 원소를 추가하는 건 새로운 줄을 추가하는 것과 같음.
        sc += [s*3 for s in one]
        sc += [s+ ' '*(n//3) +s for s in one]
        sc += [s*3 for s in one]

        return sc
            
for line in star(27):
    print(''.join(line))

print('@'.join(['1','2','3']))

# 배열 활용
# l = [['*' for _ in range(a+1)] for p in range(a+1)]
# for i,line in enumerate(l):
#     if i%3 == 2:
#         for j in range(2,a,3):
#             l[i][j] = ' '
    
# for n in range(1, round(math.log(a,3))):
#     w = 3**n
#     o = 3**(n+1)
#     for i in range(w+1, a, o):
#         for j in range(w+1, a, o):
#             for shit in range(w):
#                 for fuck in range(w):
#                     l[i+shit][j+fuck] = ' '

# for line in l[1:]:
#     print(''.join(line[1:]))
