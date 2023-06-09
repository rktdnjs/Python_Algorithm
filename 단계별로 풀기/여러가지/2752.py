# 2752 : 세수정렬
# https://www.acmicpc.net/problem/2752

import sys

input = sys.stdin.readline

numbers = list(map(int, input().split()))

numbers.sort()

for i in numbers:
    print(i, end=' ')