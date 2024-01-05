import sys
sys.stdin = open("input_20.txt","r")

from math import ceil
a, b, v = map(int, input().split())
print(ceil((v-b)/(a-b)))