# 2914 : 저작권
# https://www.acmicpc.net/problem/2914

import sys

input = sys.stdin.readline

A, B = map(int, input().split())

print(A * (B - 1) + 1)