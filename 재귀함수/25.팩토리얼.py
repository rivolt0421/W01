from functools import reduce
import sys
sys.stdin = open("input.txt","r")

def factorial(x):
    return x * factorial(x-1) if x>1 else 1
print(factorial(int(input())))