# 3009 : 네 번째 점
# https://www.acmicpc.net/problem/3009

import sys

input = sys.stdin.readline

x = {}
y = {}

for i in range(3):
    A, B = map(int, (input().split()))
    if A in x :
        x[A] += 1
    if A not in x:
        x[A] = 1
    if B in y:
        y[B] += 1
    if B not in y:
        y[B] = 1

for key, value in x.items():
    if value == 1:
        print(key, end=' ')

for key, value in y.items():
    if value == 1:
        print(key)