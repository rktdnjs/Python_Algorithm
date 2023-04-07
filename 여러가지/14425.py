# 14425 : 문자열 집합
# https://www.acmicpc.net/problem/14425

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

strings = []
test = []

for i in range(N):
    strings.append(input())

for i in range(M):
    test.append(input())

count = 0

for word in test:
    if word in strings:
        count+= 1

print(count)