# 알고리즘 수업 - 점근적 표기 1
# https://www.acmicpc.net/problem/24313

import sys

input = sys.stdin.readline

a1, a2 = map(int, input().split())
c = int(input())
n = int(input())

fn = a1 * n + a2 # f(n)
gn = n * c       # g(n)

if fn <= gn and c >= a1:
    print(1)
else:
    print(0)