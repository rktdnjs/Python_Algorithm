# 9610 : 사분면
# https://www.acmicpc.net/problem/9610

import sys

input = sys.stdin.readline

N = int(input())

where = [0 for x in range(5)]
# 1, 2, 3, 4, 축 순서대로 값 저장

for i in range(N):
    x, y = map(int, input().split())
    if x > 0 and y > 0:
        where[0] += 1
    elif x < 0 and y > 0:
        where[1] += 1
    elif x < 0 and y < 0:
        where[2] += 1
    elif x > 0 and y < 0:
        where[3] += 1
    else :
        where[4] += 1

print(f"Q1: {where[0]}")
print(f"Q2: {where[1]}")
print(f"Q3: {where[2]}")
print(f"Q4: {where[3]}")
print(f"AXIS: {where[4]}")
