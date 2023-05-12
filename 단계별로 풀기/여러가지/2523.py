# 2523 : 별 찍기 13
# https://www.acmicpc.net/problem/2523

import sys

input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    print("*"*i)

for i in range(N-1, 0, -1):
    print("*"*i)