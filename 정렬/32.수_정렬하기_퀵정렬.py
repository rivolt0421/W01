# 퀵소트를 직접 구현하면 O(N^2)이 걸리는 데이터를 손쉽게 만들 수 있습니다. 그냥 내장된 정렬 함수를 쓰세요.
# 정렬을 직접 구현하는 것을 연습하시고자 한다면,
# 피벗을 랜덤으로 잡은 퀵소트를 구현하거나 힙소트, 머지소트 등 다른 O(nlogn) 정렬 알고리즘을 구현하는 방법이 있습니다.

# 피벗을 가운데에 두면 피벗이 어쨋든 움직이게 된다. 왜냐하면 피벗보다 큰 값의 개수와 피벗보다 작은 값의 개수가
# 항상 정확히 일치할 수 없기 때문이다. 차이가 나면 피벗의 위치가 이동할 수 밖에.
# 그렇다면 피벗이 가장 끝쪽으로 이동할 수 있게되고, 이게 반복되면 피벗을 맨 처음값으로 잡는 방법의 최악의 경우와 같아지게 된다.
#
# -> 약간은 개소리. 설욕의_복귀전을 참고할 것.

import sys
import random
sys.stdin = open("정렬/input_sorting.txt","r")
sys.setrecursionlimit(10**6)
n, *lst = map(int, sys.stdin.read().split())

def insertion_sort(l, low, high):
    for i in range(low+1, high+1):
        j = i
        v = l[i]
        while j>0 and l[j-1] > v:
            l[j] = l[j-1]
            j -= 1
        l[j] = v

def quick_sort(l, low, high):
    if high - low < 20:
        insertion_sort(l, low ,high)
    else:
        pl = low
        pr = high
        m = random.randrange(low, high+1)
        pivot = l[m]

        while pl <= pr:
            while l[pl] < pivot : pl += 1
            while l[pr] > pivot : pr -= 1

            if pl <= pr:
                l[pl], l[pr] = l[pr], l[pl]
                pl += 1
                pr -= 1
        
        quick_sort(l,low,pr)
        quick_sort(l,pl,high)

quick_sort(lst, 0, len(lst)-1)
print(*lst)




        

