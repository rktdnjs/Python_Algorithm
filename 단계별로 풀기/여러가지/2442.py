# 2442 : 별 찍기 5
# https://www.acmicpc.net/problem/2442

import sys

input = sys.stdin.readline

N = int(input().strip())

for i in range(N):
    print(" " * (N - i - 1), end='')
    print("*" * (2*i +1 ))