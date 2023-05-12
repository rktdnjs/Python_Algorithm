# 2522 : 별 찍기 12
# https://www.acmicpc.net/problem/2522

import sys

input = sys.stdin.readline

N = int(input().strip())

for i in range(N):
    print(" "*(N-i-1), end='')
    print("*"*(i+1))

for i in range(N-1):
    print(" "*(i+1), end='')
    print("*"*(N-i-1))