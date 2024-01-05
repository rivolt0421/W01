import sys
sys.stdin = open("정렬/input_words.txt","r")

n, *l = sys.stdin.read().split()
n = int(n)

l = list(set(l))
l.sort(key=lambda x: len(x))

# 원소 뽑아서 정렬 후 출력 해주기
# for i in range(1,51):
#     words = [x for x in l if len(x)==i]
#     words.sort()
#     for w in words:
#         print(w)

# 같은 길이 단어들만 slicing해서 정렬하고 적용시키기
i=0; h=0
while i < len(l)-1:
    h = i   
    while h < len(l)-1 and len(l[h]) == len(l[h+1]):
        h += 1
    l[i:h+1] = sorted(l[i:h+1])
    i = h + 1

for word in l:
    print(word)