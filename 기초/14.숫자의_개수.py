import sys
sys.stdin = open("input_14.txt","r")

a, b, c = [num for num in map(int, sys.stdin.read().split())]
for i in range(10):
    print(str(a*b*c).count(str(i)))
