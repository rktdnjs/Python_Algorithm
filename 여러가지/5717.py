# 5717 : 상근이의 친구들
# https://www.acmicpc.net/problem/5717

import sys

input = sys.stdin.readline

while True:
    A, B = map(int, input().split())
    if A + B == 0:
        break
    print(A + B)