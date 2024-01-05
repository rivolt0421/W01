import sys
sys.stdin = open("input.txt","r")
sys.setrecursionlimit(10**8)

n = int(input())

def hanoi(number_of_disks_to_move, from_, to_, via_, flag):
    if number_of_disks_to_move == 1:
        if flag : print(from_, "->", to_)
    else:
        hanoi(number_of_disks_to_move-1, from_, via_, to_, flag)
        if flag : print(from_, "->", to_)
        hanoi(number_of_disks_to_move-1, via_, to_, from_, flag)

def move(n, frm, to):
    cnt = 0

    if n == 1:
        print(frm, to, sep=' ')
        return 1

    else:
        space = [x for x in [1,2,3] if x not in (frm, to)][0]

        cnt = move(n-1, frm, space) # 맨 밑을 제외한 원판들을 space로 이동시키고,
        print(frm, to, sep=' ') # 맨 밑단의 원판을 to로 이동시키는 것.
        cnt += 1

        cnt += move(n-1, space, to)
    return cnt

print(2**n-1)
if n <= 20 :
    move(n, 1, 3)
