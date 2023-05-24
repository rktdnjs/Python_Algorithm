# 28113 : 정보섬의 대중교통
# https://www.acmicpc.net/problem/28113

import sys

input = sys.stdin.readline

N, A, B = map(int, input().split())

if A < B:
    print("Bus")
elif A == B:
    print("Anything")
else:
    print("Subway")