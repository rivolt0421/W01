import random
import sys
sys.setrecursionlimit(10**6)
sys.stdin = open("정렬/input_sorting.txt","r")

n, *lst = map(int, sys.stdin.read().split())

# 삽입 정렬: 정렬된 배열의 범위를 점차 늘려나가는 방법. (<-> 정렬 해야할 범위를 점차 줄여나가는 방법. 예를 들어 선택 정렬)
# i 는 low에서 high '방향'으로 이동
# low ~ i-1 까지의 범위는 이미 정렬되어있는 상황이다. 맨 처음에는 그냥 하나의 값이 정렬되어 있다고 생각하는 것.
# 선택된 부분의 맨 오른쪽에 위치한 위치한 값, 즉 i 위치에 있는 값을 똑 뗀다. 그럼 배열에 빈칸이 생긴다.
# 왼쪽으로 탐색하면서, 지금 들고 있는 값(i 위치의 값) 보다 빈칸으로 민다.
# 지금 들고 있는 값보다 작거나 같은 원소를 만나면 더이상 밀지 않고 빈칸에 들고 있는 값을 넣는다. 그럼 low ~ i 까지의 범위가 정렬된 배열이 된다.
# 이 과정을 반복한다.
# 즉, '선택된 부분'은 맨 오른쪽 값과 그 왼쪽에 이미 정렬된 배열 로 나눌 수 있다. 맨 오른쪽 값을 그 정렬된 배열에 끼워넣기를 반복하는 것.
def insertion_sort(arr, low, high):
    for i in range(low+1, high+1):
        j = i
        key = arr[i]
        while j > 0 and arr[j-1] > key:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = key
        
        
def quick_sort(arr, low, high):
    if high-low < 20:
        insertion_sort(arr, low, high)
    else:
        pl = low
        pr = high
        pivot = arr[random.randrange(low, high+1)]
        
        while pl < pr:     # 1
            while arr[pl] < pivot : pl += 1     # 2
            while pivot < arr[pr] : pr -= 1   # 3

            if pl < pr:    # 4
                left = pl
                right = pr
                arr[left], arr[right] = arr[right], arr[left]
                
                pl += 1
                pr -= 1
            
        # 재귀 호출
        quick_sort(arr, low, pr)
        quick_sort(arr, pl, high)
        
quick_sort(lst, 0, len(lst)-1)
print(*lst)

# 퀵 소트가 좋은 경우
# == n*logn 의 시간복잡도에 근접하는 경우
# == 호출 트리의 좌우 균형이 잘 잡힌 경우
# == 분할 정복이 균등하게 잘 되는 경우
# == 재귀 호출 시의 pivot의 위치가 가운데에 가까운 경우
#
# 퀵 소트가 나쁜 경우
# == n^2 의 시간복잡도에 근접하는 경우
# == 호출 트리의 좌우 균형이 한 쪽으로 쏠린 경우
# == 분할 정복이 균등하게 잘 되지 않은 경우
# == 재귀 호출 시의 pivot의 위치가 왼쪽 or 오른쪽에 치우친 경우
# == 이미 정렬된 배열에서 처음 pivot의 위치를 맨 왼쪽 or 오른쪽으로 잡은 경우
# 
# 기억할 점
# - 좌/우 인덱스 (여기서는 pl, pr) 는 서로 pivot에서 만나게 된다.
# - 좌/우 인덱스  는 pivot을 '넘어가지는' 않는다.
#   둘 중 하나가 pivot에 닿은 경우, 그 뒤로 pivot은 둘 중 하나에 계속 붙어다님. #2, #3 의 조건 상 그럴 수 밖에 없음.
# - #1, #4 에 등호(=)가 붙음-안붙음의 차이는 결국 pivot에서 만난 좌/우 인덱스 의 위치를 재귀호출 시에 떨어트리느냐-아니냐의 차이.
#   재귀 호출 시에 각 호출의 끝 값과 시작값이 겹치는 것이 걱정될수 있지만,
#   결국 각 호출의 범위는 pivot 보다 작다/크다 가 보장되어 있음 -> '그' 끝 값과 시작 값은 각자의 범위에서 가장 큰/작은 값
#   -> (스스로를 포함한) 어떤 값이 pivot으로 정해지더라도 그 값이 이동할 일은 없다.
#   
#   
# 