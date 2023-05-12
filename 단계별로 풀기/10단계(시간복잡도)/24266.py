# 24264 : 알고리즘 수업 - 알고리즘의 수행 시간5
# https://www.acmicpc.net/problem/24266

import sys

input = sys.stdin.readline

N = int(input())

print(N*N*N) # 3중 for문
print(3) # 시간복잡도O(N^3)
