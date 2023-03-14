# 4153 : 직각삼각형
# https://www.acmicpc.net/problem/4153

import sys

input = sys.stdin.readline

while True:
    n = list(map(int, input().split()))
    n.sort() # 오름차순 정렬

    if n[0] == 0 and n[1] == 0 and n[2] == 0:
        break

    if n[0]**2 + n[1]**2 == n[2]**2:
        print('right')
    else:
        print('wrong')
