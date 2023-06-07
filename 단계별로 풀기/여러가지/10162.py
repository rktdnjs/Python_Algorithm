# 10162 : 전자레인지
# https://www.acmicpc.net/problem/10162

import sys

input = sys.stdin.readline

T = int(input())

a, b, c = 0, 0, 0

if T % 10 != 0:
    print(-1)
    exit()
if T >= 300:
    a = T // 300
    T = T % 300
if T >= 60:
    b = T // 60
    T = T % 60
if T >= 1:
    c = T // 10

print(a, b, c)