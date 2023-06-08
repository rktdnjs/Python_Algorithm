# 10103 : 주사위 게임
# https://www.acmicpc.net/problem/10103

import sys

input = sys.stdin.readline

N = int(input())

a, b = 100, 100

for i in range(N):
    A, B = map(int, input().split())
    if A > B:
        b -= A
    elif A == B:
        continue
    else:
        a -= B

print(a)
print(b)
