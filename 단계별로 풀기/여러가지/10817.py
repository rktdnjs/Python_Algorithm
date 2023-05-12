# 10817 : 세 수
# https://www.acmicpc.net/problem/10817

import sys

input = sys.stdin.readline

numbers = list(map(int, input().split()))

numbers.sort()

print(numbers[1])