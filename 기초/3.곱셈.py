import sys
sys.stdin = open("input.txt","r")

up = int(input())
down = input()
print(up * int(down[2]))
print(up * int(down[1]))
print(up * int(down[0]))
print(up * int(down))