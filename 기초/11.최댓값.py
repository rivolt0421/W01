import sys
sys.stdin = open("input.txt","r")

list = []
while True :
    try:
        list.append(int(input()))
    except EOFError:
        break

max = list[0]
index = 0
for i, x in enumerate(list):
    if list[i] >= max:
        max = list[i]
        index = i+1

print(f'{max}\n{index}')
