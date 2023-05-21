# 5063 : TGN
# https://www.acmicpc.net/problem/5063

import sys

N = int(input())

for i in range(N):
    r, e, c = map(int, input().split())
    if r < e - c:
        print("advertise")
    elif r == e - c:
        print("does not matter")
    else:
        print("do not advertise")