# 2443 : 별 찍기 - 6
# https://www.acmicpc.net/problem/2443

import sys

input = sys.stdin.readline

N = int(input())

for i in range(N, 0, -1):
    print(" " * (N - i), end='')
    print("*" * (2*i - 1))