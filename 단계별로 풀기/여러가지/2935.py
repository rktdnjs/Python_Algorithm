# 2935 : 소음
# https://www.acmicpc.net/problem/2935

import sys

input = sys.stdin.readline

A = int(input())
cal = input().strip()
B = int(input())

if cal == "*":
    print(A*B)
else :
    print(A+B)