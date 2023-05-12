# 10214 : Baseball
# https://www.acmicpc.net/problem/10214

import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    A = 0
    B = 0
    for i in range(9):
        a, b = map(int, input().split())
        A += a
        B += b
    if A > B:
        print("Yonsei")
    elif A < B:
        print("Korea")
    else:
        print("Draw")