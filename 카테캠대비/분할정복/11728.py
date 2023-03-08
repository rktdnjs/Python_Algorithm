# 11728 : 배열 합치기
# https://www.acmicpc.net/problem/11728

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

array = 0
A = (list(map(int, input().split())))
B = (list(map(int, input().split())))

array = sorted(A + B)

for i in array:
    print(i, end=' ')