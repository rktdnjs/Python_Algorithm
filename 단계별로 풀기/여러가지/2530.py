# 2530 : 인공지능 시계
# https://www.acmicpc.net/problem/2530

import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

time = int(input())

# 총 초 계산하여 하루에 해당하는 초로 나눔
Time = (3600 * A  + 60 * B + C + time) % 86400
A = Time // 3600
Time %= 3600
B = Time // 60
C = Time % 60
print(A, B, C ,end=' ')