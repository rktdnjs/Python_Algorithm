# 10773 : 제로
# https://www.acmicpc.net/problem/10773

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

List = deque([])

for i in range(N):
    number = int(input())
    if number == 0:
        List.pop()
    else:
        List.append(number)

print(sum(List)) 