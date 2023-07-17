# 1676 : 팩토리얼 0의 개수
# https://www.acmicpc.net/problem/1676

import sys
from math import factorial

input = sys.stdin.readline
count = 0

N = int(input())

N = list(str(factorial(N)))

numbers = list(reversed(N))

for i in numbers:
    if i == "0":
        count += 1
    else:
        break

print(count)