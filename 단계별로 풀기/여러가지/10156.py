# 10156 : 과자
# https://www.acmicpc.net/problem/10156

import sys

input = sys.stdin.readline

K, N, M = map(int, input().split())

total = K*N

if total > M:
    print(total - M)
else:
    print(0)