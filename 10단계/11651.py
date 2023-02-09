# 11651 : 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651

import sys

N = int(sys.stdin.readline()) # 입력받을 점의 개수
dots = []

for i in range(0, N):
    x, y = map(int, sys.stdin.readline().split())
    dots.append((x, y))

dots.sort(reverse=True)
for x, y in dots:
    print(x, y)