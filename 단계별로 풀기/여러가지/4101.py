# 4101 : 크냐?
# https://www.acmicpc.net/problem/4101
# 딴 거 풀다 시간을 너무 많이 써서 걍 이거 품

import sys

input = sys.stdin.readline

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        if A > B:
            print('Yes')
        else:
            print('No')