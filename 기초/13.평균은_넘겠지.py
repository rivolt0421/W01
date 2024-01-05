import sys
sys.stdin = open("input_13.txt","r")

c = int(input())

for i in range(c):
    l = map(int, input().split())
    n, *scores = l

    mean = sum(scores)/n
    print('{0:.3f}%'.format(100*len(list(filter(lambda x: x > mean, scores)))/n))