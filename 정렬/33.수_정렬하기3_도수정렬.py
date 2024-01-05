import sys
sys.stdin = open("정렬/input_sorting.txt","r")

n = int(input())
cnt = [0 for _ in range(0,10001)]

for i in range(n):
    cnt[int(sys.stdin.readline())] += 1

for x in range(1,10001):
    if cnt[x] != 0:
        for y in range(cnt[x]):
            print(str(x))

# count sorting (도수 정렬 : 도수 분포표 활용)
#   -> 원소의 최대값 만큼 배열을 만들어서 원소 값에 해당하는 인덱스에 해당 원소의 count를 계속 업데이트.
# python에서 int 는 28byte.