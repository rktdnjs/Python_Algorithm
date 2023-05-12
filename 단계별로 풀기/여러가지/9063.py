# 9063 : 대지
# https://www.acmicpc.net/problem/9063
# 23.03.28 기준 9단계 기하 : 직사각형과 삼각형

import sys

input = sys.stdin.readline

N = int(input())

x = []
y = []

for i in range(N):
    A, B = map(int, (input().split())) # 나눠서 입력을 받음
    x.append(A)
    y.append(B)

if N == 1:
    print(0)
else:
    x_length = max(x) - min(x)
    y_length = max(y) - min(y)
    print(x_length * y_length)