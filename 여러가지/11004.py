# 11004 : K번째 수
# https://www.acmicpc.net/problem/11004

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

numbers = list(map(int, input().split()))

numbers.sort()

print(numbers[K-1]) 