import sys
sys.stdin = open("정렬/input_sorting.txt","r")

n, *lst = map(int, sys.stdin.read().split())

def bi_insert_sort(l):
    for i in range(1,len(l)):
        key = l[i]
        pl = 0
        pr = i-1

        while True:
            pc = (pl+pr)//2

            if l[pc] == key:
                break
            
            # 언제나 가장 마지막 판정은 pl == pc == pr 인 상태에서 이루어짐.

            if l[pc] < key: # key가 중간값 보다 큰경우. 즉, 검색범위를 pc + 1 ~ 'pr' 로 재설정해야 하는 경우.
                            # pl == pc == pr 인 경우라면 key를 오른쪽에 둬야 하는 경우.
                            # 결국 뒤에서 pr+1 에 해당하는 곳에 넣어야 하기 때문에 pr은 현재값 그대로 두고, pl = pc+1만 해줌으로써 pl과 pr이 엇갈리게만 해준다.
                pl = pc + 1

            else : # key가 중간값 보다 작은 경우. 즉, 검색범위를 'pl' ~ pc - 1 로 재설정해야 하는 경우.
                   # pl == pc == pr 인 경우라면 key를 왼쪽에 둬야 하는 경우.
                   # 넣기 전에 모든 값은 오른쪽으로 한칸씩 밀리고 key를 지금 값의 왼쪽에 두어야 하기 때문에,
                   # pr = pc-1 해줌으로써 뒤에서 pr+1을 통해 현재의 pl==pc==pr의 위치에 삽입되도록 한다.
                pr = pc - 1

            if pl > pr: # pl pr 엇갈리면 반복문 나오기.
                break

        if pl < pr: # l[pc] (중간값) 이 key와 바로 같았던 경우.
            pd = pc + 1 # 중간값 오른쪽에 삽입하겠다.
        else :  # pl pr 엇갈려서 반복문 풀린 경우
            pd = pr + 1 # pr 오른쪽에 삽입하겠다.

        for j in range(i,pd,-1): # i부터 삽입지점 pd 까지 거꾸로
            l[j] = l[j-1]
        l[pd] = key

bi_insert_sort(lst)
for x in lst:
    print(x)