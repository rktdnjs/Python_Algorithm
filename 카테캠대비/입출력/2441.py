# 2441 : 별 찍기 4
# https://www.acmicpc.net/problem/2441

import sys

input = sys.stdin.readline

N = int(input().strip())

for i in range(N, 0, -1):
    print(" " * (N - i), end='')
    print("*" * i)