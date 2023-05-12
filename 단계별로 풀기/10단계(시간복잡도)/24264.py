# 24264 : 알고리즘 수업 - 알고리즘의 수행 시간3
# https://www.acmicpc.net/problem/24264

import sys

input = sys.stdin.readline

N = int(input())

print(N*N) # 2중 for문
print(2) # 시간복잡도O(N^2)